#
# spec file for package parted
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           parted
Version:        3.1
Release:        5.1
Summary:        GNU partitioner
License:        GPL-3.0+
Group:          System/Filesystems
Url:            http://www.gnu.org/software/parted/
Source0:        ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/gnu/parted/%{name}-%{version}.tar.xz.sig
Source2:        parted.keyring
Source3:        baselibs.conf
Source4:        fatresize-0.1.tar.bz2
# Build patches
Patch1:         parted-2.4-ncursesw6.patch

# Other patches
Patch10:        hfs_fix.dif
Patch11:        parted-wipeaix.patch
Patch12:        fix-error-informing-the-kernel.patch
#PATCH-FEATURE-SUSE fix-dm-partition-name.patch bnc471440,447591 petr.uzel@suse.cz
Patch13:        fix-dm-partition-name.patch
Patch14:        parted-fix-cciss-partition-naming.patch
Patch15:        libparted-fix-mmcblk-partition-name.patch
#PATCH-FEATURE-SUSE do-not-create-dm-nodes.patch bnc#501773 petr.uzel@suse.cz
Patch16:        do-not-create-dm-nodes.patch
#PATCH-FEATURE-SUSE more-reliable-informing-the-kernel.patch bnc#657360 petr.uzel@suse.cz
Patch17:        more-reliable-informing-the-kernel.patch
#PATCH-FEATURE-SUSE revert-gpt-add-commands-to-manipulate-pMBR-boot-flag.patch
# (clashes with our hybrid pMBR patches)
Patch18:        revert-gpt-add-commands-to-manipulate-pMBR-boot-flag.patch
Patch19:        parted-gpt-mbr-sync.patch
Patch20:        libparted-ppc-prepboot-in-syncmbr.patch
Patch21:        parted-workaround-windows7-gpt-implementation.patch
Patch22:        dummy-bootcode-only-for-x86.patch
Patch23:        parted-type.patch
Patch24:        parted-mac.patch
Patch25:        parted-Add-Intel-Rapid-Start-Technology-partition.patch
Patch26:        parted-btrfs-support.patch
Patch27:        parted-GPT-add-support-for-PReP-GUID.patch
Patch28:        parted-resize-command.patch
Patch29:        libparted-dasd-do-not-use-first-tracks.patch
Patch30:        libparted-initialize-dasd-part-type.patch
Patch31:        libparted-use-BLKRRPART-for-DASD.patch.patch
Patch100:       parted-fatresize-autoconf.patch
Requires:       /sbin/udevadm
BuildRequires:  check-devel
BuildRequires:  device-mapper-devel >= 1.02.33
BuildRequires:  e2fsprogs-devel
BuildRequires:  libblkid-devel >= 2.17
BuildRequires:  libreiserfs-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  makeinfo
BuildRequires:  pkg-config
BuildRequires:  readline-devel
%if %suse_version >= 1230
BuildRequires:  gpg-offline
%endif
PreReq:         %install_info_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# bug437293
%ifarch ppc64
Obsoletes:      parted-64bit
%endif

%description
GNU Parted is a program for creating, destroying, resizing, checking,
and copying partitions, and the file systems on them.

%package -n libparted0
Summary:        Library for manipulating partitions
Group:          System/Filesystems

%description -n libparted0
Libparted is a library for creating, destroying, resizing, checking
and copying partitions and the file systems on them.

%package devel
Summary:        Parted Include Files and Libraries necessary for Development
Group:          Development/Libraries/C and C++
Requires:       device-mapper-devel >= 1.02.33
Requires:       e2fsprogs-devel
Requires:       libparted0 = %version
Requires:       libreiserfs-devel
# bug437293
%ifarch ppc64
Obsoletes:      parted-devel-64bit
%endif

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package
%prep
%{?gpg_verify: %gpg_verify %{S:1}}
%setup -a 4
%patch1 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch100 -p1

%build
export CFLAGS="%{optflags} `ncursesw6-config --cflags`"
export LDFLAGS="`ncursesw6-config --libs`"
AUTOPOINT=true autoreconf --force --install
%configure      --disable-static                \
                --with-pic                      \
                --enable-device-mapper=yes      \
                --enable-dynamic-loading=no     \
                --enable-selinux                \
                --disable-Werror                \
                --disable-silent-rules
make %{?_smp_mflags}

