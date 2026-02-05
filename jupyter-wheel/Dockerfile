### xenocider/img:jupyter-wheel ###
# https://hub.docker.com/_/python
FROM python:3.12-alpine3.22
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
            openssh-client \
            openssh-server\
            openssh-sftp-server \
            nethogs \
            tmux \
            rsync \
            miniupnpc \
            ffmpeg \
            iptables \
            &&\
    apk add --no-cache \
            nodejs \
            yarn &&\
    rm -rf /root/.cache


RUN ssh-keygen -A && \
    echo "root:$RANDOM" | chpasswd &&\
    sed -i s/#\\?PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config &&\
    sed -i s/#\\?#PasswordAuthentication.*/PasswordAuthentication\ no/ /etc/ssh/sshd_config &&\
    sed -i s/X11Forwarding.*/X11Forwarding\ yes/ /etc/ssh/sshd_config &&\
    sed -i s/AllowTcpForwarding.*/AllowTcpForwarding\ yes/ /etc/ssh/sshd_config &&\
    sed -i s/#\\?X11UseLocalhost.*/X11UseLocalhost\ no/ /etc/ssh/sshd_config &&\
    sed -i s/#Port\ 22/Port\ 10222/ /etc/ssh/sshd_config &&\
    echo "PubkeyAcceptedKeyTypes=+ssh-rsa" >> /etc/ssh/sshd_config &&\
	echo StrictHostKeyChecking no>> /etc/ssh/ssh_config

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl &&\
    chmod +x ./kubectl &&\
    mv ./kubectl /usr/local/bin/kubectl

RUN wget https://github.com/mutagen-io/mutagen/releases/download/v0.16.6/mutagen_linux_amd64_v0.16.6.tar.gz &&\
    tar zxvf mutagen_linux_amd64_v0.16.6.tar.gz mutagen &&\
    chmod +x mutagen &&\
    mv mutagen /usr/local/bin

COPY --from=xenocider/img:lrzsz-musl /lrzsz-musl-0.12.20.tar /lrzsz-musl-0.12.20.tar
RUN tar -C / -xvf /lrzsz-musl-0.12.20.tar &&\
    rm /lrzsz-musl-0.12.20.tar &&\
    ln -s /usr/local/bin/lrz /usr/bin/rz &&\
    ln -s /usr/local/bin/lsz /usr/bin/sz

COPY --from=xenocider/img:wheel-jupyterlab /wheels /wheels
RUN pip3 install --no-cache-dir --no-index --find-links=/wheels jupyterlab

COPY --from=xenocider/img:wheel-pandas /wheels /wheels
RUN pip3 install --no-cache-dir --no-index --find-links=/wheels pandas

RUN pip3 install --no-cache-dir \
                 openpyxl \
                 dnspython \
                 pyotp

ADD start /

EXPOSE 38888
EXPOSE 10222
CMD ["/bin/sh", "/start"]
