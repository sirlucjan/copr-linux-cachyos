### The author of uksmd
# Oleksandr Natalenko <oleksandr@natalenko.name>
### The authors of linux-cachyos port:
# Piotr Gorski sirlucjan <piotrgorski@cachyos.org>
# Damian N. <nycko123@gmail.com>
### The port maintainer for Fedora:
# bieszczaders <zbyszek@linux.pl>
# https://copr.fedorainfracloud.org/coprs/bieszczaders/

%define _disable_source_fetch 0

Name:           uksmd-dev
Summary:        Userspace KSM helper daemon (CachyOS branding)
Version:        1.2.0
Release:        2%{?dist}
License:        GPLv3
URL:            https://github.com/CachyOS/uksmd
Source0:        %url/archive/v%{version}-rc2.tar.gz

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
Conflicts:      uksmd
%description
The daemon goes through the list of userspace tasks regularly and tells them to set MMF_VM_MERGE_ANY flag for
struct mm_struct for ksmd kthread to merge memory pages with the same content automatically. Only long-living tasks are processed.
The mechanism is wrapped around the per-process KSM API that has been introduced in with the upstream commit d7597f59d1.

This requires process_ksm_{enable,disable,status}() syscalls, that are available in linux-cachyos-bore/linux-cachyos-bore-lto kernels.

%prep
%setup -q -n uksmd-%{version}-rc2
%autosetup -c

%build
cd uksmd-%{version}-rc2
# Decreasing the meson version to satisfy dependencies
sed -i 's/0.64.0/0.63.3/g' meson.build
%meson
%meson_build

%install
cd uksmd-%{version}-rc2
%meson_install

%files
/usr/bin/uksmd
/usr/bin/uksmdstats
/usr/lib/systemd/system/uksmd.service
/usr/share/licenses/uksmd/LICENSE

%changelog
* Thu Feb 09 2023 lucjan - 1.1.0-1
- Update to 1.1.0

* Mon Jan 30 2023 lucjan - 1.0.0-4
- Improve spec file

* Mon Jan 30 2023 lucjan - 1.0.0-3
- Fix download bug

* Mon Jan 30 2023 lucjan - 1.0.0-2
- Fix debug files

* Mon Jan 30 2023 lucjan - 1.0.0-1
- Add uksmd for Fedora

