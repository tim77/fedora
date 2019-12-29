## Free/Freeworld/Non-Free version
%bcond_without freeworld
%bcond_with nonfree

## Enable LTO
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

%global short_url   https://github.com/libretro

## Assets
%global commit      c2bbf234195bbad91c827337a2fb2b5bc727407b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191031

%global appname retroarch
%global uuid    org.libretro.RetroArch

## Summary suffix
%global sum_suffix %{nil}
%if %{with freeworld}
%global sum_suffix Freeworld version.
%endif

%if %{with nonfree}
%global sum_suffix Non-Free version.
%endif


%if %{with freeworld}
Name:           %{appname}-freeworld
%else
Name:           %{appname}
%endif
Version:        1.8.2
Release:        2%{?dist}
Summary:        Cross-platform, sophisticated frontend for the libretro API. %{sum_suffix}

# CC-BY:        Assets
# CC0:          AppData manifest
#
# Apache License (v2.0)
# ------------------------------------
# deps/SPIRV-Cross/
# retroarch-assets/xmb/flatui/
# deps/glslang/glslang/
# gfx/include/vulkan/
#
# Creative Commons Attribution Public License (v4.0)
# -----------------------------------------------------------------
# retroarch-assets/rgui/wallpaper/
#
# Creative Commons Attribution-NonCommercial Public License (v3.0)
# -------------------------------------------------------------------------------
# retroarch-assets/sounds/
#
# Creative Commons Attribution-ShareAlike Public License (v3.0)
# ----------------------------------------------------------------------------
# retroarch-assets/rgui/wallpaper/
#
# Expat License
# ----------------------------
# libretro-common/glsym/
#
# GNU General Public License (v2)
# ----------------------------------------------
# memory/ngc/ssaram.c
#
# GNU Lesser General Public License
# ------------------------------------------------
# memory/neon/memcpy-neon.S
#
# SIL Open Font License
# ------------------------------------
# retroarch-assets/xmb/automatic/
# retroarch-assets/xmb/neoactive/
# retroarch-assets/xmb/retroactive/
#
# BSD 2-clause "Simplified" License
# ---------------------------------
# cores/
# gfx/
# libretro-common/
#
# BSD 2-clause "Simplified" License GPL (v2 or later)
# ---------------------------------------------------
# gfx/
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# deps/discord-rpc/
# deps/glslang/
# deps/ibxm/
# gfx/
# libretro-common/
#
License:        GPLv3+ and GPLv2 and CC-BY and CC0 and BSD and ASL 2.0 and MIT

URL:            https://www.libretro.com/
Source0:        %{short_url}/RetroArch/archive/v%{version}/%{appname}-%{version}.tar.gz

## Assets
Source1:        %{short_url}/%{appname}-assets/archive/%{commit}/%{appname}-assets-%{date}git%{shortcommit}.tar.gz

## AppData manifest
## * https://github.com/flathub/org.libretro.RetroArch/blob/master/org.libretro.RetroArch.appdata.xml
Source2:        https://raw.githubusercontent.com/flathub/%{uuid}/06be0a83a01514a675f5492db5ceb1f81a9dae68/%{uuid}.appdata.xml

## https://github.com/libretro/retroarch-assets/pull/334
Patch0:         https://github.com/libretro/retroarch-assets/pull/334.patch#/add-executable-bit-to-script.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++ >= 7
BuildRequires:  libappstream-glib
BuildRequires:  libv4l-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  mbedtls-devel
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
## Available in Freeworld repo
BuildRequires:  ffmpeg-devel
%endif
%if %{with nonfree}
## Available in Non-Free repo
BuildRequires:  Cg
BuildRequires:  libCg
BuildRequires:  xv
%endif
Recommends:     %{name}-assets = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     %{name}-filters%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
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
## Non-Free cores
## * Dummy for future
%endif
Provides:       bundled(7zip) = 9.20
Provides:       bundled(discord-rpc)
Provides:       bundled(dr)
Provides:       bundled(glslang)
Provides:       bundled(ibxm)

