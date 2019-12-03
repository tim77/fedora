### Free/Non-free version
%bcond_without freeworld
%bcond_with nonfree

### Enable LTO
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

%global short_url   https://github.com/libretro

### Assets
%global commit      c2bbf234195bbad91c827337a2fb2b5bc727407b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191031

%global appname retroarch
%global uuid    org.libretro.RetroArch

%if %{with freeworld}
Name:           %{appname}-freeworld
%else
Name:           %{appname}
%endif
Version:        1.8.1
Release:        11%{?dist}
%if %{with freeworld}
Summary:        Cross-platform, sophisticated frontend for the libretro API. Non-free version.
%else
Summary:        Cross-platform, sophisticated frontend for the libretro API
%endif

### CC-BY:      Assets
### CC0:        AppData manifest
### 
### Apache License (v2.0)
### ------------------------------------
### deps/SPIRV-Cross/
### retroarch-assets/xmb/flatui/
### deps/glslang/glslang/
### deps/mbedtls/
### gfx/include/vulkan/
### 
### Creative Commons Attribution Public License (v4.0)
### -----------------------------------------------------------------
### retroarch-assets/rgui/wallpaper/
### 
### Creative Commons Attribution-NonCommercial Public License (v3.0)
### -------------------------------------------------------------------------------
### retroarch-assets/sounds/
### 
### Creative Commons Attribution-ShareAlike Public License (v3.0)
### ----------------------------------------------------------------------------
### retroarch-assets/rgui/wallpaper/
### 
### Expat License
### ----------------------------
### libretro-common/glsym/
### 
### GNU General Public License (v2)
### ----------------------------------------------
### memory/ngc/ssaram.c
### 
### GNU Lesser General Public License
### ------------------------------------------------
### memory/neon/memcpy-neon.S
### 
### Public domain
### ----------------------------
### deps/libFLAC/
### 
### SIL Open Font License
### ------------------------------------
### retroarch-assets/xmb/automatic/
### retroarch-assets/xmb/neoactive/
### retroarch-assets/xmb/retroactive/
### 
### BSD 2-clause "Simplified" License
### ---------------------------------
### RetroArch-1.8.1/cores/
### RetroArch-1.8.1/gfx/
### RetroArch-1.8.1/libretro-common/
### 
### BSD 2-clause "Simplified" License GPL (v2 or later)
### ---------------------------------------------------
### RetroArch-1.8.1/gfx/
### 
### BSD 3-clause "New" or "Revised" License
### ---------------------------------------
### RetroArch-1.8.1/deps/discord-rpc/
### RetroArch-1.8.1/deps/glslang/
### RetroArch-1.8.1/deps/ibxm/
### RetroArch-1.8.1/deps/libFLAC/
### RetroArch-1.8.1/deps/miniupnpc/
### RetroArch-1.8.1/gfx/
### RetroArch-1.8.1/libretro-common/
###
License:        GPLv3+ and GPLv2 CC-BY and CC0 and BSD and Public Domain and ASL 2.0 and MIT

URL:            https://www.libretro.com/
Source0:        %{short_url}/RetroArch/archive/v%{version}/%{appname}-%{version}.tar.gz

### Assets
Source1:        %{short_url}/%{appname}-assets/archive/%{commit}/%{appname}-assets-%{version}.%{date}git%{shortcommit}.tar.gz

### AppData manifest
### https://github.com/flathub/org.libretro.RetroArch/blob/master/org.libretro.RetroArch.appdata.xml
Source2:        https://raw.githubusercontent.com/flathub/%{uuid}/06be0a83a01514a675f5492db5ceb1f81a9dae68/%{uuid}.appdata.xml

