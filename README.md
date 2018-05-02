# TTS-Dapp

![dapp logo](./logo.svg)


## Description
This dapp uses [mimic](https://github.com/MycroftAI/mimic) text-to-speech engine to convert text files to speech.  

## Usage
    ```
    # Help
    $ python3 tts.py -h

    # Speak a text file
    $ python3 tts.py -f foo.txt -v ap -lat 0.9
    $ <open> out.wav
    ```

## Supported languages
English (until now)

## Voices
See voice samples [here](https://github.com/Zied-Guesmi/tts-dapp.git).

## Dependencies
[python3](https://www.python.org/)  
[mimic](https://github.com/MycroftAI/mimic)  

## Docker installation
* Install [docker](https://docs.docker.com/install/)
* Get the docker image from docker hub
    ```
    $ docker run -v .:/app/ ziedguesmi/tts -f foo.txt
    $ <open> ./out.wav
    ```

* or build the image locally
    ```
    # clone the dapp
    $ git clone https://github.com/Zied-Guesmi/tts-dapp.git

    # build the docker image
    $ cd tts-dapp/
    $ docker build -t tts-dapp .

    # run the docker container
    $ docker run -v .:/app/ tts-dapp -f foo.txt

    $ <open> ./out.mp3
    ```

## Installation
Install system dependencies:
    ```
    $ apt-get update && apt-get install -y \
        automake \
        gcc \
        git \
        libasound2-dev \
        libtool \
        make \
        pkg-config \
        python3 \
        python3-pip \
        unzip \
        wget
    ```

Install mimic tts engine
    ```
    $ git clone https://github.com/MycroftAI/mimic.git
    $ cd ./mimic
    $ ./dependencies.sh --prefix="/usr/local"
    $ ./autogen.sh
    $ ./configure --prefix="/usr/local"
    $ make
    ```

Clone the tts-dapp
    ```
    $ cd ..
    $ git clone https://github.com/Zied-Guesmi/tts-dapp.git
    ```

Install python depedencies:

    $ cd tts-dapp/app/
    $ pip3 install -r requirements.txt


## TODO
Add directory support.