## https://github.com/libretro/RetroArch/issues/8153
Provides:       bundled(lua) = 5.3.5

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

Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       dejavu-sans-mono-fonts
Recommends:     open-sans-fonts

## Bundled fonts
Provides:       bundled(inter-ui-fonts)
Provides:       bundled(metrophobic-fonts)
Provides:       bundled(sf-atarian-system-fonts)
Provides:       bundled(titilium-web-fonts)

%description    assets
Assets files for %{appname}.


%package        filters
Summary:        Audio and video filters for %{appname}

Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    filters
Audio and video filters for %{appname}.


%prep
%setup -n RetroArch-%{version} -q
%setup -n RetroArch-%{version} -q -D -T -a1
pushd %{appname}-assets-%{commit}
%patch0 -p1
popd

## Unbundling
pushd deps
rm -rf  libfat \
        libFLAC \
        libiosuhax \
        libvita2d \
        libz \
        miniupnpc \
        peglib \
        pthreads \
        wayland-protocols
popd

## * Not part of the 'mbedtls' upstream source
find deps/mbedtls/ ! -name 'cacert.h' -type f -exec rm -f {} +

## Use system assets, libretro cores and audio/video filters
sed -e 's!# libretro_directory =!libretro_directory = %{_libdir}/libretro/!g' \
    -i retroarch.cfg
%if %{with freeworld}
sed -e 's!# assets_directory =!assets_directory = %{_datadir}/libretro/assets-freeworld/!g' \
    -e 's!# video_filter_dir =!video_filter_dir = %{_libdir}/retroarch/filters/video-freeworld/!g' \
    -e 's!# audio_filter_dir =!audio_filter_dir = %{_libdir}/retroarch/filters/audio-freeworld/!g' \
%else
sed -e 's!# assets_directory =!assets_directory = %{_datadir}/libretro/assets/!g' \
    -e 's!# video_filter_dir =!video_filter_dir = %{_libdir}/retroarch/filters/video/!g' \
    -e 's!# audio_filter_dir =!audio_filter_dir = %{_libdir}/retroarch/filters/audio/!g' \
%endif
    -i retroarch.cfg

## Disable online update feature due security reasons
sed -e 's!# menu_show_online_updater = true!menu_show_online_updater = false!g' \
    -e 's!# menu_show_core_updater = true!menu_show_core_updater = false!g' \
    -i retroarch.cfg
sed -e 's!HAVE_UPDATE_ASSETS=yes!HAVE_UPDATE_ASSETS=no!g' -i qb/config.params.sh

## Freeworld config file
%if %{with freeworld}
sed -e 's!GLOBAL_CONFIG_DIR "/retroarch.cfg!GLOBAL_CONFIG_DIR "/%{name}.cfg!g' \
    -i retroarch.c
%endif


%build
./configure \
    --prefix=%{_prefix} \
    --disable-builtinflac \
    --disable-builtinmbedtls \
    --disable-builtinminiupnpc \
    --disable-builtinzlib
%set_build_flags
%make_build

## Assets
%make_build -C %{appname}-assets-%{commit} \
    GIT_VERSION=%{shortcommit}

## Audio filters
%make_build -C libretro-common/audio/dsp_filters

## Video filters
%make_build -C gfx/video_filters


%install
%make_install
rm  %{buildroot}%{_docdir}/%{appname}/COPYING \
    %{buildroot}%{_docdir}/%{appname}/README.md

## Assets
%make_install -C %{appname}-assets-%{commit}
%if %{with freeworld}
mv  %{buildroot}%{_datadir}/libretro/assets/ \
    %{buildroot}%{_datadir}/libretro/assets-freeworld/
%endif

## * Move assets license file in proper location
mkdir -p    %{buildroot}%{_licensedir}/%{name}-assets/
%if %{with freeworld}
mv          %{buildroot}%{_datadir}/libretro/assets-freeworld/COPYING \
%else
mv          %{buildroot}%{_datadir}/libretro/assets/COPYING \
%endif
            %{buildroot}%{_licensedir}/%{name}-assets/COPYING

