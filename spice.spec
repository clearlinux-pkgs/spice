#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spice
Version  : 0.12.8
Release  : 14
URL      : http://www.spice-space.org/download/releases/spice-0.12.8.tar.bz2
Source0  : http://www.spice-space.org/download/releases/spice-0.12.8.tar.bz2
Summary  : SPICE server library
Group    : Development/Tools
License  : LGPL-2.1
Requires: spice-lib
BuildRequires : asciidoc
BuildRequires : glu-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : llvm-dev
BuildRequires : lz4-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : pyparsing
BuildRequires : spice-protocol
BuildRequires : zlib-dev
Patch1: 0001-Call-migrate_end_complete-after-falling-back-to-swit.patch
Patch2: 0002-Prevent-possible-DoS-attempts-during-protocol-handsh.patch
Patch3: 0003-Prevent-integer-overflows-in-capability-checks.patch
Patch4: 0004-main-channel-Prevent-overflow-reading-messages-from-.patch
Patch5: 0005-reds-Check-link-header-magic-without-waiting-for-the.patch
Patch6: 0006-reds-Disconnect-when-receiving-overly-big-ClientMoni.patch
Patch7: 0007-reds-Avoid-integer-overflows-handling-monitor-config.patch
Patch8: 0008-reds-Avoid-buffer-overflows-handling-monitor-configu.patch
Patch9: CVE-2017-7506.nopatch

%description
SPICE: Simple Protocol for Independent Computing Environments
=============================================================

%package dev
Summary: dev components for the spice package.
Group: Development
Requires: spice-lib
Provides: spice-devel

%description dev
dev components for the spice package.


%package lib
Summary: lib components for the spice package.
Group: Libraries

%description lib
lib components for the spice package.


%prep
%setup -q -n spice-0.12.8
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502379078
unset LD_AS_NEEDED
export CC=clang
export CXX=clang++
export LD=ld.gold
unset LDFLAGS
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%configure --disable-static --disable-celt051 --without-sasl --enable-lz4 --enable-opengl=no
make V=1

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1502379078
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/spice-server/spice-audio.h
/usr/include/spice-server/spice-char.h
/usr/include/spice-server/spice-core.h
/usr/include/spice-server/spice-experimental.h
/usr/include/spice-server/spice-input.h
/usr/include/spice-server/spice-migration.h
/usr/include/spice-server/spice-qxl.h
/usr/include/spice-server/spice-server.h
/usr/include/spice-server/spice-version.h
/usr/include/spice-server/spice.h
/usr/lib64/libspice-server.so
/usr/lib64/pkgconfig/spice-server.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libspice-server.so.1
/usr/lib64/libspice-server.so.1.10.1
