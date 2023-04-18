FROM fedora:37
RUN dnf -y install git rpmdevtools && \
    dnf clean all && \
    git clone https://github.com/sirlucjan/copr-linux-cachyos && \
    cd copr-linux-cachyos/sources/uksmd && \
    rpmdev-setuptree && \
    rpmbuild -bs --target=x86_64 uksmd.spec