### https://github.com/libretro/retroarch-assets/pull/334
Patch0:         https://github.com/libretro/retroarch-assets/pull/334.patch#/add-executable-bit-to-script.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ >= 7
BuildRequires:  libappstream-glib
BuildRequires:  libv4l-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  perl-Net-DBus
BuildRequires:  perl-X11-Protocol
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)
%if %{with freeworld}
### Available in Freeworld repo
BuildRequires:  ffmpeg-devel
%endif
%if %{with nonfree}
### Available in Nonfree repo
BuildRequires:  Cg
BuildRequires:  libCg
BuildRequires:  xv
%endif
%if %{with freeworld}
Requires:       %{appname}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Recommends:     %{appname}-assets = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     %{appname}-filters%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     libretro-beetle-ngp%{?_isa}
Recommends:     libretro-beetle-pce-fast%{?_isa}
Recommends:     libretro-beetle-vb%{?_isa}
Recommends:     libretro-beetle-wswan%{?_isa}
Recommends:     libretro-bsnes-mercury%{?_isa}
Recommends:     libretro-desmume2015%{?_isa}
Recommends:     libretro-gambatte%{?_isa}
Recommends:     libretro-handy%{?_isa}
Recommends:     libretro-mgba%{?_isa}
Recommends:     libretro-nestopia%{?_isa}
Recommends:     libretro-pcsx-rearmed%{?_isa}
Recommends:     libretro-prosystem%{?_isa}
Recommends:     libretro-stella2014%{?_isa}
%if %{with freeworld}
### Non-free cores
## Dummy for future
%endif
Provides:       bundled(7zip) = 9.20
Provides:       bundled(discord-rpc)
Provides:       bundled(dr)
Provides:       bundled(glslang)
Provides:       bundled(ibxm)
Provides:       bundled(libFLAC) = 1.3.2
Provides:       bundled(libz)

### https://github.com/libretro/RetroArch/issues/8153
Provides:       bundled(lua) = 5.3.5

Provides:       bundled(mbedtls)
Provides:       bundled(miniupnpc) = 2.0
Provides:       bundled(rcheevos) = 7.0.2
Provides:       bundled(SPIRV-Cross)
Provides:       bundled(stb)

%global _description %{expand:
libretro is an API that exposes generic audio/video/input callbacks. A frontend
for libretro (such as RetroArch) handles video output, audio output, input and
application lifecycle. A libretro core written in portable C or C++ can run
seamlessly on many platforms with very little to no porting effort.

While RetroArch is the reference frontend for libretro, several other projects
have used the libretro interface to include support for emulators and/or game
engines. libretro is completely open and free for anyone to use.}

%description %{_description}


%package        assets
Summary:        Assets files for %{appname}
BuildArch:      noarch

Requires:       %{appname} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       dejavu-sans-mono-fonts
Recommends:     open-sans-fonts

### Bundled fonts
Provides:       bundled(inter-ui-fonts)
Provides:       bundled(metrophobic-fonts)
Provides:       bundled(sf-atarian-system-fonts)
Provides:       bundled(titilium-web-fonts)

%description    assets
Assets files for %{appname}.


%package        filters
Summary:        Audio and video filters for %{appname}

Requires:       %{appname}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    filters
Audio and video filters for %{appname}.


%prep
%setup -n RetroArch-%{version} -q
%setup -n RetroArch-%{version} -q -D -T -a1
pushd %{appname}-assets-%{commit}
%patch0 -p1
popd

### Unbundling
pushd deps
rm -rf  libfat \
        libiosuhax \
        libvita2d \
        peglib \
        pthreads \
        wayland-protocols
popd

### Use system assets, libretro cores and audio/video filters
sed -e 's!# assets_directory =!assets_directory = %{_datadir}/libretro/assets/!g' \
    -e 's!# libretro_directory =!libretro_directory = %{_libdir}/libretro/!g' \
    -e 's!# video_filter_dir =!video_filter_dir = %{_libdir}/retroarch/filters/video/!g' \
    -e 's!# audio_filter_dir =!audio_filter_dir = %{_libdir}/retroarch/filters/audio/!g' \
    -i retroarch.cfg

### Disable online update feature due security reasons
sed -e 's!# menu_show_online_updater = true!menu_show_online_updater = false!g' \
    -e 's!# menu_show_core_updater = true!menu_show_core_updater = false!g' \
    -i retroarch.cfg
