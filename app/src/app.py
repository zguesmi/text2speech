import os, sys, subprocess, yaml

import custom_exceptions as customExceptions
from consensus import Consensus
from tts import TTS



class App:

    APP_CONFIG_FILE = '{}/../app-config.yml'.format(os.path.dirname(os.path.realpath(__file__)))
    _taskStartedFlag = '-> processing file {}'
    _taskEndedFlag = 'done..'
    _executionEndedFlag = 'Text files have been moved to "{}" folder. Sound files are saved in "{}" folder.'


    def __init__(self):

        yml = yaml.load( open(self.APP_CONFIG_FILE) )

        self._datadir = yml['datadir']
        self._inputConfigFile = '{}/{}'.format( yml['datadir'], yml['input-config'] )
        self._in = '{}/{}'.format( yml['datadir'], yml['input-dir'] )
        self._out = '{}/{}'.format( yml['datadir'], yml['output-dir'] )
        self._outputFileExtension = yml['output-files-extension']
        self._executionEndedFlag = self._executionEndedFlag.format( yml['input-dir'], yml['output-dir'] )

        self._inputConfig = self.parseConfigFile()

        self.prepareDatadir()


    def fullPath(self, filename):
        return '{}/{}'.format( self._datadir, filename )


    def inFullPath(self, filename):
        return '{}/{}'.format( self._in, filename )


    def outFullPath(self, filename):
        return '{}/{}.{}'.format( self._out, filename, self._outputFileExtension )


    def isNotConfigFile(self, filename):
        return self.fullPath(filename) != self._inputConfigFile


    def isTextFile(self, filename):
        return ( os.path.isfile(self.fullPath(filename))
            # and
            and self.isNotConfigFile(filename) )


    def parseConfigFile(self):

        if not os.path.isfile(self._inputConfigFile):
            raise customExceptions.ConfigFileNotFoundError(self._inputConfigFile)

        try:
            return yaml.load(open(self._inputConfigFile))
        except Exception as e:
            raise customExceptions.UnrespectedConfigFormatError(e)


    def prepareDatadir(self):
    
        try:
            os.mkdir(self._in)

            for f in [ f for f in os.listdir(self._datadir) if self.isTextFile(f) ]:
                subprocess.call([ 'mv', self.fullPath(f), self._in ])

            os.mkdir(self._out)

        except Exception as e:
            raise customExceptions.FatalError(e)


    def main(self):

        for filename, params in self._inputConfig.items():
            
            try:

                print(self._taskStartedFlag.format(filename))
                
                path = self.inFullPath(filename)

                if not os.path.isfile(path):

                    if os.path.isfile(self.fullPath(filename)):
                        raise customExceptions.FileTypeNotSupportedError(filename)

                    raise customExceptions.FileNotFoundError(filename)
                
                TTS().textToSpeech(
                    path=path,
                    voice=params['voice'],
                    latency=params['latency'],
                    out=self.outFullPath(filename)
                )
                
                print(self._taskEndedFlag)

            except customExceptions.CustomError:
                pass
            except Exception as e:
                print(e)

        print(self._executionEndedFlag)


if __name__ == '__main__':
    app = App()
    app.main()
    Consensus(app.APP_CONFIG_FILE).create()