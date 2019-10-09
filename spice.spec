#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x97D9123DE37A484F (toso@posteo.net)
#
Name     : spice
Version  : 0.14.2
Release  : 28
URL      : https://www.spice-space.org/download/releases/spice-server/spice-0.14.2.tar.bz2
Source0  : https://www.spice-space.org/download/releases/spice-server/spice-0.14.2.tar.bz2
Source1 : https://www.spice-space.org/download/releases/spice-server/spice-0.14.2.tar.bz2.sign
Summary  : SPICE server library
Group    : Development/Tools
License  : LGPL-2.1
Requires: spice-lib = %{version}-%{release}
Requires: spice-license = %{version}-%{release}
Requires: glib-networking
BuildRequires : asciidoc
BuildRequires : buildreq-meson
BuildRequires : gdb
BuildRequires : glib-networking
BuildRequires : glu-dev
BuildRequires : joe
BuildRequires : libjpeg-turbo-dev
BuildRequires : lz4-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(orc-0.4)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : pyparsing
BuildRequires : python3
BuildRequires : six
BuildRequires : spice-protocol
BuildRequires : strace
BuildRequires : valgrind
BuildRequires : zlib-dev

%description
SPICE: Simple Protocol for Independent Computing Environments
=============================================================

%package dev
Summary: dev components for the spice package.
Group: Development
Requires: spice-lib = %{version}-%{release}
Provides: spice-devel = %{version}-%{release}
Requires: spice = %{version}-%{release}

%description dev
dev components for the spice package.


%package lib
Summary: lib components for the spice package.
Group: Libraries
Requires: spice-license = %{version}-%{release}

%description lib
lib components for the spice package.


%package license
Summary: license components for the spice package.
Group: Default

%description license
license components for the spice package.


%prep
%setup -q -n spice-0.14.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570656101
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-celt051 --without-sasl --enable-lz4 --enable-opengl=no  --disable-opus
make

%install
export SOURCE_DATE_EPOCH=1570656101
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spice
cp COPYING %{buildroot}/usr/share/package-licenses/spice/COPYING
cp subprojects/spice-common/COPYING %{buildroot}/usr/share/package-licenses/spice/subprojects_spice-common_COPYING
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
/usr/lib64/libspice-server.so.1.13.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spice/COPYING
/usr/share/package-licenses/spice/subprojects_spice-common_COPYING
