# Inline assembler
%global debug_package %{nil}

Name:           zerotier-one
Version:        1.4.6
Release:        3%{?dist}
Summary:        Smart Ethernet Switch for Earth

# Boost:        README.md
#
# ASL:          controller/
#               debian/copyright
#               include/
#               node/
#               one.cpp
#               osdep/
#               rule-compiler/
#               selftest.cpp
#               service/
#               version.h
#
# ASL 2.0:      LICENSE.txt
#
# BSD:          ext/libnatpmp/
#               ext/miniupnpc/
#
# Boost:        COPYING
#
# MIT           ext/cpp-httplib/
#               ext/http-parser/
#               ext/json/LICENSE.MIT
#               ext/librabbitmq/
#
# GPLv3+:       attic/
#               ext/libnatpmp/
#               java/

License:        BSL and Boost and ASL and ASL 2.0 and MIT
URL:            https://zerotier.com
Source0:        https://github.com/zerotier/ZeroTierOne/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  go-md2man
BuildRequires:  http-parser-devel
BuildRequires:  json-devel
BuildRequires:  libnatpmp-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(sqlite3)
%if 0%{?fedora} > 30
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif
%{?systemd_requires}
Provides:       bundled(http-parser)
Provides:       bundled(json) = 3.2.0
Provides:       bundled(salsa2012)

%description
ZeroTier is a smart programmable Ethernet switch for planet Earth. It allows all
networked devices, VMs, containers, and applications to communicate as if they
all reside in the same physical data center or cloud region.

This is accomplished by combining a cryptographically addressed and secure peer
to peer network (termed VL1) with an Ethernet emulation layer somewhat similar
to VXLAN (termed VL2). Our VL2 Ethernet virtualization layer includes advanced
enterprise SDN features like fine grained access control rules for network
micro-segmentation and security monitoring.

All ZeroTier traffic is encrypted end-to-end using secret keys that only you
control. Most traffic flows peer to peer, though we offer free (but slow)
relaying for users who cannot establish peer to peer connections.

The goals and design principles of ZeroTier are inspired by among other things
the original Google BeyondCorp paper and the Jericho Forum with its notion of
"deperimeterization."


%prep
%autosetup -n ZeroTierOne-%{version}

### Unbundling (maybe for future, depends on upstream)
# rm -rf ext/http-parser
# rm -rf ext/json


%build
%set_build_flags
%make_build


%install
%make_install
install -m 0644 -Dp debian/%{name}.service %{buildroot}%{_unitdir}/%{name}.service


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license COPYING
%doc AUTHORS.md README.md RELEASE-NOTES.md OFFICIAL-RELEASE-STEPS.md
%{_mandir}/man*/*
%{_sbindir}/zerotier-*
%{_sharedstatedir}/%{name}/
%{_unitdir}/*.service


%changelog
* Sun Nov 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.6-3
- Update to 1.4.6

* Thu Apr 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.12-2
- Update to 1.2.12
- .spec file "fixes" :)

* Sat Mar 18 2017 François Kooman <fkooman@tuxed.net> - 1.2.2-1
- update to 1.2.2

* Mon Jul 25 2016 François Kooman <fkooman@tuxed.net> - 1.1.14-1
- update to 1.1.14

* Tue Jul 19 2016 François Kooman <fkooman@tuxed.net> - 1.1.12-2
- allow override of LDFLAGS by rpmbuild

* Wed Jul 13 2016 François Kooman <fkooman@tuxed.net> - 1.1.12-1
- update to 1.1.12
- remove fix for selftest when controller is enabled

* Mon Jul 04 2016 François Kooman <fkooman@tuxed.net> - 1.1.6-2
- use go-md2man to generate the manpages

* Mon Jul 04 2016 François Kooman <fkooman@tuxed.net> - 1.1.6-1
- initial package
