# Remsnet  Spec file for package tmda
#
# Copyright (c) 1995-2008 Remsnet Netzwerk Service OhG , D-73630 Remshalden
# Copyright (c) 2008-2014 Remsnet Consullting & Internet Services LTD , D-40476 Duesseldorf


# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments https://github.com/remsnet/OpenSuSE-fatresize



Name: fatresize
Version: 1.0.2
Release: 1.3_rcis
License: GPL-3.0
Group: System/Filesystems
Summary: The FAT16/FAT32 non-destructive resizer
URL: http://sourceforge.net/projects/fatresize/
Source: http://fossies.org/linux/privat/fatresize-1.0.3.tar.gz/%name-%version.tar.bz2
Patch0: %name-%version-libparted_ver_check.patch
Patch1: %name-%version-ped_assert.patch
Patch2: %name-%version-ped_free.patch
BuildRequires: gcc autoconf automake bison flex
BuildRequires: buildconf => 9999
BuildRequires: shtool => 2.0.8
BuildRequires: parted-devel >= 2.4
Requires: libparted0 >= 2.4
Requires: shtool => 2.0.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fatresize is a FAT16/FAT32 non-destructive resizer.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build


#/usr/bin/buildconf

autoreconf -fisv
#
# Opensuse Style Build


export CFLAGS="$CFLAGS -I%{_libdir}"
export CXXFLAGS="$CFLAGS -I%{_libdir}"
export CFLAGS="$CFLAGS -fpic -DPIC"
export LIBS="-pie "
%configure \
        --prefix=%{_prefix} \
        --exec-prefix=%{_sbindir} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir}\
        --datadir=%{_libdir}/%{name} \
        --sysconfdir=%{_sysconfdir}/%{name} \
        --localstatedir=%{_localstatedir}/run/%{name} \
        --docdir=%{_docdir}/%{name}                 \
        --libexecdir=%{_prefix}/lib


%{__make}  %{?_smp_mflags} all

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%__mkdir %buildroot
%makeinstall install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_sbindir/%name

%changelog
* Sun Apr  6 2014 support@remsnet.de -r3
- build depends updated for Opensuse 13.1
* Tue Dec 18 2012 Antoine Belvire <antoine.belvire@laposte.net> 1.0.2-1
- Created package via OBS
- Added patch fixing bad libparted version check
- Added patch fixing new parted PED_ASSERT function syntax
ad1:/proj/parted # cat shtool-2.0.8-1.spec

Name: shtool
Version: 2.0.8
Release: 1.3_rcis
#
License: GPL
Group: Development/Tools/Building
#
BuildRoot: %{_tmppath}/%{name}-%{version}-build
#
URL: http://www.ossp.org/pkg/tool/%{name}/
Source: ftp://ftp.ossp.org/pkg/tool/%{name}/%{name}-%{version}.tar.gz
#
Summary: GNU shtool -- The GNU Portable Shell Tool
%description
The GNU shtool program is a compilation of small but very stable and
portable shell scripts into a single shell tool. All ingredients
were in successful use over many years in various free software
projects. The compiled shtool program is intended to be used inside
the source tree of free software packages. There it can take over
various (usually non-portable) tasks related to the building and
installation of such packages.

It currently contains the following tools:
  echo       Print string with optional construct expansion
  mdate      Pretty-print modification time of a file or dir
  table      Pretty print a field-separated list as a table
  prop       Display progress with a running propeller
  move       Move files with simultan substitution
  install    Install a program, script or datafile
  mkdir      Make one or more directories
  mkln       Make link with calculation of relative paths
  mkshadow   Make a shadow tree
  fixperm    Fix file permissions inside a source tree
  rotate     Rotate logfiles
  tarball    Roll distribution tarballs
  subst      Apply sed(1) substitution operations
  platform   Platform identification utility
  arx        Extended archive command
  slo        Separate linker options by library class
  scpp       Sharing C Pre-Processor
  version    Generate and maintain a version information file
  path       Deal with program paths

Authors:
--------
    Ralf S. Engelschall <rse@engelschall.com>

%prep
%setup

%build
%configure
%{__make}
%ifnarch %arm
%{__make} check
%endif

%install
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS RATIONAL README THANKS
%{_bindir}/shtool
%{_bindir}/shtoolize
%{_mandir}/man1/shtool-rotate.1*
%{_mandir}/man1/shtool-tarball.1*
%{_mandir}/man1/shtool-subst.1*
%{_mandir}/man1/shtool-arx.1*
%{_mandir}/man1/shtool-slo.1*
%{_mandir}/man1/shtool-scpp.1*
%{_mandir}/man1/shtool-version.1*
%{_mandir}/man1/shtool-path.1*
%{_mandir}/man1/shtoolize.1*
%{_mandir}/man1/shtool.1*
%{_mandir}/man1/shtool-echo.1*
%{_mandir}/man1/shtool-mdate.1*
%{_mandir}/man1/shtool-table.1*
%{_mandir}/man1/shtool-prop.1*
%{_mandir}/man1/shtool-move.1*
%{_mandir}/man1/shtool-install.1*
%{_mandir}/man1/shtool-mkdir.1*
%{_mandir}/man1/shtool-mkln.1*
%{_mandir}/man1/shtool-mkshadow.1*
%{_mandir}/man1/shtool-fixperm.1*
%{_mandir}/man1/shtool-platform.1*
%{_datadir}/aclocal/shtool.m4
%{_datadir}/shtool/sh.common
%{_datadir}/shtool/sh.echo
%{_datadir}/shtool/sh.mdate
%{_datadir}/shtool/sh.table
%{_datadir}/shtool/sh.prop
%{_datadir}/shtool/sh.move
%{_datadir}/shtool/sh.install
%{_datadir}/shtool/sh.mkdir
%{_datadir}/shtool/sh.mkln
%{_datadir}/shtool/sh.mkshadow
%{_datadir}/shtool/sh.fixperm
%{_datadir}/shtool/sh.rotate
%{_datadir}/shtool/sh.tarball
%{_datadir}/shtool/sh.subst
%{_datadir}/shtool/sh.platform
%{_datadir}/shtool/sh.arx
%{_datadir}/shtool/sh.slo
%{_datadir}/shtool/sh.scpp
%{_datadir}/shtool/sh.version
%{_datadir}/shtool/sh.path

* Sun Apr  6 2014 support@remsnet.de -r3
- build depends updated for Opensuse 13.1
