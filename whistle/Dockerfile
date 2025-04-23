# whistle v2.9.35
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
    rm -rf /root/.cache &&\
    yarn global add whistle
# yarn global add whistle@2.9.35


EXPOSE 8899
CMD ["w2", "run"]
