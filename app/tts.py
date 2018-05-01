import argparse, cv2, os, sys
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image


class App:

    TEXT_PATH = './out.txt'

    def __init__(self):

        self.parseArgs()
        if not os.path.isfile(self.args['image']):
            sys.exit('No such file: {}'.format(self.args['image']))

    def parseArgs(self):

        argParser = argparse.ArgumentParser()
        argParser.add_argument('-i', '--image', required=True, help='Path to input image', type=str)
        argParser.add_argument('-l', '--language', required=True, help='Text\'s language', type=str,
            choices=['en', 'es', 'ar', 'fr', 'de', 'zh', 'it', 'ja', 'pt', 'ru', 'tr', 'ko'])
        argParser.add_argument('-p', '--preprocess', required=False, help='Type of preprocessing', type=str,
            choices=['thresh', 'blur'], default='thresh')
        
        self.args = vars(argParser.parse_args())

    def extractText(self):

    def saveText(self):

        try:
            file = open(self.TEXT_PATH, 'w')
            file.write(self.text)
        except Exception as e:
            print('Error writing text to file !\n{}'.format(e))
        finally:
            file.close()

    def main(self):

        self.extractText()
        self.saveText()

if __name__ == '__main__':
    App().main()
    