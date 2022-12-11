# xenocider/testone:latest
FROM python:3.8.16-alpine3.16
# https://hub.docker.com/_/python
LABEL maintainer="xenos <xenos.lu@gmail.com>"
ENV LANG "C.UTF-8"
ENV PS1 '\h:\w\$ '
ENV TZ 'Asia/Shanghai'

COPY . /one

RUN apk add --no-cache \
            tzdata \
            ffmpeg \
            &&\
            ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &&\
            echo $TZ > /etc/timezone &&\
            pip3 install --no-cache-dir pip --upgrade &&\
            pip3 install --no-cache-dir -r /one/requirements.txt

CMD ["/bin/sh"]
