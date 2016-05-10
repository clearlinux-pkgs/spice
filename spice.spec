#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spice
Version  : 0.13.1
Release  : 7
URL      : http://www.spice-space.org/download/releases/spice-0.13.1.tar.bz2
Source0  : http://www.spice-space.org/download/releases/spice-0.13.1.tar.bz2
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
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : pyparsing
BuildRequires : spice-protocol
BuildRequires : zlib-dev

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
%setup -q -n spice-0.13.1

%build
unset LD_AS_NEEDED
export CC=clang
export CXX=clang++
export LD=ld.gold
export CFLAGS="-g -O3 -feliminate-unused-debug-types  -pipe -Wall -D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wl,--copy-dt-needed-entries -m64 -march=westmere  -mtune=native -fasynchronous-unwind-tables -D_REENTRANT  -Wl,-z -Wl,now -Wl,-z -Wl,relro "
export CXXFLAGS=$CFLAGS
unset LDFLAGS
%configure --disable-static --disable-celt051 --without-sasl --enable-lz4 --enable-opengl
make V=1

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 check

%install
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
