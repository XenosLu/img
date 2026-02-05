FROM alpine:3.15

RUN apk add --no-cache build-base &&\
    rm -rf /root/.cache

RUN wget https://ohse.de/uwe/releases/lrzsz-0.12.20.tar.gz &&\
    tar -zxvf lrzsz-0.12.20.tar.gz &&\
    cd lrzsz-0.12.20 &&\
    ./configure &&\
    make &&\
    DESTDIR=$(pwd)/dest make install &&\
    tar -C dest -cf /lrzsz-musl-0.12.20.tar usr
