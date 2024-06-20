%define _disable_source_fetch 0

Name:           cachyos-settings
Release:        6%{?dist}
Version:	    1.0.0
Summary:        CachyOS-Settings ported to Fedora
License:        GPLv3
URL:            https://github.com/CachyOS/CachyOS-Settings
BuildRequires:  git

Requires: zram-generator

Provides: zram-generator-defaults
Obsoletes: zram-generator-defaults
Obsoletes: bore-sysctl
Obsoletes: kerver

%description
CachyOS-Settings for Fedora based systems

%prep
git clone -b %{version} %{URL} %{_builddir}/cachyos-settings

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_prefix}/lib
cp %{_builddir}/cachyos-settings/usr/{bin,lib} %{buildroot}/%{_prefix} -r
rm %{buildroot}/%{_bindir}/tunecfs*
chmod +x %{buildroot}/%{_bindir}/*

%files
%{_bindir}/*
%{_prefix}/lib/*

%changelog
%autochangelog





