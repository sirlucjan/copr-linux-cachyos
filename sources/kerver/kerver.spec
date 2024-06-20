%define _disable_source_fetch 0

Name:           kerver
Version:        1.1
Release:        1%{?dist}
Summary:        Kernel information script

License:        GPL           
Source0:        https://raw.githubusercontent.com/sirlucjan/copr-linux-cachyos/master/sources/kerver/kerver
    
%description
Kernel information script

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{SOURCE0} $RPM_BUILD_ROOT/%{_bindir}
chmod +x $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%{_bindir}/%{name}