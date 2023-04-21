# https://hub.docker.com/_/python
FROM python:3.11.3-alpine3.17

RUN apk add --no-cache \
            build-base \
            python3-dev \
            libffi-dev \
            openssl-dev \
            libc-dev \
            py3-pyzmq &&\
    rm -rf /root/.cache

RUN pip3 install wheel \
                 setuptools \
                 &&\
    pip3 wheel pandas --wheel-dir=/wheels &&\
    ls -l /wheels

# How to use:
# COPY --from=xenocider/image:wheel-pandas-cp38-alpine /wheels /wheels
# RUN pip3 install --no-cache-dir --no-index --find-links=/wheels pandas
