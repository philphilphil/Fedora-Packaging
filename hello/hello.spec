Name:    hello
Version: 2.10
Release: 1%{?dist}
Summary: GNU Hello
URL:     https://www.gnu.org/software/hello/
License: GPLv3+

Source0: https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz

%description
The GNU hello program produces a familiar, friendly greeting. It allows
nonprogrammers to use a classic computer science tool which would otherwise be
unavailable to them. Because it is protected by the GNU General Public License,
users are free (in perpetuity) to share and change it.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files

%changelog