sed -e 's!HAVE_UPDATE_ASSETS=yes!HAVE_UPDATE_ASSETS=no!g' -i qb/config.params.sh


%build
./configure --prefix=%{_prefix}
%set_build_flags
%make_build

### Assets
%make_build -C %{appname}-assets-%{commit} \
    GIT_VERSION=%{shortcommit}

### Audio filters
%make_build -C libretro-common/audio/dsp_filters

### Video filters
%make_build -C gfx/video_filters


%install
%make_install
rm %{buildroot}%{_docdir}/%{appname}/COPYING
rm %{buildroot}%{_docdir}/%{appname}/README.md

### Assets
%make_install -C %{appname}-assets-%{commit}

## Move assets license file in proper location
mkdir -p    %{buildroot}%{_licensedir}/%{appname}-assets/
mv          %{buildroot}%{_datadir}/libretro/assets/COPYING %{buildroot}/%{_licensedir}/%{appname}-assets/COPYING

## Remove duplicate fonts which available in Fedora repos
rm %{buildroot}%{_datadir}/libretro/assets/pkg/osd-font.ttf
rm %{buildroot}%{_datadir}/libretro/assets/xmb/flatui/font.ttf

### Audio filters
%make_install -C libretro-common/audio/dsp_filters \
    PREFIX=%{_prefix} \
    INSTALLDIR=%{_libdir}/retroarch/filters/audio

### Video filters
%make_install -C gfx/video_filters \
    PREFIX=%{_prefix} \
    INSTALLDIR=%{_libdir}/retroarch/filters/video

### AppData manifest
install -m 0644 -Dp %{SOURCE2} %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml

### Rename desktop file to UUID for compatibility
mv %{buildroot}%{_datadir}/applications/%{appname}.desktop %{buildroot}%{_datadir}/applications/%{uuid}.desktop 

%if %{with freeworld}
### Rename binary, desktop file and appdata manifest
mv %{buildroot}%{_bindir}/%{appname}                    %{buildroot}%{_bindir}/%{appname}-freeworld
mv %{buildroot}%{_datadir}/applications/%{uuid}.desktop %{buildroot}%{_datadir}/applications/%{uuid}-freeworld.desktop
mv %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml      %{buildroot}%{_metainfodir}/%{uuid}-freeworld.appdata.xml
sed  -i 's!Exec=retroarch!Exec=retroarch-freeworld!'    %{buildroot}%{_datadir}/applications/%{uuid}-freeworld.desktop
sed  -i 's!org.libretro.RetroArch.desktop!org.libretro.RetroArch-freeworld.desktop!' %{buildroot}%{_metainfodir}/%{uuid}-freeworld.appdata.xml
%endif


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml


%files
%license COPYING
%doc README.md README-exynos.md README-OMAP.md README-mali_fbdev_r4p0.md CHANGES.md CONTRIBUTING.md
%if %{with freeworld}
%{_bindir}/%{appname}-freeworld
%exclude %{_bindir}/%{appname}-cg2glsl
%exclude %{_datadir}/libretro/
%exclude %{_datadir}/pixmaps/
%exclude %{_libdir}
%exclude %{_licensedir}/%{appname}-assets/COPYING
%exclude %{_mandir}
%exclude %{_sysconfdir}
%else
%{_bindir}/%{appname}
%{_bindir}/%{appname}-cg2glsl
%{_datadir}/pixmaps/*.svg
%{_mandir}/man6/*
%config(noreplace) %{_sysconfdir}/%{appname}.cfg

%files assets
### Incorrect-fsf-address
### https://github.com/libretro/retroarch-assets/issues/335
%{_datadir}/libretro/
%{_licensedir}/%{appname}-assets/

%files filters
%{_libdir}/%{appname}/
%endif
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.xml


%changelog
* Fri Nov 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.1-11
- Initial package
- Thanks to Vitaly Zaitsev <vitaly@easycoding.org> for help with packaging and review