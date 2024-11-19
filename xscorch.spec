#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: 542402611043
#
# Source0 file verified with key 0x5C9DB08058235D71 (jacob@gnifty.net)
#
Name     : xscorch
Version  : 0.2.1
Release  : 3
URL      : http://www.xscorch.org/releases/xscorch-0.2.1.tar.gz
Source0  : http://www.xscorch.org/releases/xscorch-0.2.1.tar.gz
Source1  : http://www.xscorch.org/releases/xscorch-0.2.1.tar.gz.asc
Source2  : 5C9DB08058235D71.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xscorch-bin = %{version}-%{release}
Requires: xscorch-data = %{version}-%{release}
Requires: xscorch-license = %{version}-%{release}
Requires: xscorch-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gnupg
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libmikmod)
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: fedora-xscorch-0.2.1-memcpy.patch
Patch2: fedora-xscorch-0.2.1-missing-proto.patch

%description
xscorch  -  A Scorched Earth clone
Code copyright(c) 2000-2004 Justin David Smith
Code copyright(c) 2000-2011 Jacob Luna Lundberg

%package bin
Summary: bin components for the xscorch package.
Group: Binaries
Requires: xscorch-data = %{version}-%{release}
Requires: xscorch-license = %{version}-%{release}

%description bin
bin components for the xscorch package.


%package data
Summary: data components for the xscorch package.
Group: Data

%description data
data components for the xscorch package.


%package extras
Summary: extras components for the xscorch package.
Group: Default

%description extras
extras components for the xscorch package.


%package license
Summary: license components for the xscorch package.
Group: Default

%description license
license components for the xscorch package.


%package man
Summary: man components for the xscorch package.
Group: Default

%description man
man components for the xscorch package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 5C9DB08058235D71' gpg.status
%setup -q -n xscorch-0.2.1
cd %{_builddir}/xscorch-0.2.1
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732038447
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
%configure --disable-static
make  %{?_smp_mflags}  LDFLAGS+="-Wl,-z,muldefs"

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

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
export SOURCE_DATE_EPOCH=1732038447
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xscorch
cp %{_builddir}/xscorch-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xscorch/b47456e2c1f38c40346ff00db976a2badf36b5e3 || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/xscorch/images
install -p -m 644 img/xscorch-logo.xpm %{buildroot}/usr/share/xscorch/images/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xscorch

%files data
%defattr(-,root,root,-)
/usr/share/xscorch/accessories.def
/usr/share/xscorch/copying.txt
/usr/share/xscorch/images/xscorch-icon.xpm
/usr/share/xscorch/images/xscorch-logo.xpm
/usr/share/xscorch/profiles.def
/usr/share/xscorch/scorings.def
/usr/share/xscorch/sounds/README
/usr/share/xscorch/weapons.def
/usr/share/xscorch/xscorch.txt

%files extras
%defattr(-,root,root,-)
/usr/bin/xscorch-server

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xscorch/b47456e2c1f38c40346ff00db976a2badf36b5e3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man6/xscorch.6
