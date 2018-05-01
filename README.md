# TTS-Dapp

![dapp logo](./logo.png)


## Description
This dapp uses ..... to convert text to speech.  

## Usage
    # Help
    $ python3 tts.py -h

    # 
    $ python3 tts.py <......> 

## Supported languages
English (en), Spanish (es), Frensh (fr), Arabic (ar), German (de), Chinese simple (zh), Italian (it), Japanese (ja), Portuguese (pt), Russian (ru), Turkish (tr), Korean (ko).

## Dependencies
[python3](https://www.python.org/)  

## Docker installation
Install [docker](https://docs.docker.com/install/)

    $ docker run -v .:/app/ ziedguesmi/tts <......>
    $ open ./out.mp3

or

    # clone the dapp
    $ git clone https://github.com/Zied-Guesmi/tts-dapp.git

    # build the docker image
    $ cd tts-dapp/
    $ docker build -t tts-dapp .

    # run the docker container
    $ docker run -v .:/app/ tts-dapp <......>

    $ open ./out.mp3

## Native installation
Install system dependencies:

    $ apt-get update && apt-get install -y \
        python3 \
        python3-pip
        
Install python depedencies:

    $ git clone https://github.com/Zied-Guesmi/tts-dapp.git
    $ cd tts-dapp/app/
    $ pip3 install -r requirements.txt