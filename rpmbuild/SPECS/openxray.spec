# WIP
# Note: requires internet access during build procces because of git submodules

%global commit b8992dfd680f52c7b48b13c07ca0d73cf9377a78
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20210403

# Optimize for build time or performance
%bcond_without release_build

# GCC or Clang compiler
%bcond_with clang

%if %{with release_build}
%else
%global optflags %{optflags} -O0
%endif

%if %{with clang}
%global optflags %(echo %{optflags} | sed -e 's/-mcet//g' -e 's/-fcf-protection//g' -e 's/-fstack-clash-protection//g' -e 's/$/-Qunused-arguments -Wno-unknown-warning-option/')
%endif

%global version_dev 822

%global debug_package %{nil}

Name:       openxray
Version:    0.0.%{version_dev}
Release:    1.%{date}git%{shortcommit}%{?dist}
Summary:    Improved version of the X-Ray Engine – game engine used in S.T.A.L.K.E.R.

# FIXME
License:    CC-BY-SA
URL:    https://github.com/OpenXRay/xray-16
%dnl Source0:   %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source0:    xray-16.tar.xz

BuildRequires: cmake
BuildRequires: cryptopp-devel
BuildRequires: desktop-file-utils
BuildRequires: freeimage-plus-devel
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: glew-devel
BuildRequires: libglvnd-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: liblockfile-devel
BuildRequires: libogg-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: lzo-devel

### Native vs bundled?
BuildRequires: zlib-devel
BuildRequires: luajit-devel
# BuildRequires: ode-devel

BuildRequires: openal-soft-devel
BuildRequires: pcre2-devel
BuildRequires: pcre-devel
BuildRequires: readline-devel
BuildRequires: tbb-devel
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(sdl2)
%if %{with clang}
BuildRequires: clang
BuildRequires: compiler-rt
BuildRequires: llvm
%endif

Requires:   %{name}-data = %{version}-%{release}
Requires:   hicolor-icon-theme
Requires:   liblockfile

Provides:   bundled(libODE)
Provides:   bundled(xrLuajit)

%description
This repository contains X-Ray Engine sources based on version 1.6.02. The
original engine is used in S.T.A.L.K.E.R.: Call of Pripyat game released by
GSC Game World.


%package    data
Summary:    Data files for %{name}
BuildArch:  noarch

Requires:   %{name} = %{version}-%{release}

%description data
Data files for %{name}.


%prep
%dnl %autosetup -n xray-16-%{commit}
%autosetup -n xray-16
%dnl git clone https://github.com/OpenXRay/xray-16 --recursive
%dnl git checkout %{commit}
%dnl cp -ar xray-16/* %{_builddir}/xray-16-%{commit}/

### Unbundling
# rm -rf Externals/ode
# rm -rf Externals/zlib
# rm -rf Externals/LuaJIT

mkdir -p %{_target_platform}

%build
%dnl %set_build_flags
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


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
echo 'If game resources are located in another place:

  xr_3da -fsltx <path/to/>/fsgame.ltx'


%files
%license License.txt
%doc README.md
%{_bindir}/xr_3da
%{_libdir}/*.so
%{_prefix}/lib/mimalloc-1.6/

%files data
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/xr_3da
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/pixmaps/*.png


%changelog
* Sun Apr 04 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.822-1
- build(update): 822

* Thu Oct 24 2019 Artem Polishchuk <ego.cordatus@gmail.com>
- Initial package
