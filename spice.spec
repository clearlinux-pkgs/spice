#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spice
Version  : 0.14.0
Release  : 22
URL      : http://www.spice-space.org/download/releases/spice-0.14.0.tar.bz2
Source0  : http://www.spice-space.org/download/releases/spice-0.14.0.tar.bz2
Summary  : SPICE server library
Group    : Development/Tools
License  : LGPL-2.1
Requires: spice-lib
Requires: spice-license
BuildRequires : asciidoc
BuildRequires : glu-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : lz4-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(orc-0.4)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : pyparsing
BuildRequires : python
BuildRequires : six
BuildRequires : spice-protocol
BuildRequires : valgrind
BuildRequires : zlib-dev
Patch1: CVE-2018-10873.patch

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
Requires: spice-license

%description lib
lib components for the spice package.


%package license
Summary: license components for the spice package.
Group: Default

%description license
license components for the spice package.


%prep
%setup -q -n spice-0.14.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536005563
unset LD_AS_NEEDED
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-celt051 --without-sasl --enable-lz4 --enable-opengl=no
make

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1536005563
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/spice
cp COPYING %{buildroot}/usr/share/doc/spice/COPYING
cp spice-common/COPYING %{buildroot}/usr/share/doc/spice/spice-common_COPYING
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
/usr/include/spice-server/spice-replay.h
/usr/include/spice-server/spice-server.h
/usr/include/spice-server/spice-version.h
/usr/include/spice-server/spice.h
/usr/lib64/libspice-server.so
/usr/lib64/pkgconfig/spice-server.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libspice-server.so.1
/usr/lib64/libspice-server.so.1.12.4

%files license
%defattr(-,root,root,-)
/usr/share/doc/spice/COPYING
/usr/share/doc/spice/spice-common_COPYING
