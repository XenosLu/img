# https://hub.docker.com/_/python
FROM python:3.11.3-alpine3.17

RUN apk add --no-cache \
            cargo \
            libffi-dev &&\
    rm -rf /root/.cache

RUN pip3 install wheel \
                 setuptools \
                 &&\
    pip3 wheel jupyterlab --wheel-dir=/wheels &&\
    ls -l /wheels

# How to use:
# COPY --from=xenocider/image:wheel-jupyterlab /wheels /wheels
# RUN pip3 install --no-cache-dir --no-index --find-links=/wheels jupyterlab
