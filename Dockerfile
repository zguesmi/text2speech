FROM ubuntu:16.04

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"

RUN apt-get update && apt-get install -y \
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
        wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install mimic tts engine
RUN git clone https://github.com/MycroftAI/mimic.git /mimic
WORKDIR /mimic
RUN ./dependencies.sh --prefix="/usr/local"
RUN ./autogen.sh
RUN ./configure --prefix="/usr/local"
RUN make

COPY ./app/ /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ['python3', 'tts.py']