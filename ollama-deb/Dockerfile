# https://hub.docker.com/_/python
FROM python:3.10-slim-bullseye
LABEL maintainer="xenos <xenos.lu@gmail.com>"
ENV LANG="C.UTF-8"
RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
    apt-get update &&\
    apt-get install -y wget \
                       curl \
                       jq \
                       git \
                       make \
                       gnupg \
                       g++ \
                       &&\
    pip3 install pip --upgrade &&\

RUN curl -fsSL https://ollama.com/install.sh | sh
# RUN curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz &&\
#    tar -C /usr -xzf ollama-linux-amd64.tgz
# RUN ollama pull wizardlm-uncensored:13b-llama2-q4_K_S
# RUN ollama pull deepseek-coder:1.3b
# RUN ollama pull tinyllama:1.1b

EXPOSE 11434

CMD ["/bin/sh"]
