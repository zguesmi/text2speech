import os, sys, subprocess, yaml, yamlordereddictloader

import custom_exceptions as customExceptions
from consensus import Consensus
from tts import TTS


class Flag:

    taskStarted = '-> processing file {}'
    taskEnded = 'done..'
    executionEnded = 'Text files have been moved to "{}" folder. Sound files are saved in "{}" folder.'


class App:

    _PREFIX = 'original'
    _EXTENSION = '.wav'
    _appConfigFile = '{}/app-config.yml'


    def __init__(self):

        self._paths = {}
        self.flag = Flag()
        self.readAppConfigFile()
        self.readInputConfigFile()
        self.prepareDatadir()


    @property
    def datadir(self):
        return self._paths['/']


    @property
    def out(self):
        return self._paths['/out']


    def readAppConfigFile(self):

        dirname = os.path.dirname
        path = self._appConfigFile.format(dirname(dirname(os.path.realpath(__file__))))

        if not os.path.isfile(path):
            raise customExceptions.AppConfigNotFoundError(path)

        try:
            yml = yaml.load(open(path), yamlordereddictloader.SafeLoader)

            self._paths['/'] = yml['datadir']
            self._paths['/in'] = '{}/{}'.format(yml['datadir'], yml['input-dir'])
            self._paths['/out'] = '{}/{}'.format(yml['datadir'], yml['output-dir'])
            self._paths['conf'] = '{}/{}'.format(yml['datadir'], yml['input-config'])

            self.flag.executionEnded = self.flag.executionEnded.format(yml['input-dir'], yml['output-dir'])

        except Exception as e:
            raise customExceptions.IllegalAppConfigFormatError(e)


    def readInputConfigFile(self):

        if not os.path.isfile(self._paths['conf']):
            raise customExceptions.InputConfigNotFoundError(self._paths['conf'])

        try:
            self._inputConfig = yaml.load(open(self._paths['conf']), yamlordereddictloader.SafeLoader)
        except Exception as e:
            raise customExceptions.IllegalInputConfigFormatError(e)


    def getAbsPath(self, dirname, filename, extension=''):
        return '{}/{}{}'.format(self._paths[dirname], filename, extension)


    def isNotConfigFile(self, filename):
        return self.getAbsPath('/', filename) != self._paths['conf']


    def isFile(self, filename):
        return ( os.path.isfile(self.getAbsPath('/', filename)) and
            self.isNotConfigFile(filename) )


    def prepareDatadir(self):

        try:
            datadirContent = os.listdir(self._paths['/'])
            os.mkdir(self._paths['/in'])
            os.mkdir(self._paths['/out'])

            for filename in [ f for f in datadirContent if self.isFile(f) ]:
                subprocess.call([ 'mv', self.getAbsPath('/', filename), self._paths['/in'] ])

        except Exception as e:
            raise customExceptions.FatalError(e)


    def renameInputFiles(self):

        for filename in os.listdir(self._paths['/in']):
            oldPath = self.getAbsPath('/in', filename)
            newName = '{}-{}'.format(self._PREFIX, filename)
            newPath = self.getAbsPath('/in', newName)
            subprocess.call([ 'mv', oldPath, newPath ])


    def main(self):

        for filename, params in self._inputConfig.items():
            
            try:

                print(self.flag.taskStarted.format(filename))
                
                path = self.getAbsPath('/in', filename)

                if not os.path.isfile(path):

                    if os.path.isfile(self.getAbsPath('/', filename)):
                        raise customExceptions.FileTypeNotSupportedError(filename)

                    raise customExceptions.FileNotFoundError(filename)
                
                TTS().textToSpeech(
                    path=path,
                    voice=params['voice'],
                    latency=params['latency'],
                    out=self.getAbsPath('/out', filename)
                )
                
                print(self.flag.taskEnded)

            except customExceptions.CustomError:
                pass
            except Exception as e:
                print(e)

        self.renameInputFiles()

        print(self.flag.executionEnded)


if __name__ == '__main__':
    app = App()
    app.main()
    Consensus(datadir=app.datadir, outputdir=app.out)