## * Remove duplicate fonts which available in Fedora repos
%if %{with freeworld}
rm  %{buildroot}%{_datadir}/libretro/assets-freeworld/pkg/osd-font.ttf \
    %{buildroot}%{_datadir}/libretro/assets-freeworld/xmb/flatui/font.ttf
%else
rm  %{buildroot}%{_datadir}/libretro/assets/pkg/osd-font.ttf \
    %{buildroot}%{_datadir}/libretro/assets/xmb/flatui/font.ttf
%endif

## Audio filters
%make_install -C libretro-common/audio/dsp_filters \
    PREFIX=%{_prefix} \
    %if %{with freeworld}
    INSTALLDIR=%{_libdir}/retroarch/filters-freeworld/audio
    %else
    INSTALLDIR=%{_libdir}/retroarch/filters/audio
    %endif

## Video filters
%make_install -C gfx/video_filters \
    PREFIX=%{_prefix} \
    %if %{with freeworld}
    INSTALLDIR=%{_libdir}/retroarch/filters-freeworld/video
    %else
    INSTALLDIR=%{_libdir}/retroarch/filters/video
    %endif

## AppData manifest
install -m 0644 -Dp %{SOURCE2} %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml

## Rename desktop file to UUID for compatibility
mv  %{buildroot}%{_datadir}/applications/%{appname}.desktop \
    %{buildroot}%{_datadir}/applications/%{uuid}.desktop

%if %{with freeworld}
## Rename binary, desktop file, appdata manifest and config file
mv  %{buildroot}%{_bindir}/%{appname} \
    %{buildroot}%{_bindir}/%{appname}-freeworld
mv  %{buildroot}%{_bindir}/%{appname}-cg2glsl \
    %{buildroot}%{_bindir}/%{appname}-cg2glsl-freeworld
mv  %{buildroot}%{_datadir}/applications/%{uuid}.desktop \
    %{buildroot}%{_datadir}/applications/%{uuid}-freeworld.desktop
mv  %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml \
    %{buildroot}%{_metainfodir}/%{uuid}-freeworld.appdata.xml
mv  %{buildroot}%{_sysconfdir}/%{appname}.cfg \
    %{buildroot}%{_sysconfdir}/%{name}.cfg
sed -i 's!Exec=retroarch!Exec=retroarch-freeworld!' \
    %{buildroot}%{_datadir}/applications/%{uuid}-freeworld.desktop
sed -i 's!org.libretro.RetroArch.desktop!org.libretro.RetroArch-freeworld.desktop!' \
    %{buildroot}%{_metainfodir}/%{uuid}-freeworld.appdata.xml
%endif


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml


%files
%license COPYING
%doc README.md README-exynos.md README-OMAP.md README-mali_fbdev_r4p0.md CHANGES.md CONTRIBUTING.md
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.xml
%{_datadir}/pixmaps/*.svg
%{_mandir}/man6/*
%config(noreplace) %{_sysconfdir}/%{name}.cfg

## Freeworld package
%if %{with freeworld}
%{_bindir}/%{appname}-freeworld
%{_bindir}/%{appname}-cg2glsl-freeworld

%files assets
## Incorrect-fsf-address
## * https://github.com/libretro/retroarch-assets/issues/335
%{_datadir}/libretro/assets-freeworld/
%{_licensedir}/%{name}-assets/
%dir %{_datadir}/libretro/

%files filters
%{_libdir}/%{appname}/filters-freeworld/
%dir %{_libdir}/%{appname}
%else
## Free package
%{_bindir}/%{appname}
%{_bindir}/%{appname}-cg2glsl

%files assets
## Incorrect-fsf-address
## * https://github.com/libretro/retroarch-assets/issues/335
%{_datadir}/libretro/assets/
%{_licensedir}/%{appname}-assets/
%dir %{_datadir}/libretro/

%files filters
%{_libdir}/%{appname}/filters/
%dir %{_libdir}/%{appname}
%endif


%changelog
* Sun Dec 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.2-2
- Make fully standlone Freeworld package as RPM Fusion recommended

* Thu Dec 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Fri Nov 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.1-14
- Initial package
- Thanks to Vitaly Zaitsev <vitaly@easycoding.org> for help with packaging and review