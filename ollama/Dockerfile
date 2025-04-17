# https://hub.docker.com/_/python
FROM python:3.10.11-alpine3.17
LABEL maintainer="xenos <xenos.lu@gmail.com>"

ENV PS1 '\h:\w\$ '
ENV TZ 'Asia/Shanghai'

RUN apk add --no-cache \
            tzdata \
            &&\
            ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &&\
            echo $TZ > /etc/timezone &&\
    apk add --no-cache \
            docker-cli \
            curl \
            git \
            vim \
            tree \
            tmux \
            && \
    rm -rf /root/.cache

RUN curl -fsSL https://ollama.com/install.sh | sh
# RUN ollama pull wizardlm-uncensored:13b-llama2-q4_K_S
# RUN ollama pull deepseek-coder:1.3b
# RUN ollama pull tinyllama:1.1b

EXPOSE 11434
