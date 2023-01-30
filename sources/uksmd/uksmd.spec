### The author of uksmd
# Oleksandr Natalenko <oleksandr@natalenko.name>
### The authors of linux-cachyos port:
# Piotr Gorski sirlucjan <piotrgorski@cachyos.org>
# Damian N. <nycko123@gmail.com>
### The port maintainer for Fedora:
# bieszczaders <zbyszek@linux.pl>
# https://copr.fedorainfracloud.org/coprs/bieszczaders/

%define _disable_source_fetch 0

Name:           uksmd
Summary:        Userspace KSM helper daemon (CachyOS branding)
Version:        1.0.0
Release:        3%{?dist}
License:        GPLv3
URL:            https://github.com/CachyOS/uksmd
Source0:        https://github.com/CachyOS/uksmd/archive/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  libcap-ng
BuildRequires:  libcap-ng-devel
BuildRequires:  procps-ng
BuildRequires:  procps-ng-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
Requires:       libcap-ng
Requires:       libcap-ng-devel
Requires:       procps-ng
Requires:       procps-ng-devel
%description
uksmd
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%autosetup -c

%build
cd %{name}-%{version}
sed -i 's/0.64.0/0.63.3/g' meson.build
%meson
%meson_build

%install
cd %{name}-%{version}
%meson_install

%files
/usr/bin/uksmd
/usr/bin/uksmdstats
/usr/lib/systemd/system/uksmd.service
/usr/share/licenses/uksmd/LICENSE

%changelog
* Mon Jan 30 2023 lucjan - 1.0.0-3
- Fix download bug

* Mon Jan 30 2023 lucjan - 1.0.0-2
- Fix debug files

* Mon Jan 30 2023 lucjan - 1.0.0-1
- Add uksmd for Fedora
