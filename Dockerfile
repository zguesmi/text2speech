FROM ziedguesmi/mimic-tts:latest

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"

RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./app /text2speech

RUN pip3 install -r /text2speech/requirements.txt

RUN mkdir /iexec

WORKDIR /mimic

ENTRYPOINT [ "/text2speech/docker-start" ]