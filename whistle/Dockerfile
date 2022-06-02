FROM alpine:3.15
LABEL maintainer="xenos <xenos.lu@gmail.com>"

ENV PS1 '\h:\w\$ '
ENV TZ 'Asia/Shanghai'

RUN apk add --no-cache \
            tzdata \
            &&\
            ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &&\
            echo $TZ > /etc/timezone &&\
    apk add --no-cache \
            nodejs \
            yarn &&\
    rm -rf /root/.cache



EXPOSE 8899
CMD ["/bin/sh"]
