Name:    restic
Version: 0.5.0
Release: 1%{?dist}
Summary: Backup program
URL:     https://restic.github.io
License: BSD

BuildRequires: golang
Source0: https://github.com/restic/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%define debug_package %{nil}

%description
restic is a backup program that is fast, efficient and secure.

%prep
%autosetup

%build
go run build.go

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}/%{_bindir}

%files
%{_bindir}/%{name}

%license LICENSE

%changelog
* Wed Mar 15 2017 Philipp Baum <phil@phib.io> - 0.5.0-1
- Initial package build
