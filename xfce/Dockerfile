# xenocider/container:xfce
FROM ubuntu:18.04
LABEL maintainer="xenos <xenos.lu@gmail.com>"
ENV LANG "C.UTF-8"

ENV TZ 'Asia/Shanghai'

# basic component and configuration
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime &&\
    echo $TZ > /etc/timezone &&\
    apt-get update &&\
    apt-get install -y --no-install-recommends \
            openssh-server \
            x2goserver \
            xfce4 \
            gvfs \
            sshfs \
            x2goserver-fmbindings  \
            xubuntu-icon-theme \
            greybird-gtk-theme \
            xfce4-terminal \
            rdesktop \
            gedit \
            mpv &&\
    apt-get install -y --no-install-recommends \
            fcitx \
            fcitx-pinyin \
            fcitx-ui-classic \
            fcitx-frontend-gtk3 \
            fcitx-config-gtk

RUN apt-get install -y \
            fonts-arphic-ukai \
            fonts-arphic-uming \
            fonts-croscore \
            fonts-droid-fallback \
            fonts-kacst \
            fonts-kacst-one \
            fonts-noto \
            fonts-noto-cjk \
            fonts-noto-color-emoji \
            fonts-noto-hinted \
            fonts-noto-mono \
            fonts-noto-unhinted \
            fonts-open-sans \
            fonts-opendyslexic \
            fonts-roboto \
            fonts-roboto-hinted \
            fonts-sil-mondulkiri \
            fonts-sil-padauk

RUN apt-get install -y --no-install-recommends \
            fonts-ubuntu

RUN apt-get install -y \
            epiphany-browser
RUN apt-get install -y \
            geany

# apt-get install -y software-properties-common &&\
# add-apt-repository -y ppa:mozillateam/ppa &&\
# apt-get install -y  firefox-esr


RUN mkdir -p /run/sshd &&\
    sed -i s/#\\?X11UseLocalhost.*/X11UseLocalhost\ no/ /etc/ssh/sshd_config &&\
    mkdir -p /var/run/dbus &&\
    sed -i "s/^\(deb.*http:\/\/\).*\(\/ubuntu\)/\1mirrors.163.com\2/g" /etc/apt/sources.list

ADD start /

CMD ["/bin/sh", "/start"]
