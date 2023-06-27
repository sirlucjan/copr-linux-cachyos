FROM copr-cachyos:latest
RUN git clone https://github.com/sirlucjan/copr-linux-cachyos && \
    cd copr-linux-cachyos/sources/uksmd && \
    rpmdev-setuptree && \
    rpmbuild -bs --target=x86_64 uksmd-trunk.spec
