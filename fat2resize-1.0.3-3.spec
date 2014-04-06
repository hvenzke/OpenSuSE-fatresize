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
