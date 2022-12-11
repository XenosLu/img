# xenocider/image:bullseye-workspace-base
FROM python:3.10.8-slim-bullseye
# https://hub.docker.com/_/python
LABEL maintainer="xenos <xenos.lu@gmail.com>"
ENV LANG "C.UTF-8"
ENV TZ 'Asia/Shanghai'

# basic component and configuration
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &&\
    echo $TZ > /etc/timezone &&\
    apt-get update &&\
    apt-get install -y --no-install-recommends \
            tzdata \
            openssh-server
            
# utilities     
RUN apt-get install -y --no-install-recommends \
            docker.io \
            vim \
            curl \
            tmux \
            lrzsz \
            gnupg \
            ntpdate \
            git \
            wget \
            miniupnpc \
            net-tools \
            inetutils-ping

# COPY requirements.txt ./
# RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir -U pip
RUN pip3 install --no-cache-dir pyotp
RUN pip3 install --no-cache-dir xenoslib
RUN pip3 install --no-cache-dir easyocr

RUN mkdir -p /run/sshd &&\
    sed -i "s/^\(deb.*http:\/\/\).*\(\/debian\)/\1mirrors.aliyun.com\2/g" /etc/apt/sources.list


CMD ["/usr/sbin/sshd", "-D", "-E", "/var/log/sshd"]
