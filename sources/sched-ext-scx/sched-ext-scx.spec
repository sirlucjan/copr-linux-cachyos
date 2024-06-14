%define _disable_source_fetch 0

Name:           sched-ext-scx
Version:        0.1.10
Release:        1%{?dist}
Summary:        Sched_ext Schedulers and Tools

License:        GPV=2.0
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  meson >= 1.2
BuildRequires:  python
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang >= 17
BuildRequires:  llvm >= 17
BuildRequires:  lld >= 17
BuildRequires:  bpftool
BuildRequires:  libbpf >= 1.3
BuildRequires:  libbpf-devel >= 1.3
BuildRequires:  elfutils-libelf
BuildRequires:  elfutils-libelf-devel
BuildRequires:  zlib
BuildRequires:  jq
BuildRequires:  jq-devel
BuildRequires:  systemd
Requires:  libbpf
Requires:  elfutils-libelf
Requires:  zlib
Requires:  jq

%description
bebebeba

%prep
%autosetup -n scx-%{version}

%build
%meson \
 -Dsystemd=enabled \
 -Dopenrc=disabled \
 -Dlibalpm=disabled
%meson_build


%install
%meson_install


%files
%{_bindir}/*
%{_prefix}/lib/systemd/system/scx.service
%{_sysconfdir}/default/scx
%{_sysconfdir}/systemd/journald@sched-ext.conf
