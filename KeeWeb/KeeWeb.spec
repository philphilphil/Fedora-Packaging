Name:    KeeWeb
Version: 1.4.0
Release: 3%{?dist}
Summary: Free cross-platform password manager compatible with KeePass 
URL:     https://github.com/keeweb/keeweb
License: MIT
BuildRequires: desktop-file-utils

Source0: https://github.com/keeweb/keeweb/releases/download/v%{version}/KeeWeb-%{version}.linux.x64.zip
Source1: %{name}.desktop


%description
Free cross-platform password manager compatible with KeePass 

%prep
%autosetup -c KeeWeb-%{version}

%install
mkdir -p %{buildroot}/opt
cp -r ../KeeWeb-%{version} %{buildroot}/opt/KeeWeb-%{version}
install -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/applications/KeeWeb.desktop
#desktop-file-validate %{buildroot}%{_datadir}/applications/KeeWeb.desktop

%files
/opt/KeeWeb-%{version}/*
%{_datadir}/applications/KeeWeb.desktop

%changelog
* Sat Mar 11 2017 Philipp Baum <phil@phib.io> - 1.4.0-3
- Changed installdir to /opt
* Sat Mar 11 2017 Philipp Baum <phil@phib.io> - 1.4.0-2
- Added Desktop-file
* Sat Mar 11 2017 Philipp Baum <phil@phib.io> - 1.4.0-1
- Initial package build