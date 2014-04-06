OpenSuSE-fatresize
==================

Build Project for fatresize on  OpenSuSE


We had the need to toogle  Jeos partions images ´s FAT16 /FAT32  on opensuse 13.1.<br>
Fat2resize been the known working tool for it.<br>

The  parted release shiped on opensuse 13.1 arm raspberry PI NOT compiled with fat2resize , <br>
neither the fat2resize 1.03 are shipped .<br>



Build dependencies required:

  - libparted0-2.4-34.2.1.armv6hl
  - parted-2.4-34.2.1.armv6hl
  - parted-devel-2.4-34.2.1.armv6hl
  - automake ( from oss distro )
  - autoconf ( from oss distro )
  - libtool ( from oss distro )
  - shtool 2.0.8 ( https://www.gnu.org/software/shtool/shtool.html )

 SPEC & Build Project Info are here ; <br>
 The Build for Raspberry PI RPM & SRPM created for Opensuse 13.1 RPI arm <br>
 are stored at Our Drop Box URL https://www.dropbox.com/sh/ofpzj8u3j2v43zq/mqoFqLLzQB 
