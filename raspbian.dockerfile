# WIP compile mimic for raspberry pi - ziedguesmi/mimic-tts-raspbian

FROM ziedguesmi/mimic-tts-raspbian

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"
LABEL version="1.0"

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        && \
    pip3 install PyYAML yamlordereddictloader  --no-cache-dir && \
    apt-get remove -y python3-pip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /iexec

RUN [ "cross-build-end" ]

COPY ./app /text2speech

WORKDIR /mimic

ENTRYPOINT [ "/text2speech/entrypoint" ]