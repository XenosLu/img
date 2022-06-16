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
    apk add --no-cache \
            nginx &&\
    rm -rf /root/.cache

RUN yarn global add whistle

ADD start /
ADD nginx.conf /

EXPOSE 8899
EXPOSE 8898
# CMD ["w2", "start", "&&", "sleep", "infinity"]
CMD ["w2", "run"]
# CMD ["/bin/sh", "/start"]