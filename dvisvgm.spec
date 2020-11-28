#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dvisvgm
Version  : 2.11
Release  : 8
URL      : https://github.com/mgieseki/dvisvgm/releases/download/2.11/dvisvgm-2.11.tar.gz
Source0  : https://github.com/mgieseki/dvisvgm/releases/download/2.11/dvisvgm-2.11.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 GPL-3.0 MIT
Requires: dvisvgm-bin = %{version}-%{release}
Requires: dvisvgm-license = %{version}-%{release}
Requires: dvisvgm-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : ghostscript-dev
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(libbrotlienc)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libwoff2enc)
BuildRequires : potrace-dev
BuildRequires : texlive
BuildRequires : texlive-dev
BuildRequires : xmlto

%description
dvisvgm -- A DVI to SVG converter
DESCRIPTION
dvisvgm is a utility for TeX/LaTeX users. It converts DVI, EPS, and
PDF files to the XML-based scalable vector graphics format SVG.

%package bin
Summary: bin components for the dvisvgm package.
Group: Binaries
Requires: dvisvgm-license = %{version}-%{release}

%description bin
bin components for the dvisvgm package.


%package license
Summary: license components for the dvisvgm package.
Group: Default

%description license
license components for the dvisvgm package.


%package man
Summary: man components for the dvisvgm package.
Group: Default

%description man
man components for the dvisvgm package.


%prep
%setup -q -n dvisvgm-2.11
cd %{_builddir}/dvisvgm-2.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606584016
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || true

%install
export SOURCE_DATE_EPOCH=1606584016
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dvisvgm
cp %{_builddir}/dvisvgm-2.11/COPYING %{buildroot}/usr/share/package-licenses/dvisvgm/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/dvisvgm-2.11/libs/brotli/LICENSE %{buildroot}/usr/share/package-licenses/dvisvgm/c045813a6c514f2d30d60a07c6aaf3603850e608
cp %{_builddir}/dvisvgm-2.11/libs/clipper/License.txt %{buildroot}/usr/share/package-licenses/dvisvgm/262180609d130913cbf4aacd89de9e3281fab846
cp %{_builddir}/dvisvgm-2.11/libs/ff-woff/LICENSE %{buildroot}/usr/share/package-licenses/dvisvgm/f13242fd2b6974c2940761a97937b4918c5fa4e6
cp %{_builddir}/dvisvgm-2.11/libs/variant/LICENSE.md %{buildroot}/usr/share/package-licenses/dvisvgm/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
cp %{_builddir}/dvisvgm-2.11/libs/woff2/LICENSE %{buildroot}/usr/share/package-licenses/dvisvgm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/dvisvgm-2.11/tests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/dvisvgm/5a2314153eadadc69258a9429104cd11804ea304
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dvisvgm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dvisvgm/262180609d130913cbf4aacd89de9e3281fab846
/usr/share/package-licenses/dvisvgm/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/dvisvgm/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/dvisvgm/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/dvisvgm/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/dvisvgm/c045813a6c514f2d30d60a07c6aaf3603850e608
/usr/share/package-licenses/dvisvgm/f13242fd2b6974c2940761a97937b4918c5fa4e6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dvisvgm.1
