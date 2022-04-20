FROM  python:3.8.13-alpine3.15

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
    pip3 wheel jupyterlab --wheel-dir=/wheels &&\
    ls -l /wheels

# How to use:
# COPY --from=xenocider/image:wheel-jupyterlab /wheels /wheels
# RUN pip3 install --no-cache-dir --no-index --find-links=/wheels jupyterlab
