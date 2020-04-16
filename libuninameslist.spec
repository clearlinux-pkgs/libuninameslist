#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libuninameslist
Version  : 20200413
Release  : 5
URL      : https://github.com/fontforge/libuninameslist/archive/20200413/libuninameslist-20200413.tar.gz
Source0  : https://github.com/fontforge/libuninameslist/archive/20200413/libuninameslist-20200413.tar.gz
Summary  : Large, sparse array mapping each unicode code point to the annotation data for it
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libuninameslist-lib = %{version}-%{release}
Requires: libuninameslist-license = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : sed

%description
libuninameslist – A Library of Unicode names and annotation data
================================================================
[![Build Status](https://travis-ci.org/fontforge/libuninameslist.svg?branch=master)](https://travis-ci.org/fontforge/libuninameslist) [![Build status](https://ci.appveyor.com/api/projects/status/qseac73evm9leu0g?svg=true)](https://ci.appveyor.com/project/fontforge/libuninameslist) [![Coverity Scan Build Status](https://scan.coverity.com/projects/793/badge.svg?flat=1)](https://scan.coverity.com/projects/793)

%package dev
Summary: dev components for the libuninameslist package.
Group: Development
Requires: libuninameslist-lib = %{version}-%{release}
Provides: libuninameslist-devel = %{version}-%{release}
Requires: libuninameslist = %{version}-%{release}
Requires: libuninameslist = %{version}-%{release}

%description dev
dev components for the libuninameslist package.


%package lib
Summary: lib components for the libuninameslist package.
Group: Libraries
Requires: libuninameslist-license = %{version}-%{release}

%description lib
lib components for the libuninameslist package.


%package license
Summary: license components for the libuninameslist package.
Group: Default

%description license
license components for the libuninameslist package.


%prep
%setup -q -n libuninameslist-20200413
cd %{_builddir}/libuninameslist-20200413

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587057070
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1587057070
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libuninameslist
cp %{_builddir}/libuninameslist-20200413/COPYING %{buildroot}/usr/share/package-licenses/libuninameslist/e9cf76556aab3f1d3c2a70d8c96bceb4a681ebe3
cp %{_builddir}/libuninameslist-20200413/LICENSE %{buildroot}/usr/share/package-licenses/libuninameslist/c650f1713067548d62c7ae6f5a48cf02bb8c1bb1
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/uninameslist.h
/usr/lib64/libuninameslist.so
/usr/lib64/pkgconfig/libuninameslist.pc
/usr/share/man/man3/libuninameslist.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libuninameslist.so.1
/usr/lib64/libuninameslist.so.1.0.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libuninameslist/c650f1713067548d62c7ae6f5a48cf02bb8c1bb1
/usr/share/package-licenses/libuninameslist/e9cf76556aab3f1d3c2a70d8c96bceb4a681ebe3
