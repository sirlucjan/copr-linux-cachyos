### The authors of linux-cachyos port:
# Piotr Gorski sirlucjan <piotrgorski@cachyos.org>
### The port maintainer for Fedora:
# bieszczaders <zbyszek@linux.pl>
# https://copr.fedorainfracloud.org/coprs/bieszczaders/

Name:           bore-sysctl
Summary:        Userspace KSM helper daemon (CachyOS branding)
Version:        1.0.5
Release:        1%{?dist}
Source0:        https://raw.githubusercontent.com/sirlucjan/CachyOS-Settings/master/etc/sysctl.d/99-bore-scheduler.conf
License:        GPLv3
URL:            https://github.com/sirlucjan/CachyOS-Settings

%description
BORE Scheduler sysctl settings

%install
mkdir -p %{buildroot}/etc/sysctl.d
cp -a %{_sourcedir}/99-bore-scheduler.conf %{buildroot}/etc/sysctl.d

%files
/etc/sysctl.d/99-bore-scheduler.conf
