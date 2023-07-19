### The authors of linux-cachyos port:
# Piotr Gorski sirlucjan <piotrgorski@cachyos.org>
### The port maintainer for Fedora:
# bieszczaders <zbyszek@linux.pl>
# https://copr.fedorainfracloud.org/coprs/bieszczaders/

%define _disable_source_fetch 0

Name:           bore-sysctl
Summary:        Userspace KSM helper daemon (CachyOS branding)
Version:        1.0.1
Release:        1%{?dist}
License:        GPLv3
URL:            https://github.com/sirlucjan/CachyOS-Settings

BuildRequires:  wget

%description
BORE Scheduler sysctl settings

%install
wget https://raw.githubusercontent.com/sirlucjan/CachyOS-Settings/master/etc/sysctl.d/99-bore-scheduler.conf
install -m 755 -d %{buildroot}/etc/sysctl.d
cp -a 99-bore-scheduler.conf %{buildroot}/etc/sysctl.d

%files
/etc/sysctl.d/99-bore-scheduler.conf
