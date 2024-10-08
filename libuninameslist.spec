#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v19
# autospec commit: f35655a
#
Name     : libuninameslist
Version  : 20240910
Release  : 15
URL      : https://github.com/fontforge/libuninameslist/archive/20240910/libuninameslist-20240910.tar.gz
Source0  : https://github.com/fontforge/libuninameslist/archive/20240910/libuninameslist-20240910.tar.gz
Summary  : Unicode Names and Annotations List Library (NamesList.txt=@NL_VERSION@)
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libuninameslist-lib = %{version}-%{release}
Requires: libuninameslist-license = %{version}-%{release}
BuildRequires : file
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
LibUniNamesList
***************
LibUniNamesList holds www.unicode.org Nameslist.txt data which can be useful
for programs that need Unicode "Names", "Annotations" and block definitions.

%package dev
Summary: dev components for the libuninameslist package.
Group: Development
Requires: libuninameslist-lib = %{version}-%{release}
Provides: libuninameslist-devel = %{version}-%{release}
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
%setup -q -n libuninameslist-20240910
cd %{_builddir}/libuninameslist-20240910
pushd ..
cp -a libuninameslist-20240910 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726244784
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726244784
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libuninameslist
cp %{_builddir}/libuninameslist-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libuninameslist/e9cf76556aab3f1d3c2a70d8c96bceb4a681ebe3 || :
cp %{_builddir}/libuninameslist-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libuninameslist/4bc2eccad1f1ea956a58362d96c1f0d66c5fca06 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/libuninameslist.so.1.0.15
/usr/lib64/libuninameslist.so.1
/usr/lib64/libuninameslist.so.1.0.15

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libuninameslist/4bc2eccad1f1ea956a58362d96c1f0d66c5fca06
/usr/share/package-licenses/libuninameslist/e9cf76556aab3f1d3c2a70d8c96bceb4a681ebe3
