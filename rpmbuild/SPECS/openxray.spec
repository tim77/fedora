### Very WIP, expect hilarious crap in packaging ###
# Note: requires internet access during build procces because of git submodules

# Optimize for build time or performance
%bcond_without release_build

# GCC or Clang compiler
%bcond_with clang

%if %{with release_build}
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto
%else
%global optflags        %{optflags} -O0
%endif

%if %{with clang}
%global optflags %(echo %{optflags} | sed -e 's/-mcet//g' -e 's/-fcf-protection//g' -e 's/-fstack-clash-protection//g' -e 's/$/-Qunused-arguments -Wno-unknown-warning-option/')
%endif

%global version_dev 558

%global debug_package %{nil}

Name:           openxray
Version:        0.0.%{version_dev}
Release:        1.master%{?dist}
Summary:        Improved version of the X-Ray Engine – game engine used in S.T.A.L.K.E.R.

# FIXME
License:        CC-BY-SA
URL:            https://github.com/OpenXRay/xray-16
Source0:        %{url}/archive/%{version_dev}/%{name}-%{version}.tar.gz
#Source1:        filter-requires.sh

BuildRequires:  cmake
BuildRequires:  cryptopp-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freeimage-plus-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glew-devel
#BuildRequires:  intltool
#BuildRequires:  libappstream-glib
BuildRequires:  libglvnd-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  liblockfile-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  lzo-devel

# Native vs bundled?
BuildRequires:  zlib-devel
#BuildRequires:  luajit-devel
#BuildRequires:  ode-devel

BuildRequires:  openal-soft-devel
BuildRequires:  pcre2-devel
BuildRequires:  pcre-devel
BuildRequires:  readline-devel
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sdl2)
%if %{with clang}
BuildRequires:  clang
BuildRequires:  compiler-rt
BuildRequires:  llvm
%endif
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}
Provides:       bundled(libODE)
Provides:       bundled(xrLuajit)

%description
This repository contains X-Ray Engine sources based on version 1.6.02. The
original engine is used in S.T.A.L.K.E.R.: Call of Pripyat game released by
GSC Game World.


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data
Data files for %{name}.


%prep
%autosetup -n xray-16-%{version_dev}
git clone --depth=1 https://github.com/OpenXRay/xray-16 --recursive
cp -ar xray-16/* %{_builddir}/xray-16-%{version_dev}/

## Unbundling
#rm -rf Externals/ode
rm -rf Externals/zlib
#rm -rf Externals/LuaJIT

mkdir -p %{_target_platform}

%build
#%%set_build_flags
pushd %{_target_platform}

# cmake macros result failed build, so use with default upstream flags
cmake \
    %if %{with clang}
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_AR=%{_bindir}/llvm-ar \
    -DCMAKE_RANLIB=%{_bindir}/llvm-ranlib \
    -DCMAKE_LINKER=%{_bindir}/llvm-ld \
    -DCMAKE_OBJDUMP=%{_bindir}/llvm-objdump \
    -DCMAKE_NM=%{_bindir}/llvm-nm \
    %endif
    ..
%make_build
popd


%install
pushd %{_target_platform}
%make_install
popd

# Move binary file in proper location
mkdir -p    %{buildroot}%{_bindir}
mv          %{buildroot}%{_prefix}/games/xr_3da %{buildroot}%{_bindir}/

# Move libs in proper location
mkdir -p    %{buildroot}%{_libdir}
mv          %{buildroot}%{_prefix}/lib/*        %{buildroot}%{_libdir}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license License.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/xr_3da
%{_libdir}/*.so

%files data
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*.png


%changelog
* Thu Oct 24 2019 Artem Polishchuk <ego.cordatus@gmail.com>
- Initial package
