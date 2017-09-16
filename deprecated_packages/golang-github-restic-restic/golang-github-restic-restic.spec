# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 0
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 0

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%global provider        github
%global provider_tld    com
%global project         restic
%global repo            restic
# https://github.com/restic/restic
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          f678c9734655c140e0e2dbf184eb86379e888a0d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        backup program
# Detected licences
# - BSD (2 clause) at 'LICENSE'
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if ! 0%{?with_bundled}
# src/cmds/restic/cmd_tag.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_init.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_find.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_key.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_snapshots.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_unlock.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_version.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_check.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/global_debug.go
BuildRequires: golang(github.com/pkg/profile)

# src/cmds/restic/cmd_mount.go
BuildRequires: golang(bazil.org/fuse)
BuildRequires: golang(bazil.org/fuse/fs)
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_restore.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/main.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/global.go
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)

# src/cmds/restic/cmd_ls.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_forget.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_prune.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_rebuild_index.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_list.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_backup.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_dump.go
BuildRequires: golang(github.com/spf13/cobra)

# src/cmds/restic/cmd_cat.go
BuildRequires: golang(github.com/spf13/cobra)

# Remaining dependencies not included in main packages
BuildRequires: golang(github.com/pkg/sftp)
BuildRequires: golang(github.com/elithrar/simple-scrypt)
BuildRequires: golang(golang.org/x/crypto/poly1305)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(github.com/restic/chunker)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(github.com/pkg/xattr)
BuildRequires: golang(github.com/minio/minio-go)
BuildRequires: golang(golang.org/x/sys/unix)
%endif

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(bazil.org/fuse)
BuildRequires: golang(bazil.org/fuse/fs)
BuildRequires: golang(github.com/elithrar/simple-scrypt)
BuildRequires: golang(github.com/minio/minio-go)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/pkg/sftp)
BuildRequires: golang(github.com/pkg/xattr)
BuildRequires: golang(github.com/restic/chunker)
BuildRequires: golang(golang.org/x/crypto/poly1305)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/sys/unix)
%endif

Requires:      golang(bazil.org/fuse)
Requires:      golang(bazil.org/fuse/fs)
Requires:      golang(github.com/elithrar/simple-scrypt)
Requires:      golang(github.com/minio/minio-go)
Requires:      golang(github.com/pkg/errors)
Requires:      golang(github.com/pkg/sftp)
Requires:      golang(github.com/pkg/xattr)
Requires:      golang(github.com/restic/chunker)
Requires:      golang(golang.org/x/crypto/poly1305)
Requires:      golang(golang.org/x/crypto/scrypt)
Requires:      golang(golang.org/x/crypto/ssh/terminal)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(golang.org/x/sys/unix)

Provides:      golang(%{import_path}/src/restic) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/archiver) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/backend) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/backend/local) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/backend/mem) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/backend/rest) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/backend/s3) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/backend/sftp) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/backend/test) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/checker) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/crypto) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/debug) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/errors) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/filter) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/fs) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/fuse) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/hashing) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/index) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/list) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/location) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/mock) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/pack) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/pipe) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/repository) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/test) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/walk) = %{version}-%{release}
Provides:      golang(%{import_path}/src/restic/worker) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif


%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{import_path}

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
export GOPATH=$(pwd):$(pwd)/vendor/src:%{gopath}
%endif

#%gobuild -o bin/ %{import_path}/
#%gobuild -o bin/src/cmds/restic %{import_path}/src/cmds/restic
#%gobuild -o bin/src/restic/backend/test %{import_path}/src/restic/backend/test

%install
install -d -p %{buildroot}%{_bindir}
#install -p -m 0755 bin/ %{buildroot}%{_bindir}
#install -p -m 0755 bin/src/cmds/restic %{buildroot}%{_bindir}
#install -p -m 0755 bin/src/restic/backend/test %{buildroot}%{_bindir}

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" | grep -v "vendor/src") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go" | grep -v "vendor/src") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor/src:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/src/cmds/restic
%gotest %{import_path}/src/restic
%gotest %{import_path}/src/restic/archiver
%gotest %{import_path}/src/restic/backend
%gotest %{import_path}/src/restic/backend/local
%gotest %{import_path}/src/restic/backend/mem
%gotest %{import_path}/src/restic/backend/rest
%gotest %{import_path}/src/restic/backend/s3
%gotest %{import_path}/src/restic/backend/sftp
%gotest %{import_path}/src/restic/backend/test
%gotest %{import_path}/src/restic/checker
%gotest %{import_path}/src/restic/crypto
%gotest %{import_path}/src/restic/filter
%gotest %{import_path}/src/restic/fuse
%gotest %{import_path}/src/restic/hashing
%gotest %{import_path}/src/restic/index
%gotest %{import_path}/src/restic/location
%gotest %{import_path}/src/restic/pack
%gotest %{import_path}/src/restic/pipe
%gotest %{import_path}/src/restic/repository
%gotest %{import_path}/src/restic/walk
%gotest %{import_path}/src/restic/worker
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
#%{_bindir}/
#%{_bindir}/src/cmds/restic
#%{_bindir}/src/restic/backend/test

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md
%endif

%changelog
* Tue Mar 21 2017 Philipp Baum - 0-0.1.gitf678c97
- First package for Fedora

