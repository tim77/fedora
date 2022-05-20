# Packaged for Fedora by Artem Polishchuk <ego.cordatus@gmail.com>

Name:           opentyrian
Version:        2.1.20220318
Release:        0.%autorelease
Summary:        An open-source port of the DOS shoot-em-up Tyrian

License:        GPLv2+
URL:            https://github.com/opentyrian/opentyrian
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Tyrian Freeware game assets
Source1:        https://camanis.net/tyrian/tyrian21.zip
# AppData rejected by upstream
# https://github.com/opentyrian/opentyrian/pull/13
Source2:        https://raw.githubusercontent.com/flathub/com.github.%{name}.OpenTyrian/master/%{name}.appdata.xml

# Install all icon sizes
Patch0:         %{url}/commit/74245dbebb8f280f4229c32b65de0854e5f843d2.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(sdl2)

Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme

%global _description %{expand:
OpenTyrian is an open-source port of the DOS game Tyrian.

Tyrian is an arcade-style vertical scrolling shooter.  The story is set in
20,031 where you play as Trent Hawkins, a skilled fighter-pilot employed to
fight MicroSol and save the galaxy.

Tyrian features a story mode, one- and two-player arcade modes, and networked
multiplayer.}

%description %{_description}


# Tyrian Freeware game assets
%package        data
Summary:        Game assets files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data %{_description}

Game assets files for %{name}.


%prep
%autosetup -p1
%setup -DTa 1

# Clean useless Windows files of Tyrian Freeware game assets
pushd tyrian21
rm -rf {*.exe,tyrian.ico,helpme.doc,manual.doc,order.doc,shipedit.doc}
popd


%build
%set_build_flags
%make_build \
    gamesdir=%{_datadir} \
    OPENTYRIAN_VERSION=%{version} \
    prefix=%{_prefix} \


%install
%make_install \
    docdir=%{_docdir}/%{name} \
    gamesdir=%{_datadir} \
    OPENTYRIAN_VERSION=%{version} \
    prefix=%{_prefix} \

# Install Tyrian Freeware game assets
mkdir -p %{buildroot}%{_datadir}/tyrian
cp -a tyrian21/* %{buildroot}%{_datadir}/tyrian/
# Remove and catch license file by RPM macros
rm -f %{buildroot}%{_datadir}/tyrian/license.doc

# Install AppData manifest
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING tyrian21/license.doc
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%dnl %{_datadir}/pixmaps/%{name}.png
%{_mandir}/man6/*.6*
%{_metainfodir}/%{name}.appdata.xml

%files data
%{_datadir}/tyrian/


%changelog
