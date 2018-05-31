FROM ziedguesmi/mimic-tts:latest

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"
LABEL version="1.0"

COPY requirements.txt /text2speech/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        && \
    pip3 install -r /text2speech/requirements.txt  --no-cache-dir && \
    rm /text2speech/requirements.txt && \
    apt-get remove -y python3-pip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /iexec

COPY ./app /text2speech

WORKDIR /mimic

ENTRYPOINT [ "/text2speech/entrypoint" ]