%install
%makeinstall
rm %{buildroot}%{_libdir}/*.la
%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n libparted0
/sbin/ldconfig

%postun -n libparted0
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO
%{_sbindir}/*
%{_mandir}/man8/part*.8.gz
%doc %{_infodir}/*.info*

%files devel
%defattr(-,root,root)
%doc doc/API doc/FAT
%{_includedir}/*
%{_libdir}/pkgconfig/libparted.pc
%{_libdir}/*.so

%files -n libparted0
%defattr(-,root,root)
%{_libdir}/*.so.*

%files lang -f %{name}.lang

%changelog
* Mon Feb 17 2014 puzel@suse.com
- Fixup last commit - call BLKRRPART only for DASDs
- added patches:
  * libparted-use-BLKRRPART-for-DASD.patch.patch
- removed patches:
  * revert-libparted-remove-now-worse-than-useless-_kern.patch
  * revert-linux-remove-DASD-restriction-on-_disk_sync_p.patch
* Fri Feb 14 2014 puzel@suse.com
- Use BLKRRPART on DASD disks (instead of BLKPG_*) (bnc#862139)
- added patches:
  * revert-libparted-remove-now-worse-than-useless-_kern.patch
  * revert-linux-remove-DASD-restriction-on-_disk_sync_p.patch
* Thu Feb 13 2014 puzel@suse.com
- reserve first 2 tracks on DASD disks for metadata (bnc#862138)
  * add: libparted-dasd-do-not-use-first-tracks.patch
- initialize memory for newly allocated partition (bnc#862138)
  * add: libparted-initialize-dasd-part-type.patch
* Fri Jan 24 2014 puzel@suse.com
- include new fatresize(8) utility
- added patches:
  * parted-fatresize-autoconf.patch
* Wed Jan 22 2014 puzel@suse.com
- Do not fail when shrinking the partition in non-interactive mode.
- modified patches:
  * parted-resize-command.patch
* Wed Jan  8 2014 puzel@suse.com
- update to parted-3.1 (fate#316110)
- changes in parted-3.1:
  * Changes in behavior
  - Floppy drives are no longer scanned on linux: they cannot be
    partitioned anyhow, and some users have a misconfigured BIOS
    that claims to have a floppy when they don't, and scanning
    gets hung up.
  - parted: the mkpart command has changed semantics with regard
    to specifying the end of the partition.  If the end is
    specified using units of MiB, GiB, etc., parted subtracts one
    sector from the specified value.  With this change, it is now
    possible to create partitions like 1MiB-2MiB, 2MiB-3MiB and
    so on.
  * Many bugfixes (see changelog)
- changes in parted-3.0:
  * Changes in behavior
  - Remove all FS-related (file system-related) sub-commands;
    these commands are no longer recognized because they were all
    dependent on parted "knowing" too much about file system:
    mkpartfs, mkfs, cp, move, check.
  - 'resize' command changed semantics:
    it no longer resizes the filesystem, but only moves end
    sector of the partition
- libparted-devel contains libparted-fs-resize library
- add ability to change size of the partition (ignoring contained
  filesystem) with 'resize' command; this command has different
  semantics than the former 'resize' command which upstream
  decided to drop
  - parted-resize-command.patch (fate#316110)
- when using syncmbr on POWER, make the first partition type 0x41
  (PReP boot) (bnc#797485)
  - add libparted-ppc-prepboot-in-syncmbr.patch
- support for PReP GUID (bnc#797485)
  - parted-GPT-add-support-for-PReP-GUID.patch
- Build requires makeinfo
- drop fix-function-def.patch (not needed)
- drop parted-stdio.h.patch (not needed)
- drop parted-use-ext-range.patch (upstream)
- drop fix-nilfs2-probe-function.patch (upstream)
- drop parted-improve-loop-support.patch (upstream)
- drop always-resize-part.dif (FS support removed)
- merged following hybrid pMBR patches:
  parted-gpt-mbr-sync.patch,
  parted-gpt-sync-mbr-label.patch,
  parted-fix-gpt-sync-on-BE-systems.patch
* Mon Dec 30 2013 puzel@suse.com
- Fix partition device names on MMC devices (bnc#847580)
  - libparted-fix-mmcblk-partition-name.patch
* Tue Sep 17 2013 mlin@suse.com
- Add parted-Add-Intel-Rapid-Start-Technology-partition.patch:
  * Add Intel Fast Flash(iFFS) partition type support for Intel Rapid
    Start Technology. Added type 0x84 on MS-DOS and
    D3BFE2DE-3DAF-11DF-BA40-E3A556D89593 on GPT disk type.
* Mon Apr 22 2013 puzel@suse.com
- fix hybrid pMBR (gpt_sync_mbr) on BE systems (bnc#809205)
  - parted-fix-gpt-sync-on-BE-systems.patch
- detect btrfs filesystem (bnc#810779)
  - parted-btrfs-support.patch
* Mon Apr 15 2013 idonmez@suse.com
- Add Source URL, see https://en.opensuse.org/SourceUrls
- Add GPG checking
* Wed Nov 21 2012 puzel@suse.com
- add fix-error-informing-the-kernel.patch:
  Informing the kernel about partition changes still fails if first
  logical partition starts right after the extended partition. Fix
  it.
* Thu Sep 27 2012 puzel@suse.com
- add parted-workaround-windows7-gpt-implementation.patch
  (bnc#781688)
* Fri Jul 27 2012 aj@suse.de
- Fix build with missing gets declaration (glibc 2.16)
* Tue Jul  3 2012 puzel@suse.com
- copy dummy bootcode to MBR only on x86 because it can cause
  problems to certain ARM machine (bnc#769789)
  - add: dummy-bootcode-only-for-x86.patch
* Tue Apr 17 2012 puzel@suse.com
- fix informing the kernel about partitions on cciss devices
  (bnc#757225)
  - add: parted-fix-cciss-partition-naming.patch
* Fri Dec 30 2011 puzel@suse.com
- fix crash in nilfs2 probe function if there is tiny (1s)
  partition on the disk (bnc#735763)
  - fix-nilfs2-probe-function.patch
* Sun Nov 20 2011 coolo@suse.com
- add libtool as buildrequire to avoid implicit dependency
* Wed Oct 26 2011 puzel@suse.com
- improve loop support, fix geometry reporting on loopback devices:
  parted-improve-loop-support.patch (bnc#726603)
* Mon Sep 26 2011 puzel@suse.com
- improve parted-gpt-sync-mbr-label.patch: do not
  sync partitions that can not be represented by the DOS label
  (bnc#710402)
* Wed Sep  7 2011 puzel@suse.com
- change do-not-create-dm-nodes.patch so that parted does
  not remove dm partition mappings and leaves the job up
  to kpartx -u called via udev
  (bnc#712177, bnc#679780)
* Mon Sep  5 2011 puzel@suse.com
- add parted-use-ext-range.patch (bnc#715695)
* Thu Aug 25 2011 puzel@novell.com
- add parted-gpt-sync-mbr-label.patch (bnc#710402)
  - this patch implements support for special label 'gpt-sync-mbr'
* Tue Aug 16 2011 puzel@novell.com
- update parted-gpt-mbr-sync.patch so that it no longer
  creates synced partitions one sector shorter (bnc#700465)
* Sun Jul 31 2011 crrodriguez@opensuse.org
- Use ncursesw6 instead of plain-old ncurses5
- Disable automake silent rules
* Thu May 19 2011 puzel@novell.com
- update to parted-2.4
  * Bug fixes
  - parted no longer allows the modification of certain in-use
    partitions.  In particular, before this fix, parted would
    permit removal or modification of any in-use partition on a
    dmraid and any in-use partition beyond the 15th on a regular
    scsi disk.
  - Improve support of DASD devices on the s390 architecture.
    Parted now supports all DASD types (CKD and FBA), DASD formats
    (CDL, LDL, CMS non-reserved, and CMS reserved), and DASD
    drivers (ECKD, FBA, and DIAG) in all combinations supported by
    the Linux kernel.  As before, only CDL format on CKD DASD using
    the ECKD driver is supported for read-write operations (create,
    delete, move, re-size, etc.).  However, the implicit partition
    present on LDL- and CMS-formatted disks is now correctly
    recognized for read-only operations.  In detail:
  - parted now correctly handles LDL-format disks with a block
    size other than 4096 (bug fix)
  - parted now recognizes the CMS disk format, both reserved and
    non-reserved (enhancement)
  - parted now supports FBA DASD devices (enhancement)
  - parted now supports the DIAG driver when running in a virtual
    machine under z/VM (enhancement)
  - libparted: raise the limit on the maximum start sector and the
    maximum number of sectors in a "loop" partition table from 2^32
    to 2^64.
  - libparted once again recognizes a whole-disk FAT partition
  - libparted now recognizes scsi disks with a high major (128-135)
    as scsi disks
  - an msdos partition table on a very small device (smaller than
    one cylinder) is now recognized.
  - libparted: zero-length devices (other than files) are ignored
    rather than throwing an exception.
  - libparted: gpt label creation can no longer divide by zero with
    a defective device or when a concurrent writer modifies the
    PE-size bytes in the small interval between the write and
    subsequent read of the primary GPT header.
  * Changes in behavior
  - "parted $dev print" now prints information about the device
    (model, size, transport, sector size) even when it fails to
    recognize the disk label.
  - specifying partition start or end values using MiB, GiB, etc.
    suffixes now makes parted do what I want, i.e., use that
    precise value, and not some other that is up to 500KiB or
    500MiB away from what I specified.  Before, to get that
    behavior, you would have had to use carefully chosen values
    with units of bytes ("B") or sectors ("s") to obtain the same
    result, and with sectors, your usage would not be portable
    between devices with varying sector sizes.  This change does
    not affect how parted handles suffixes like KB, MB, GB, etc.
- drop always_print_geom.diff (merged upstream)
* Thu Dec  9 2010 puzel@novell.com
- add more-reliable-informing-the-kernel.patch (bnc#657360)
* Tue Nov  9 2010 puzel@novell.com
- updated always_print_geom.diff to print also physical/logical
  sector size (patch by Arvin Schnell)
* Fri Sep 17 2010 puzel@novell.com
- package according to shared library policy: split libparted0
- add build dependencies on libblkid and libuuid
* Fri Sep 17 2010 puzel@novell.com
- fix always-resize-part.dif (bnc#639579)
* Wed Aug 11 2010 puzel@novell.com
- update parted-type.patch (bnc#630009)
* Thu Jul  8 2010 puzel@novell.com
- update to parted-2.3
  - parted now recognizes ATA over Ethernet (AoE) devices
  - parted now recognizes Linux Software RAID Arrays
  - libparted has a new partition flag to check for diagnostic
    (aka recovery or reserved) partitions: PED_PARTITION_DIAG
  - When libparted deferenced a /dev/mapper/foo symlink, it would
    keep the resulting /dev/dm-N name and sometimes use it later,
    even though it had since become stale and invalid.
    It no longer stores the result of dereferencing a /dev/mapper
    symlink.
  - libparted's msdos_partition_is_flag_available function now
    always reports that the "hidden" flag is not available for
    an extended partition. Similarly,
    msdos_partition_get_flag(p,PED_PARTITION_HIDDEN) always
    returns 0 for an extended partition.
  - libparted uses a more accurate heuristic to distinguish between
    ext4 and ext3 partitions.
  - libparted now properly checks the return value of dm_task_run
    when operating on devicemapper devices.
  - allow using ped_device_cache_remove(dev) followed by a (later)
    ped_device_destroy() without corrupting the device cache.
  - when creating an ext2 file system, Parted no longer creates an
    invalid one when its size is 2TiB or larger.
- drop etherd_support.diff (included upstream)
- drop parted-remove-experimental-warning.patch (included upstream)
- drop make-align-check-work-in-interactive-mode.patch
  (included upstream)
- drop parted-no-inttypes-include (not needed)
- refresh all remaining patches
* Wed Jun 30 2010 puzel@novell.com
- update make-align-check-work-in-interactive-mode.patch to
  be consistent with upstream
* Mon Jun 28 2010 jengelh@medozas.de
- use %%_smp_mflags
* Thu May 27 2010 puzel@novell.com
- add make-align-check-work-in-interactive-mode.patch (bnc#608704)
* Fri Apr  2 2010 puzel@novell.com
- add parted-remove-experimental-warning.patch
- refresh always_print_geom.diff to apply at correct function
* Fri Feb 26 2010 puzel@novell.com
- update to parted-2.2
  - Changes in behavior
  - The default alignment (--align option) for newly created
    partitions has been changed to optimal.
  - New features
  - The ped_device_get_*_alignment() functions now return a sane
    default value instead of NULL when the so called topology
    information is incomplete.  The default minimum alignment aligns
    to physical sector size, the default optimal alignment is 1MiB,
    which is what vista and windows 7 do.
  - Bug fixes
  - Parted no longer uses a physical sector size of 0 or of any
    other value smaller than the logical sector size.
  - dos: creating an HFS or HFS+ partition in an msdos partition
    table used to set the partition type to 0x83.  That is wrong.
    The required number is 0xaf, and that is what is used now.
  - gpt: read-only operation could clobber MBR part of hybrid
    GPT+MBR table [bug introduced in parted-2.1]
  - gpt: a read-only operation like "parted $dev print" would
    overwrite $dev's protective MBR when exactly one of the primary
    and backup GPT tables was found to be corrupt.  [bug introduced
    prior to parted-1.8.0]
  - sun: the version, sanity and nparts VTOC fields were ignored by
    libparted.  Those fields are properly initialized now. The
    nparts (number of partitions) field is initialized to 8 (max.
    number of sun partitions) rather that to a real number of
    partitions. This solution is compatible with Linux kernel and
    Linux fdisk.
  - libparted: try harder to inform kernel of partition changes.
    Previously when editing partitions, occasionally the kernel
    would fail to be informed of partition changes.  When this
    happened future problems would occur because the kernel had
    incorrect information.  For example, if this problem arose when
    resizing or creating a new partition, then an incorrect
    partition size might be displayed or a user might encounter a
    failure to format or delete a newly created partition,
    respectively.
  - libparted: committing a disk that was returned by
    ped_disk_duplicate would always result in ped_disk_clobber being
    called (and thus the first and last 9KiB of the disk being
    zeroed), even if the duplicated disk, was not returned by
    ped_disk_fresh().
- drop do-not-install-test-programs.patch (fixed in upstream)
* Wed Feb 17 2010 puzel@novell.com
- add do-not-install-test-programs.patch
  - avoid deleting this in specfile
* Mon Feb  1 2010 puzel@novell.com
- update to parted-2.1 (noteworthy changes)
  * New features
  - new --align=<align> commandline option which can have the
    following values:
  - none: Use the minimum alignment allowed by the disk type
  - cylinder: Align partitions to cylinders (the default)
  - minimal:  Use minimum alignment as given by the disk
    topology information
  - optimal:  Use optimum alignment as given by the disk
    topology information
    The minimal and optimal values will use layout information
    provided by the disk to align the logical partition table
    addresses to actual physical blocks on the disks. The minimal
    value uses the minimum alignment needed to align the partition
    properly to physical blocks, which avoids performance
    degradation. Where as the optimal value uses a multiple of the
    physical block size in a way that guarantees optimal
    performance.  The min and opt values will only work when
    compiled with libblkid >= 2.17 and running on a kernel >=
    2.6.31, otherwise they will behave as the none --align value.
  - Parted now supports disks with sector size larger than 512 bytes.
    Before this release, parted could operate only on disks with a
  sector size of 512 bytes. However, disk manufacturers are
  already making disks with an exposed hardware sector size of
  4096 bytes. Prior versions of parted cannot even read a
  partition table on such a device, not to mention create or
  manipulate existing partition tables. Due to internal design
  and time constraints, the following less-common partition
  table types are currently disabled:
  - amiga, bsd, aix, pc98
  - new command "align-check TYPE N" to determine whether the
  starting sector of partition N is
  TYPE(minimal|optimal)-aligned for the disk.  The same
  libblkid and kernel version requirements apply as for --align
  * Bug fixes
  - parted can once again create partition tables on loop devices.
  - improved >512-byte sector support
  - gpt tables are more rigorously checked
  - improved dasd disk support
  - handle device nodes created by lvm built with udev
    synchronisation enabled properly.
  - when printing tables, parted no longer truncates flag names
  - Partitions in a GPT table are no longer assigned the
  "microsoft reserved partition" type.  Before this change,
  each partition would be listed with a type of "msftres" by
  default.
  * Notice
  - Parted stopped using BLKPG_* ioctls to inform the kernel
  about changes of the partition table. The consequence of this
  change is that parted alone can no longer inform the kernel
  about changes to partition table on a disk where some of the
  partitions are mounted.
- build requires check-devel and pkg-config
- drop parted-1.8.3.dif - fixed by adding pkg-config and check-devel
  to BuildRequires
- drop parted.tty.patch, parted.no-O_DIRECT.patch,
  do-not-discard-bootcode-in-extended-partition.patch,
  avoid-unnecessary-open-close.patch,
  do-not-unnecessarily-open-part-dev.patch
  - fixed upstream
- drop fix-tests.sh - make check disabled in specfile
- drop fix-error-informing-the-kernel.patch,
  fix-race-call-udevadm-settle.patch,
  retry-blkpg-ioctl.patch, use-ext-range.patch
  - affected code removed as part of the BLKPG to BLKRRPART
    switch
- clean up specfile
* Mon Feb  1 2010 jengelh@medozas.de
- package baselibs.conf
* Mon Jan 25 2010 puzel@novell.com
- use-ext-range.patch (bnc#567652)
* Thu Dec  3 2009 puzel@novell.com
- avoid-unnecessary-open-close.patch,
  do-not-unnecessarily-open-part-dev.patch,
  fix-race-call-udevadm-settle.patch,
  retry-blkpg-ioctl.patch (bnc#539521)
* Wed Oct  7 2009 puzel@novell.com
- do-not-create-dm-nodes.patch (bnc#501773)
* Fri Jul 31 2009 puzel@novell.com
- update to parted-1.9.0
  * bugfixes:
  * parted now preserves the protective MBR (PMBR) in GPT type
    labels.
  * gpt_read now uses SizeOfPartitionEntry instead of the size
  of GuidPartitionEntry_t. This ensures that *all* of the
  partition entries are correctly read.
  * mklabel (interactive mode) now correctly asks for
  confirmation, when replacing an existent label, without
  outputting an error message.
  * resize now handles FAT16 file systems with a 64k cluster.
  This configuration is not common, but it is possible.
  * parted now ignores devices of the type /dev/md* when
  probing.  These types of devices should be handled by the
  device-mapper capabilities of parted.
  * The parted documentation now describes the differences in
  the options passed to mkpart for the label types.
  * changes in behavior
  * In libparted, the linux-swap "filesystem" types are now
  called "linux-swap(v0)" and "linux-swap(v1)" rather than
  "linux-swap(old)" and "linux-swap(new)" as in parted 1.8, or
  "linux-swap" as in older versions; "old" and "new" generally
  make poor names, and v1 is the only format supported by
  current Linux kernels. Aliases for all previous names are
  available.
- drop following patches as they were merged upstream/are no
  longer needed:
  * 2TB_size_overflow.diff
  * disable_FAT_check.diff
  * do-not-automatically-correct-GPT.patch
  * dont-require-dvh-partition-name.patch
  * fix-array-overflow.patch
  * fix-corrupted-gpt-crash.patch
  * fix-dasd-probe.patch
  * fix-dvh-update.patch
  * fix-improper-data-conversion.patch
  * fix-make-install-failure.patch
  * gnulib.diff
  * parted-cmd-arg-fix.patch
  * parted-fdasd-compile-fixes
- remove FAT16 stuff from fat16_hfs_fix.dif, rename it hfs_fix.dif
- add fix-tests.sh
  * adjust testsuite so that it succeeds with our patchset
- update all patches to remove fuzz, renumber patches
- change license to GPL v3
- parted-type.patch: fix output of flags
* Wed Jul  1 2009 puzel@novell.com
- add libsepol-devel to BR: (fix build)
* Wed Jun 17 2009 puzel@suse.cz
- add fix-make-install-failure.patch (fix build)
- add fix-array-overflow.patch (fixes warning)
- split -lang subpackage
* Tue Apr  7 2009 crrodriguez@suse.de
- remove static libraries
* Tue Mar 10 2009 puzel@suse.cz
- fix-multipath-part-name.patch replaced with
  fix-dm-partition-name.patch (bnc#471440)
* Wed Feb 18 2009 puzel@suse.cz
- do-not-automatically-correct-GPT.patch (bnc#436825)
* Tue Feb 10 2009 puzel@suse.cz
- dont-require-dvh-partition-name.patch (bnc#471703)
* Mon Feb  9 2009 puzel@suse.cz
- parted-cmd-arg-fix.patch (bnc#473207)
* Fri Jan 23 2009 puzel@suse.cz
- do-not-discard-bootcode-in-extended-partition.patch (bnc#467576)
* Fri Jan 23 2009 puzel@suse.cz
- fix-error-informing-the-kernel.patch (bnc#449183)
* Thu Jan 22 2009 puzel@suse.cz
- fix-multipath-part-name.patch (bnc#447591)
* Wed Jan  7 2009 olh@suse.de
- obsolete old -XXbit packages (bnc#437293)
* Wed Nov 26 2008 puzel@suse.cz
- fix-dasd-probe.patch (bnc#438681)
* Fri Nov  7 2008 puzel@suse.cz
- fix-corrupted-gpt-crash.patch (bnc#439910)
- fix-dvh-update.patch (bnc#397210)
* Wed Nov  5 2008 puzel@suse.cz
- disabled largest_partition_number.patch (bnc#440141)
* Mon Oct 20 2008 puzel@suse.cz
- fix improper data conversion (bnc#435702)
* Tue Oct  7 2008 puzel@suse.cz
- updated largest_partition_number.patch (bnc#428992)
* Thu Aug 28 2008 kukuk@suse.de
- Kill *.la file
* Mon Aug 25 2008 prusnak@suse.cz
- enabled SELinux support [Fate#303662]
* Thu Aug 21 2008 agraf@suse.de
- fix the GPT sync to work properly on Macs
* Mon Aug 11 2008 agraf@suse.de
- make GPT sync more compatible:
  - don't sync on IA64
  - always add a partition with partition type 0xee, so Linux is happy
  - protect the EFI System Partition if available
* Tue Jul 22 2008 hare@suse.de
- Fix fdasd.c compilation
- Don't include broken inttypes.h
* Fri Jul 18 2008 agraf@suse.de
- add GPT sync, so whenever the GPT is modified, fake MBR entries
  for the first 4 partitions will be created. This fixes booting
  from disks > 2TB and makes booting a Mac possible (bnc#220839)
* Tue Jul  8 2008 puzel@suse.cz
- added largest_partition_number.patch
  * fixes computation of largest partition number (bnc#397210)
* Fri May  9 2008 schwab@suse.de
- Fix gnulib macro and use autoreconf.
* Thu Apr 10 2008 ro@suse.de
- added baselibs.conf file to build xxbit packages
  for multilib support
* Mon Mar 24 2008 ro@suse.de
- fix typo in specfile
* Thu Mar 20 2008 meissner@suse.de
- fix buildrequires
- change from loading libreiserfs dynamically to just link it
  (avoids adding libreiserfs-devel + deps to the system)
  FATE#303510
- enable device mapper linking (I very much doubt it was intended to
  be disabled)
* Sun Mar 16 2008 crrodriguez@suse.de
- fix file-not-in-lang rpmlint warnings
* Tue Jan 15 2008 fehr@suse.de
- Add patch 2TB_size_overflow.diff developed by Jim Meyering
  <meyering@redhat.com> to properly handle cases of overflow over
  2TB limit in msdos label (#352484)
* Mon Aug 13 2007 fehr@suse.de
- Update to new version 1.8.8
    Properly detect 'ext2 fs too small' cases.
    Read an msdos partition table from a device with 2K sectors.
    Correct handling of HeaderSize field in GPT labels.
    Fix block number used when checking for ext2 fs state.
    Add detection support for Xen virtual block devices (/dev/xvd*).
    Fixed exception handling in mkpart and mkpartfs commands.
    Fix invalid command line argument handling.
    Close memory leaks in parted.c and table.c.
* Fri Jul 13 2007 olh@suse.de
- do not open with O_DIRECT (#290087)
* Thu Jul  5 2007 sassmann@suse.de
- fix parted to generate parseable output (#289049)
    added check to test if tty is availabe, if no tty is available
    readline functions are omitted
* Thu Jun 21 2007 adrian@suse.de
- fix changelog entry order
* Sun May 13 2007 olh@suse.de
- restore mkpart linux-swap syntax (#274080)
* Thu May 10 2007 fehr@suse.de
- Update to new version 1.8.7
    Fix primary partition cylinder alignment error for DOS disk labels
    Avoid segfault due to a double free on reiserfs support
    Fix script mode (-s) for mkfs command in parted
    Fix off-by-one bug in parted when displaying information about the disk
* Wed May  2 2007 olh@suse.de
- remove unused check-devel from buildrequires to allow build in sles10
* Tue Mar 27 2007 sbrabec@suse.cz
- Require check-devel.
* Thu Mar 22 2007 fehr@suse.de
- Update to new version 1.8.6
    Revert the implementation of the linux-swap(new) and linux-swap(old) types.
- Update to new version 1.8.5
    Add po translations
- Update to new version 1.8.4
    Minor bug fix release for 1.8.3 to fix build issues on various platforms
* Mon Mar 19 2007 fehr@suse.de
- Update to new version 1.8.3
    libparted:
  - Sync the linux-swap header according to the Linux kernel sources.
  - Enable support for swsusp partitions and the ability to differentiate
    between old and new versions of linux-swap partitions.
  - Preserve starting sector for primary NTFS 3.1 partitions on DOS disklabel.
  - Handle 2048-byte logical sectors in linux_read().
  - Don't assume logical sector size is <= 512B on AIX.
  - Detect HFS write failure.
  - Added HFS+ resize support.
    parted/partprobe:
  - Use fputs() and putchar() in place for printf(), when possible.
  - Detect/report stdout write errors.
  - Accept the --version and --help options.
  - Fix memory leaks in parted(8).
* Wed Mar  7 2007 fehr@suse.de
- make resize of ext2/3 under YaST2 work again (#249674)
* Tue Feb 20 2007 fehr@suse.de
- make mklabel in scripted mode work again
* Mon Jan 15 2007 fehr@suse.de
- Update to new version 1.8.2
    libparted:
  - Add the ped_device_cache_remove() function to remove a device from the
    cache.  This is necessary for some things that use libparted, including
    pyparted.
  - Fix a segfault in ped_assert() where the wrong pointer is freed in the
    backtrace handler.
  - Only call _disk_warn_loss(disk) in do_mklabel() if disk is not NULL.
    Fixes a segfault when initializing new volumes.
  - Dynamically allocate space for exception messages.
  - Output a backtrace when catching SEGV_MAPPER or a general SIGSEGV.
    parted:
  - Destroy all objects before return when called with --list or --all option.
  - Zero sized device is shown as 0.00B and not -0.00kB.
  - Implement 'print devices' command.
  - Alias 'print list' to 'print all'.
  - Alias 'mktable' to 'mklabel'.
* Tue Dec  5 2006 fehr@suse.de
- Update to new version 1.8.1
  libparted
    Rework backtrace support
    Disable ext2fs resize for now, tell user to use resize2fs
    GPT fixes
    Prevent SIGFPE when FAT sector size is 0
    DASD support for IBM zSeries systems
    AIX disk label support
    Detect Promise SX8 storage devices
    Macintosh (ppc and x86) disk label improvements
    Add support binary units (MiB, KiB, GiB)
    Fix geometry read problems on 64-bit Macs
    Add support for /dev/mapper devices via libdevmapper library
    Detect Apple_Boot partition types correctly on MacOS X 10.4 systems
  parted
    Fix loop in print_all().
    Introduce the -list command-line switch.
    Warn before mklabel and mkfs.
    Proper print when there are no extended partitions, but partition names.
* Tue Nov  7 2006 ro@suse.de
- fix manpage permissions
* Fri Jul 21 2006 olh@suse.de
- keep kernel interface to extended partition on Linux
* Tue Jul 18 2006 olh@suse.de
- build with make -j
  add parted-mac_data-init.patch
  add parted-mac-set-type-corruption.patch (#192082)
* Mon May 29 2006 fehr@suse.de
- Update to new version 1.7.1
  libparted: bug fixes related to linking, HFS, ext2, the Mac disk label
  parted: signal handling bug fix
* Thu May 18 2006 fehr@suse.de
- Update to new version 1.7.0
  libparted:
  * support for Apple GUIDs to GPT code
  * probe /dev/hd? before /dev/sd?
  * prefer /sys/block to /proc/partitions where possible
  * fix of ext2 "strange layout" bug (EXPERIMENTAL)
  * handling of sector sizes not equal to 512
  * added ped_device_get_constraint to support device-dependent constraints
  parted:
  * new formatter for "print" command
  * SIGSEGV handler
  * fixed "rescue" command core dump
  * fixes for 'mkpart' and 'mkpartfs' and 'print'
  * position and size of partitions are displayed with up to two
    digits after the decimal dot (depending on the unit and value)
  manual:
  * cut down substantially.
    Lots of general content will be moved to the GNU Storage Guide.
* Tue Apr 25 2006 fehr@suse.de
- Update to new version 1.7.0rc5
* Mon Mar  6 2006 schwab@suse.de
- Fix format string.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Dec  6 2005 fehr@suse.de
- update to new version 1.6.25.1
* Wed Nov  9 2005 fehr@suse.de
- update to new version 1.6.25
- make parted correctly refuse to resize inconsistent fat
  filesystems even if env var YAST_IS_RUNNING is set (#132967)
* Thu Sep  8 2005 fehr@suse.de
- fix wrong permissions of brazilian man page (#114849)
* Mon Aug 15 2005 fehr@suse.de
- update to new version 1.6.24
* Wed Aug  3 2005 fehr@suse.de
- make parted print BIOS geometry also if no disk label is present
  (#100444)
* Thu Jul 28 2005 fehr@suse.de
- update to new version 1.6.23
* Tue Jul 19 2005 pkirsch@suse.de
- fix fat16 minimum requirements
- fix mac partition handling
* Thu Apr  7 2005 fehr@suse.de
- update to new version 1.6.22
* Wed Mar 16 2005 fehr@suse.de
- prevent shifted start sect when resizing with unknown fs (#73008)
* Mon Jan 17 2005 fehr@suse.de
- fix typo in input_sector.patch
- update to new version 1.6.21
* Thu Jan 13 2005 fehr@suse.de
- allow creation of partitions by exact sector number (#49276)
* Tue Jan 11 2005 fehr@suse.de
- update to new version 1.6.20
* Mon Nov 29 2004 fehr@suse.de
- update to new version 1.6.19
- add reiserfs to needforbuild
* Mon Nov 22 2004 fehr@suse.de
- update to new version 1.6.18
* Mon Nov  8 2004 fehr@suse.de
- update to new version 1.6.16
* Tue Oct 26 2004 fehr@suse.de
- add patch by SGI for documentation of dvh-disklabel (#47611)
* Wed Sep 29 2004 fehr@suse.de
- add support for ATA over ethernet
- add support for partitioning device-mapper devices (for dmraid)
* Mon Sep 20 2004 fehr@suse.de
- update to new version 1.6.15
* Thu Sep 16 2004 fehr@suse.de
- greatly simplify always-resize-part.dif by using
  ped_constraint_exact
* Wed Sep 15 2004 fehr@suse.de
- prevent unwanted modifying of partition start and end due to
  alignment constraints during resize (#45013, #44699)
* Mon Sep  6 2004 fehr@suse.de
- update to new version 1.6.14
* Mon Sep  6 2004 fehr@suse.de
- update to new version 1.6.13
* Mon Aug 16 2004 fehr@suse.de
- update to new version 1.6.12
* Mon Apr 26 2004 fehr@suse.de
- update to new version 1.6.11
* Wed Mar 31 2004 meissner@suse.de
- Detect viodasd virtual disks on iSeries. #37521
* Sat Jan 10 2004 adrian@suse.de
- add %%run_ldconfig
* Mon Oct 20 2003 fehr@suse.de
- fix printing of partitions larger than 1TB in size (#32319)
* Fri Sep 12 2003 fehr@suse.de
- extend parted to handle User-mode virtual block devices (#30375)
* Mon Sep  8 2003 fehr@suse.de
- do not warning about too new GPT version if running under YaST2
  and too new version is 0x00010200 (#29563)
* Mon Jul 28 2003 fehr@suse.de
- update to new version 1.6.6
* Thu Jun 19 2003 ro@suse.de
- build with current gettext
* Thu Jun 12 2003 fehr@suse.de
- add missing dir to filelist
* Thu Apr 24 2003 ro@suse.de
- fix install_info --delete call and move from preun to postun
* Thu Mar 20 2003 fehr@suse.de
- display also partitions of type Apple_Free on Macintosh
* Mon Feb 24 2003 fehr@suse.de
- update to new version 1.6.5
* Mon Feb 17 2003 fehr@suse.de
- Use env var YAST_IS_RUNNING instead if YAST2_RUNNING for checking
  if parted is called by YAST2
* Fri Feb  7 2003 fehr@suse.de
- Use %%install_info macro
* Mon Feb  3 2003 fehr@suse.de
- disable check for string "FAT" in boot sector since it makes
  parted fail on some IDE disks with TurboLinux installed (#19401)
* Tue Dec 10 2002 fehr@suse.de
- update to new version 1.6.4
* Mon Nov 18 2002 schwab@suse.de
- Add AM_GNU_GETTEXT_VERSION.
* Mon Sep 23 2002 meissner@suse.de
- recognize AIX IPL signatures in MSDOS labels and mark these labels
  invalid. Also overwrite the AIX IPL signature on "mklabel" (#20039).
* Mon Sep  2 2002 fehr@suse.de
- fix bug occuring sometimes when resizing reiserfs from YaST2
  (bug was in patch always-resize-part.dif)
* Tue Aug 13 2002 fehr@suse.de
- update to parted 1.6.3
* Thu Aug  8 2002 fehr@suse.de
- add patch to ignore /proc/sys/kernel/real-root-dev and do a stat
  on "/" instead. real-root-dev does not always contain a valid
  entry
* Tue Aug  6 2002 meissner@suse.de
- redid patch for partition ids on MAC with some API additions
  to make it 64bit clean.
* Thu Aug  1 2002 fehr@suse.de
- add patch by Marcus Meissner to show partition type on MACs
* Thu Jul 25 2002 fehr@suse.de
- add patch by Marcus Meissner to show and set partition id on dos
  label
* Tue Jul 16 2002 schwab@suse.de
- Update to parted 1.6.2, needed for ia64.
* Tue Jul  2 2002 meissner@suse.de
- rerun auto* tools
* Thu Jun 27 2002 fehr@suse.de
- make setting flags lvm and raid to off work
* Mon Jun 10 2002 fehr@suse.de
- add patch to resize also partitions with unkown fs under YaST2
* Tue May  7 2002 fehr@suse.de
- update to 1.4.24
- add patch to be verbose when resizing fat under YaST2
* Tue May  7 2002 ro@suse.de
- fixed specfile: no macro allowed in Version: line
* Fri Apr 26 2002 coolo@suse.de
- use %%_libdir
* Mon Sep  3 2001 kkaempf@suse.de
- update to 1.4.18
  compiles now with gcc 3.x and new autoconf/automake.
  support for ext3.
  lots of minor fixes, see ChangeLog in source.
* Thu May 10 2001 freitag@suse.de
- Added documentation to filelist, Bug# 6115
* Wed May  9 2001 mfabian@suse.de
- bzip2 sources
* Mon Apr 30 2001 tom@suse.de
- Change to new version 1.4.11
  Removed configure patch (not needed anymore)
  Removed gettextize (doesn't build)
  Changed shared libraries to new state in file list
* Thu Apr 12 2001 ro@suse.de
- gettextize for new gettext
* Wed Apr  4 2001 kukuk@suse.de
- Add shared libraries to filelist for intel
* Fri Mar 23 2001 schwab@suse.de
- Fix configure check for sizeof off_t.
- Enable shared libs for x86 now that llseek.c rubbish is not
  needed any more.
* Fri Feb 23 2001 uli@suse.de
- enabled shared libs for non-x86 archs (see libparted/llseek.c for
  explanation why this doesn't work for x86)
* Thu Feb 22 2001 ro@suse.de
- added readline/readline-devel to neededforbuild (split from bash)
* Fri Jan 12 2001 tom@suse.de
- update to version 1.4.6
* Wed Jan  3 2001 tom@suse.de
- update to version 1.4.5
* Mon Dec  4 2000 schwab@suse.de
- Add %%suse_update_config.
* Fri Dec  1 2000 tom@suse.de
- update to version 1.4.4
* Tue Nov 21 2000 tom@suse.de
- update to version 1.4.2
* Thu Nov  9 2000 ro@suse.de
- fixed neededforbuild
* Tue Oct 10 2000 tom@suse.de
- initial version, GNU parted 1.2.9
