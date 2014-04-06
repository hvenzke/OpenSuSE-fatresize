OpenSuSE-fatresize
==================

Build Project for fatresize 1.0.2 on  OpenSuSE


We had the need to toogle RPI images ´s FAT16 /FAT32  on OpenSuse 13.1.<br>
Fat2resize been the known working tool for it.<br>

The  parted release shiped on opensuse 13.1 arm Raspberry PI  _NOT_ compiled with fat2resize , <br>
neither the fat2resize 1.0.2 are shipped on Arm RPi  .<br>



Build dependencies required:

  - libparted0-2.4-34.2.1.armv6hl ( from oss distro )
  - parted-devel-2.4-34.2.1.armv6hl ( from oss distro )
  - libudev-devel  ( from oss distro )
  - device-mapper-devel  ( from oss distro )
  - automake ( from oss distro )
  - autoconf ( from oss distro )
  - libtool ( from oss distro )
  - shtool 2.0.8 ( https://www.gnu.org/software/shtool/shtool.html ), see below.

 SPEC & Build Project Info are here ; <br>
 The Build for Raspberry PI RPM & SRPM created for Opensuse 13.1 RPI arm <br>
 are stored at Our Drop Box URL https://www.dropbox.com/sh/ofpzj8u3j2v43zq/mqoFqLLzQB 

 an Updated parted 3.1 SRPM release for RPI are taken from    
 http://download.opensuse.org/ports/ppc/source/factory/repo/oss/suse/src/
 and rebuild with fatresize support.


 Build changes :
  fatresize 1.0.2    -  completed
  patch applied that lower the FAT2MIN to 32MB , uppon the FAT spec this are correct for SD and USB sticks.


 depend Build Changes :
  shtool 2.0.8    - completed 
  parted 3.1      - in progress

  
