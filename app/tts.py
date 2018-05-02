import argparse, os, sys, subprocess


class TTS:
        
    def textToSpeech(self, filename, voice, latency, out):
        cmd = [ "/mimic/mimic", "-f", filename, "-voice", voice, "--setf", "duration_stretch={}".format(latency), "-o", out ]
        try:
            subprocess.call(cmd)
        except Exception as e:
            sys.exit(e)


class App:

    OUTPUT_FILE = 'out.wav'     

    def __init__(self):
        self.parseArgs()
        if not os.path.isfile(self.args['file']):
            sys.exit('No such file: {}'.format(self.args['file']))

    def parseArgs(self):

        argParser = argparse.ArgumentParser()
        argParser.add_argument('-f', '--file', required=True, help='Path to input file', type=str)
        argParser.add_argument('-v', '--voice', required=False, help='Speech\'s voice', type=str,
            choices=['ap', 'slt', 'slt_hts', 'kal', 'awb', 'kal16', 'rms', 'awb_time'], default='ap')
        argParser.add_argument('-lat', '--latency', required=False, help='Speech\'s latency', type=str,
            choices=[str(p/10) for p in range(0, 20)], default='1.0')

        self.args = vars(argParser.parse_args())

    def main(self):

        TTS().textToSpeech(
            filename=self.args['file'],
            voice=self.args['voice'],
            latency=self.args['latency'],
            out=self.OUTPUT_FILE
        )

if __name__ == '__main__':
    App().main()
    