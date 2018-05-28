# WIP compile mimic for raspberry pi - ziedguesmi/mimic-tts-raspbian

FROM ziedguesmi/mimic-tts-raspbian

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /iexec

COPY ./app /text2speech

RUN pip3 install PyYAML yamlordereddictloader

RUN [ "cross-build-end" ]

WORKDIR /mimic

ENTRYPOINT [ "/text2speech/docker-start" ]