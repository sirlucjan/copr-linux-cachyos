%define _disable_source_fetch 0

Name:           cachyos-settings
Release:        2%{?dist}
Version:	    1.0.0
Summary:        CachyOS-Settings ported to Fedora
License:        GPLv3
URL:            https://github.com/CachyOS/CachyOS-Settings
BuildRequires:  git

%description
CachyOS-Settings for Fedora based systems

%prep
git clone -b %{version} %{URL} %{_builddir}/cachyos-settings

%install
mkdir -p %{buildroot}/%{_prefix}
cp %{_builddir}/cachyos-settings/usr/{bin,lib} %{buildroot}/%{_prefix} -r
chmod +x %{buildroot}/%{_bindir}/*

%files
%{_prefix}/*






