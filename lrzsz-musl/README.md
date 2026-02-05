# How to use:
# In dockerfile:
COPY --from=xenocider/img:lrzsz-alpine /lrzsz-musl-0.12.20.tar /lrzsz-musl-0.12.20.tar
RUN mkdir extract &&\
    tar -C extract -xvf /lrzsz-0.12.20.tar &&\
    cp -r extract/* / &&\
    rm -rf extract/ &&\
    ln -s /usr/local/bin/lrz /usr/bin/rz &&\
    ln -s /usr/local/bin/lsz /usr/bin/sz
