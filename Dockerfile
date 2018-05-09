FROM ziedguesmi/mimic-tts:latest

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"

RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./app/ /tts

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ['/tts/docker-start']