FROM fedora:38
RUN dnf -y install git rpmdevtools && \
    dnf clean all && \
    git clone https://github.com/sirlucjan/copr-linux-cachyos && \
    cd copr-linux-cachyos/sources/uksmd-dev && \
    git checkout develop && \
    rpmdev-setuptree && \
    rpmbuild -bs --target=x86_64 uksmd-dev.spec
