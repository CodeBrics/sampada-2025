# Firmware Analysis Results

## Found Startup Scripts:

- `/etc/init.d/rcS`
- `/sbin/init`

## Analysis of Startup Scripts:

### Startup Script: `/etc/init.d/rcS`

- **Directory Name**: `/etc/init.d`
- **File Name**: `rcS`
- **File Type**: `POSIX shell script, ASCII text executable`
- **MD5 Hash**: `136123cc52047e72676753cdcf038284`
- **File Size**: `155 bytes`
- **Architecture**: `Not applicable`
- **Current Date**: `Friday, January 31, 2025, 2 PM `

---

### Startup Script: `/bin/busybox`

- **Directory Name**: `/bin`
- **File Name**: `busybox`
- **File Type**: `ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped`
- **MD5 Hash**: `a053573c0e452c7a96c3fc028d2b9e8e`
- **File Size**: `1337336 bytes`
- **Architecture**: `ARM`
- **Current Date**: `Friday, January 31, 2025, 2 PM `

---

# Detected Suspicious Strings

### File: `linuxrc`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `init`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/getty`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/lsusb`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/ifdown`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/makedevs`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/pppoe`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/ifconfig`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/chat`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/upnp_tv_ctrlpt`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/route`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/depmod`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/insmod`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/reboot`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/mdev`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/ifup`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/init`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/lsmod`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/hdparm`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/3gpp`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/net3g`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/netinit`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/halt`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/netinit6`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/dvrhelper`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/inetd`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/fdisk`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/modprobe`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/rmmod`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/pppd`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/pppoe-start`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `sbin/upgraded`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/lspci`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `sbin/poweroff`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `etc/inittab`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `exec`     |

### File: `etc/passwd`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/services`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `exec`     |
| `http://`     |

### File: `etc/passwd-`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/protocols`

| Keyword        |
|----------------|
| `http://`     |

### File: `etc/init.d/S80network`

| Keyword        |
|----------------|
| `bash`     |
| `/bin/sh`     |

### File: `etc/init.d/S02wndev`

| Keyword        |
|----------------|
| `bash`     |
| `http://`     |
| `wget`     |

### File: `etc/init.d/S81toe`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/init.d/S99dh`

| Keyword        |
|----------------|
| `chmod`     |
| `/bin/sh`     |

### File: `etc/init.d/S01udev`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/init.d/S00devs`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/init.d/rcS`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/udev/rules.d/75-persistent-net-generator.rules.optional`

| Keyword        |
|----------------|
| `admin`     |

### File: `boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin`

| Keyword        |
|----------------|
| `http://`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/killall`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/mknod`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/cttyhack`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/touch`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/free`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/mesg`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/df`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/killall5`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/tar`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/msh`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/umount`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/nice`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/gzip`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/passwd`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/mv`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/eject`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/chat`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/[`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/echo`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/vi`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/sleep`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/sync`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/iproute`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/mktemp`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/top`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/ping6`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/dnsdomainname`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/mkdir`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/dd`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/ping`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/printenv`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/iptunnel`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/chmod`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/bootenv`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/busybox`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/login`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/ps`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/ls`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/ifenslave`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/[[`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/cat`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/kill`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/grep`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/ip`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/netstat`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/mount`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/wget`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/pwd`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/awk`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/p7zip`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/sh`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/iprule`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/iplink`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/cp`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/uname`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/rm`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/vlock`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/ash`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/devmem`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/hostname`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/du`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/gunzip`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/ipaddr`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/hush`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `bin/less`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `tmp/daemon1`

| Keyword        |
|----------------|
| `bash`     |

### File: `lib/ld-uClibc-0.9.33.2.so`

| Keyword        |
|----------------|
| `exec`     |

### File: `lib/libpthread-0.9.33.2.so`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `exec`     |

### File: `lib/libc.so.0`

| Keyword        |
|----------------|
| `chmod`     |
| `/bin/sh`     |
| `exec`     |
| `password`     |

### File: `lib/libpthread.so.0`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `exec`     |

### File: `lib/ld-uClibc.so.0`

| Keyword        |
|----------------|
| `exec`     |

### File: `lib/libgcc_s.so.1`

| Keyword        |
|----------------|
| `exec`     |

### File: `lib/libuClibc-0.9.33.2.so`

| Keyword        |
|----------------|
| `chmod`     |
| `/bin/sh`     |
| `exec`     |
| `password`     |

### File: `web/webplugin.exe`

| Keyword        |
|----------------|
| `http://`     |
| `FindNextFileA`     |
| `CopyFileA`     |
| `CreateProcessA`     |
| `https://`     |
| `FindFirstFileA`     |

### File: `web/index.htm`

| Keyword        |
|----------------|
| `base64`     |
| `admin`     |
| `password`     |
| `http://`     |

### File: `web/SigFileList`

| Keyword        |
|----------------|
| `base64`     |

### File: `web/olp.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/jsCore/aes.js`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/jsCore/rpcCore.js`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `exec`     |

### File: `web/config/index.htm`

| Keyword        |
|----------------|
| `base64`     |
| `admin`     |
| `password`     |
| `http://`     |

### File: `web/js/wificfg.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/update.js`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/js/iscsiconfig.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/deviceInitial.js`

| Keyword        |
|----------------|
| `admin`     |

### File: `web/js/broadcast.js`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/js/3gnetcfg.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/ddnsconfig.js`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |

### File: `web/js/loginEx.js`

| Keyword        |
|----------------|
| `admin`     |

### File: `web/js/useronvif.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/index.js`

| Keyword        |
|----------------|
| `password`     |
| `admin`     |

### File: `web/js/imageprty.js`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/js/connetcfg.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/defaultcfg.js`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/js/findPwd.js`

| Keyword        |
|----------------|
| `password`     |
| `admin`     |

### File: `web/js/qrcode.js`

| Keyword        |
|----------------|
| `base64`     |

### File: `web/js/adddevice.js`

| Keyword        |
|----------------|
| `password`     |
| `admin`     |

### File: `web/js/previewindex.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/pppoe.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/usermanage.js`

| Keyword        |
|----------------|
| `password`     |
| `admin`     |

### File: `web/js/chanldiscgroup.js`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/js/remotestorage.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/emailconfig.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/image/icons2.png`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/platformHtm/GAYS.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/platformHtm/GAYS.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/previewindex.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/audiocfg.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/3gnetcfg.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/remotestorage.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/usermanage.htm`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

### File: `web/html/useronvif.htm`

| Keyword        |
|----------------|
| `password`     |
| `admin`     |

### File: `web/html/pppoe.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/emailconfig.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/alarmindex.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/wificfg.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/adddevice.htm`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

### File: `web/html/ddnsconfig.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/chanldiscgroup.htm`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/html/update.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/faceplayback.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/iscsiconfig.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/setindex.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/infoindex.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/css/oem.css`

| Keyword        |
|----------------|
| `password`     |

### File: `web/jsBase/lib/m1.2.js`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/jsBase/lib/qrcode.js`

| Keyword        |
|----------------|
| `base64`     |

### File: `usr/SigFileList`

| Keyword        |
|----------------|
| `password`     |

### File: `usr/sbin/usb_modeswitch`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `usr/sbin/ii`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/sbin/.dec.sh`

| Keyword        |
|----------------|
| `bash`     |
| `base64`     |

### File: `usr/sbin/nfs`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/sbin/3gpp`

| Keyword        |
|----------------|
| `password`     |
| `http://`     |
| `bash`     |
| `/bin/sh`     |
| `admin`     |
| `chmod`     |
| `exec`     |

### File: `usr/etc/load_modules.sh`

| Keyword        |
|----------------|
| `chmod`     |
| `/bin/sh`     |

### File: `usr/bin/Challenge`

| Keyword        |
|----------------|
| `base64`     |
| `password`     |
| `http://`     |
| `/bin/sh`     |
| `admin`     |
| `https://`     |
| `chmod`     |
| `exec`     |
| `openssl`     |
| `wget`     |

### File: `usr/bin/DahuaExec`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/bin/lua/compat-5.1.lua`

| Keyword        |
|----------------|
| `http://`     |
| `wget`     |

### File: `usr/bin/lua/LiveUpdate.lua`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_i2s.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vicap.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/sysctl_hi3521a_asic.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/crgctrl_hi3521a.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vga_hdmi_spi.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_tde.ko`

| Keyword        |
|----------------|
| `wget`     |

### File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_vou.ko`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_vpss.ko`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/lib/lib.7z.extracted/0/lib/load_hisimod.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/8192cu.ko`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/data/config.lua`

| Keyword        |
|----------------|
| `admin`     |

### File: `usr/data/space`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/data/Data/StringAll.7z.extracted/0/StringAll`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `usr/data/Data/sharePicture/reset3.png`

| Keyword        |
|----------------|
| `http://`     |

# Vulnerabilities in executable files

## File: web/jsCore/rsa.js
**Ports**: 1, 10, 11, 12, 127, 128, 14, 15, 16, 16383, 192, 2, 2048, 224, 24, 255, 256, 26, 28, 3, 30, 32, 32767, 36, 4, 5, 52, 6, 63, 65535, 7, 8, 9
### Encryption/Encoding: Hex, RSA

## File: web/js/serialconfig.js
**Ports**: 1, 1200, 19200, 2, 2400, 3, 38400, 4800, 5, 57600, 9600

## File: usr/bin/lua/ptz/HY.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 5, 6, 8, 9

## File: web/js/https.js
**Ports**: 1, 127, 2, 20, 200, 3, 4, 63, 80, 800

## File: bin/bootenv
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/udev/rules.d/54-gphoto.rules
**Ports**: 1, 2, 4, 5, 6, 660, 8, 98

## File: web/js/logmanage.js
**Ports**: 1, 10, 100, 12, 1900, 2, 20, 200, 23, 400

## File: usr/bin/lua/ptz/PelcoD1_Tour.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: web/html/alarmindex.htm
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 1999, 2, 25, 3, 4, 5, 6, 7, 8, 9

## File: web/html/ipcFaceNewConfig.htm
**Ports**: 1, 10, 100, 3, 300, 35, 50, 500, 600

## File: bin/chmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/ipaddr
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/SigFileList
**Ports**: 54, 60, 75, 90, 97, 99

## File: bin/ls
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoD-DON.lua
**Ports**: 14, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: bin/df
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/data/ssl/ca.key
**Ports**: 8

## File: usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vicap.sh
**Ports**: 1, 10, 32

## File: etc/services
**Ports**: 1, 1000, 1001, 10080, 10081, 10082, 10083, 101, 102, 104, 105, 106, 107, 1080, 109, 1099, 11, 110, 1109, 111, 11201, 1127, 113, 115, 116, 117, 1178, 119, 1210, 1214, 123, 1236, 1241, 129, 13, 1300, 1313, 1314, 135, 1352, 137, 138, 139, 143, 1433, 1434, 15, 1524, 1525, 1529, 15345, 161, 162, 163, 164, 1645, 1646, 1649, 17, 17001, 17002, 17003, 17004, 174, 177, 178, 179, 18, 1812, 1813, 19, 191, 194, 1957, 1958, 1959, 199, 2, 20, 2000, 20011, 20012, 2003, 201, 2010, 202, 204, 2053, 206, 209, 21, 210, 2101, 2102, 2103, 2104, 2105, 2111, 2121, 213, 2150, 22, 220, 22273, 23, 2401, 2430, 2431, 2432, 2433, 24554, 25, 2583, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2628, 27374, 29, 2988, 2989, 3, 3050, 3130, 3306, 345, 346, 347, 3493, 3632, 369, 3690, 37, 370, 371, 372, 389, 39, 4, 406, 42, 4224, 43, 443, 444, 445, 45, 4557, 4559, 4600, 465, 487, 4899, 49, 4949, 5, 50, 500, 5002, 512, 513, 514, 515, 5151, 517, 518, 520, 5222, 525, 526, 5269, 53, 530, 5308, 531, 532, 533, 5354, 5355, 538, 540, 543, 5432, 544, 548, 5555, 5556, 556, 563, 5674, 5675, 5680, 57, 57000, 587, 6, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 60177, 60179, 607, 610, 611, 612, 631, 6346, 6347, 636, 65, 655, 6566, 6667, 67, 68, 69, 7, 70, 7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 7009, 706, 7100, 749, 750, 751, 752, 754, 760, 761, 765, 77, 775, 777, 779, 783, 79, 80, 8021, 808, 8080, 8081, 8088, 87, 871, 873, 88, 9, 901, 9101, 9102, 9103, 9359, 95, 9673, 98, 989, 99, 990, 992, 993, 994, 995
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: SSL, TLS

## File: web/config/index.htm
**Ports**: 1, 10, 100, 1000, 10000, 172, 176, 1999, 2, 200, 210, 3, 30, 4, 400, 42, 5, 500, 6, 60, 7, 8, 9, 9999
### Encryption/Encoding: Base64

## File: usr/bin/lua/ptz/SANLI.lua
**Ports**: 1, 128, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 64, 7, 8, 80

## File: web/js/general.js
**Ports**: 1, 1024, 255, 3

## File: web/css/setindex.css
**Ports**: 1, 10, 100, 1000, 10001, 101, 5, 50, 6, 7, 70, 8, 80

## File: web/css/faceplayback.css
**Ports**: 100, 33, 555, 67

## File: web/html/faceplayback.htm
**Ports**: 1, 10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1999, 2, 20, 2012, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 4, 6, 7, 8, 9

## File: usr/data/Data/StringAll.7z
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 24, 25, 27, 28, 29, 3, 30, 31, 32, 329, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 45, 47, 48, 49, 5, 50, 5266, 53, 55, 57, 58, 59, 6, 60, 61, 619, 62, 63, 64, 66, 665, 68, 69, 7, 70, 71, 73, 736, 74, 75, 758, 77, 78, 788, 8, 80, 83, 84, 85, 87, 89, 9, 90, 91, 94, 95, 96, 97, 98

## File: web/html/upnpconfig.htm
**Ports**: 1, 65535

## File: lib/libm-0.9.33.2.so
**Ports**: 1, 101, 11, 12, 135, 14, 18, 182, 2, 208, 22, 23, 24, 3, 30, 320, 33333, 375, 4, 40, 42, 43, 44, 45, 46, 47, 5, 50, 51, 53, 55, 56, 6, 60, 62, 7, 75, 8, 80, 81, 82, 83, 8353, 84, 85, 87, 9

## File: web/html/previewindex.htm
**Ports**: 1, 10, 100, 11, 12, 128, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 31, 32, 36, 3600, 4, 5, 6, 62, 64, 7, 8, 80, 9, 900

## File: sbin/dvrhelper
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/WindowManager.js
**Ports**: 1, 2, 3, 4

## File: bin/sh
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoP-A.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 5, 6, 7, 8

## File: web/html/blackwhite.htm
**Ports**: 1, 64

## File: etc/init.d/rcS
**Ports**: 9

## File: usr/lib/lib.7z.extracted/0/lib/avss.ko
**Ports**: 1, 10, 2, 2017, 29, 3, 32, 35, 4, 5, 6, 7, 8, 9
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: AES, RSA

## File: web/js/update.js
**Ports**: 1, 10, 100, 16, 2, 20, 200, 251, 3, 30, 300, 4, 5, 500, 6, 9
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: Base64

## File: usr/lib/lib.7z.extracted/0/lib/hi_i2c.ko
**Ports**: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9

## File: etc/udev/rules.d/60-pcmcia.rules
**Ports**: 1, 16

## File: lib/SigFileList
**Ports**: 1, 2, 33, 6, 9

## File: web/css/playbackindex.css
**Ports**: 10, 100, 1000, 10000, 11, 2000, 444, 555, 900, 998, 999, 9995, 9999

## File: sbin/netinit6
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/CP-CVI.lua
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: sbin/getty
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/mdev
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/DahuaExec
**Ports**: 1, 15, 2, 3, 4, 5, 6, 8, 80
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: lib/libpthread.so.0
**Ports**: 1, 2, 20, 2006, 22, 3, 30, 33, 4, 40, 404, 414, 42, 44, 47, 5, 6, 7, 8, 80, 81, 9
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: web/css/oem.css
**Ports**: 100, 13, 2, 210, 333, 900, 999

## File: web/css/Intellent.css
**Ports**: 1, 100, 2, 2014, 210, 29, 3, 444, 50, 6, 60, 8, 999

## File: usr/bin/lua/ptz/PelcoP5.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 4, 5, 6, 7, 8

## File: usr/bin/lua/ptz/WV-CS950.lua
**Ports**: 1, 10, 100, 13, 14, 15, 16, 1610, 17, 2, 2007, 23, 3, 350, 4, 5, 6, 64, 7, 8, 9, 96, 99

## File: sbin/modprobe
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/platformHtm/GAYS.htm
**Ports**: 1, 10, 2, 3, 4, 5, 6

## File: web/js/loginEx.js
**Ports**: 1, 120, 128, 192, 200, 255, 3, 300, 3600, 4, 60, 63, 8

## File: usr/lib/lib.7z.extracted/0/lib/option.ko
**Ports**: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_base.ko
**Ports**: 1, 10, 11, 128, 13, 1554, 1608, 18, 19, 2, 2017, 3, 31, 326, 33, 4, 40, 400, 41, 44, 45, 495, 5, 57, 6, 7, 72, 8, 80, 82, 9, 95

## File: web/js/Grid.js
**Ports**: 1, 4

## File: usr/data/Data/cursors/hand.cur
**Ports**: 9

## File: usr/data/Data/cursors/wait.cur
**Ports**: 8

## File: web/css/index.css
**Ports**: 100, 1000, 10000, 45, 50, 55, 60, 8, 80

## File: sbin/ifup
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/net3g
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin
**Ports**: 1, 10, 100, 101, 1010, 10101, 10104, 10107, 102, 10245, 10286, 103, 1030, 10310, 10327, 104, 10430, 10700, 1071, 10711, 10712, 10715, 108, 11, 110, 111, 1142, 115, 11611, 11657, 11673, 11694, 117, 11731, 118, 1181, 119, 12, 120, 12084, 121, 12103, 12134, 1215, 12152, 1230, 1232, 12357, 12363, 124, 12611, 12781, 128, 12809, 12827, 12845, 12857, 12869, 12882, 12913, 12958, 12985, 12987, 13, 1300, 13020, 13029, 13033, 13045, 13051, 13057, 13064, 13091, 131, 13189, 13197, 132, 133, 13321, 13353, 13370, 134, 13464, 135, 13505, 13575, 13582, 136, 14, 140, 141, 142, 14622, 14680, 148, 14871, 14903, 14947, 15, 15007, 1505, 1509, 15101, 1515, 15335, 15402, 15550, 15691, 157, 15780, 158, 15941, 15966, 16, 16039, 16048, 16089, 16096, 16097, 16098, 16100, 16121, 16140, 16155, 16176, 16197, 16221, 16240, 16251, 16260, 16341, 164, 16410, 16416, 16531, 16537, 16551, 16553, 16723, 16740, 16757, 16761, 16772, 16779, 16800, 16820, 16823, 16845, 16863, 16896, 169, 16914, 16934, 16951, 16961, 16965, 17, 170, 17009, 17042, 17044, 17060, 17083, 17166, 17176, 17198, 17224, 17241, 17275, 17302, 17308, 17314, 17315, 17326, 17361, 17381, 17390, 17405, 17413, 17487, 17534, 17563, 17663, 17667, 17744, 17764, 17772, 17773, 17774, 17776, 17821, 17839, 17852, 17864, 17873, 17874, 17875, 17965, 17988, 17990, 18, 180, 18003, 18008, 1803, 18057, 18070, 18083, 181, 18148, 18183, 1820, 1824, 18240, 18315, 18316, 18317, 18344, 18595, 18645, 18650, 18699, 18709, 18805, 18854, 18878, 18879, 18880, 18881, 18882, 18954, 19, 19009, 19020, 19060, 19079, 19082, 19095, 19132, 19139, 19152, 19157, 19164, 19165, 19211, 19212, 19217, 19219, 19246, 19276, 193, 19364, 19388, 19414, 19422, 19433, 19453, 19459, 19461, 19470, 19482, 19496, 19514, 19556, 19569, 19588, 19595, 19617, 19628, 19630, 19656, 19692, 19752, 19809, 19810, 19811, 19816, 19838, 19892, 19897, 19938, 19942, 19952, 1996, 19964, 19969, 19982, 19990, 2, 20, 200, 2000, 2001, 2003, 2005, 2006, 2009, 2012, 2017, 202, 20202, 204, 2048, 205, 207, 21, 2100, 2104, 2105, 2111, 215, 2151, 22, 222, 2222, 22242, 23, 2300, 235, 23995, 24, 240, 242, 244, 248, 249, 25, 255, 256, 2560, 257, 258, 26, 2600, 2608, 266, 27, 270, 28, 280, 282, 28242, 288, 29, 3, 30, 300, 3000, 30016, 30021, 30034, 30035, 30036, 30040, 302, 30211, 30223, 30241, 30252, 30260, 303, 30300, 30327, 304, 30432, 30454, 30481, 305, 30565, 30595, 30607, 30629, 30640, 30642, 30643, 30648, 30651, 30675, 30738, 30739, 30775, 30805, 30806, 30817, 30840, 30851, 30940, 30942, 30969, 30980, 30981, 31, 31088, 3110, 31160, 31161, 31214, 31275, 31289, 313, 31315, 31322, 31323, 31413, 31618, 31681, 31825, 32, 3200, 32124, 32129, 32154, 32159, 32186, 32213, 3226, 32261, 323, 324, 32457, 32465, 3250, 32637, 32681, 32773, 3280, 32839, 32842, 32888, 33, 330, 33191, 332, 33222, 33223, 33239, 33249, 33254, 33273, 33282, 333, 33302, 33307, 33312, 33317, 3333, 33330, 33338, 33408, 33519, 33520, 33522, 33543, 33626, 33720, 33724, 33779, 3380, 33875, 3390, 34, 340, 3404, 34108, 34110, 343, 345, 34573, 34574, 34597, 35, 35028, 35029, 35067, 35078, 35082, 35207, 35224, 35225, 35226, 35245, 35265, 35292, 35365, 35396, 35420, 35450, 35516, 35547, 35594, 356, 35678, 357, 35750, 35856, 35860, 35869, 35888, 36, 360, 3600, 36026, 3605, 36112, 36145, 36264, 36301, 36304, 36351, 36465, 36609, 36669, 36670, 36671, 36672, 36813, 36814, 36911, 37, 37543, 37552, 37561, 37575, 37611, 37648, 37704, 37714, 37765, 37815, 37933, 38, 380, 38032, 38033, 38121, 38137, 38207, 38218, 38228, 38245, 383, 38382, 38425, 38426, 38427, 38436, 38464, 38469, 38474, 38479, 38519, 38529, 38544, 38568, 38581, 38582, 38682, 38701, 38708, 38818, 38851, 38864, 38894, 38994, 38995, 38996, 39, 39014, 39110, 39136, 39137, 39164, 3925, 3926, 39273, 39277, 39308, 39324, 39349, 39397, 39405, 3941, 39412, 39463, 39522, 39639, 39647, 39685, 39688, 39765, 39793, 39800, 39801, 39805, 39811, 39814, 39842, 39903, 39938, 39944, 4, 40, 400, 4000, 401, 40137, 40194, 4020, 40211, 4027, 403, 404, 4040, 40404, 40407, 40411, 40463, 40467, 40509, 40516, 40662, 40671, 40676, 40700, 40704, 40759, 408, 4080, 40808, 409, 4096, 40998, 41, 410, 4100, 411, 4110, 41102, 41103, 41175, 41184, 41191, 4120, 41236, 41317, 414, 4141, 41506, 41586, 418, 41866, 41883, 41897, 41961, 41988, 42, 420, 42025, 42075, 42086, 42094, 42260, 42261, 42265, 42266, 42368, 42375, 42456, 42472, 42561, 4269, 42825, 42978, 43, 43084, 43089, 43094, 431, 43327, 43338, 43349, 43383, 43392, 43416, 43459, 43500, 43502, 43503, 43542, 43576, 43594, 44, 440, 4404, 44044, 44176, 443, 444, 4444, 44844, 44863, 44904, 45, 451, 452, 456, 45670, 46, 461, 47, 477, 48, 480, 4814, 49, 4920, 5, 50, 500, 5000, 505, 51, 512, 52, 5200, 523, 53, 535, 54, 541, 54555, 55, 555, 5555, 55555, 5585, 56, 561, 5614, 5615, 5616, 5617, 5632, 5633, 5634, 5635, 5687, 5688, 569, 57, 5719, 5781, 58, 5892, 59, 5924, 596, 6, 60, 600, 6070, 61, 6119, 61200, 6131, 62, 6233, 6234, 6288, 63, 64, 640, 6404, 646, 65, 6538, 6586, 6588, 6594, 66, 6617, 666, 6666, 67, 6705, 68, 6840, 685, 6879, 6898, 69, 6926, 7, 70, 706, 708, 71, 7132, 7175, 72, 721, 7280, 7283, 73, 731, 7325, 737, 74, 7425, 7477, 75, 7523, 755, 76, 7624, 7642, 765, 77, 7704, 777, 7777, 78, 780, 781, 7851, 7868, 789, 79, 7951, 797, 8, 80, 800, 8000, 8001, 801, 8012, 8019, 802, 803, 8031, 8034, 804, 8040, 805, 808, 8080, 809, 81, 8100, 811, 814, 818, 82, 820, 8296, 83, 8305, 84, 840, 841, 847, 8475, 848, 85, 86, 8610, 866, 8696, 87, 870, 876, 88, 880, 8818, 884, 888, 8888, 89, 9, 90, 900, 901, 909, 91, 9120, 92, 921, 93, 930, 94, 940, 9462, 949, 95, 9546, 96, 960, 9660, 97, 9721, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: DES, RSA, SSL

## File: usr/bin/lua/ptz/WV-CS850II.lua
**Ports**: 1, 10, 100, 13, 14, 15, 16, 1610, 17, 2, 200, 3, 4, 5, 6, 64, 7, 8, 9, 99

## File: bin/ifenslave
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/grep
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/css/reset.css
**Ports**: 10, 100, 2013, 400, 5, 8

## File: bin/nice
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoASCII.lua
**Ports**: 1, 10, 2, 200, 256, 3, 4, 5, 6, 63, 64, 99, 9999

## File: bin/cp
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/makedevs
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/hostname
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/Data_Signature
**Ports**: 4, 6, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vpss.ko
**Ports**: 1, 10, 100, 1000, 11, 12, 1280, 13, 14, 1418, 16, 17, 177, 180, 19, 2, 20, 200, 2017, 202, 24, 25, 255, 26, 270, 28, 3, 31, 32, 33, 333, 35, 4, 40, 400, 401, 4096, 41, 42, 431, 433, 44, 45, 4585, 46, 48, 49, 5, 50, 54, 545, 55, 550, 58, 6, 60, 61, 611, 63, 65, 66, 661, 7, 70, 74, 77, 7707, 771, 776, 8, 80, 801, 81, 82, 83, 833, 84, 840, 846, 85, 8554, 86, 8606, 866, 87, 88, 881, 888, 89, 8906, 895, 9, 90, 96, 966, 999
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/js/recordplan.js
**Ports**: 1, 100, 150, 2, 20, 24, 3, 30, 4, 40, 43200, 5, 6, 60, 7, 70, 8, 80

## File: web/html/localconfig.htm
**Ports**: 1, 10, 11, 12, 13, 2, 2012, 24, 3, 30, 4, 45, 5, 6, 60, 63, 64, 65535, 7, 8, 9, 998

## File: web/js/remotestorage.js
**Ports**: 1, 10, 16, 19, 2, 3, 31, 32, 5, 60, 600, 65535, 7

## File: usr/etc/load_modules.sh
**Ports**: 2, 777

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_region.ko
**Ports**: 1, 10, 111, 15, 16, 2, 20, 2017, 24, 3, 32, 36, 4, 40, 41, 42, 45, 47, 48, 5, 50, 52, 55, 57, 6, 64, 65, 67, 7, 70, 73, 75, 8, 80, 81, 82, 84, 85, 88, 9, 96

## File: web/js/chanldiscgroup.js
**Ports**: 1, 100, 1500, 2, 250, 4, 400, 50, 55, 8
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/js/recordcontrol.js
**Ports**: 1, 16, 2, 24, 25, 32, 50, 512, 600

## File: bin/mv
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/com/ParseKLPOSStr.lua
**Ports**: 1, 10, 128, 16, 2, 2000, 3, 32, 7, 8

## File: web/js/IVSFaceSearch.js
**Ports**: 1, 100, 12, 1969, 2, 2049, 23, 31, 3600, 40, 59, 60, 8

## File: web/js/videomatrix.js
**Ports**: 1, 100, 1024, 12, 120, 150, 16, 2, 20, 200, 25, 3, 300, 32, 350, 36, 4, 5, 6, 8, 9

## File: bin/ash
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libc.so.0
**Ports**: 1, 10, 100, 1020, 105, 109, 11, 110, 111, 1111, 11111, 1121, 12, 1234, 124, 13, 133, 14, 141, 145, 15, 1535, 16, 17, 17641, 18, 186, 1872, 1873, 19, 1912, 1913, 1926, 1927, 1989, 1990, 2, 20, 202, 20212, 2033, 2078, 208, 21, 2133, 22, 222, 2222, 22222, 22223, 22224, 228, 23, 234, 2345, 24, 245, 246, 25, 256, 26, 263, 27, 27751, 28, 288, 29, 3, 30, 300, 303, 306, 31, 32, 320, 321, 33, 333, 3345, 33744, 34, 342, 344, 35, 36, 37, 376, 38, 39, 4, 40, 401, 4050, 408, 4080, 41, 4151, 42, 4289, 43, 432, 4353, 44, 44355, 444, 4467, 45, 46, 47, 48, 49, 498, 5, 50, 51, 51305, 52, 5289, 53, 54, 543, 55, 551, 56, 5666, 5678, 56789, 57, 571, 572, 58, 588, 59, 5945, 6, 60, 600, 61, 613, 62, 620, 6272, 63, 64, 65, 66, 666, 67, 68, 682, 683, 69, 699, 7, 70, 701, 703, 71, 72, 73, 7383, 74, 7407, 75, 757, 76, 769, 77, 777, 78, 785, 789, 79, 793, 794, 8, 80, 800, 807, 808, 8080, 81, 813, 815, 818, 82, 83, 831, 84, 848, 85, 86, 87, 88, 8859, 89, 899, 9, 90, 900, 91, 92, 93, 94, 95, 96, 964, 97, 98, 99, 999, 9999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: usr/lib/lib.7z.extracted/0/lib/hifb.ko
**Ports**: 1, 10, 13, 140, 16, 1620, 18, 180, 19, 2, 2017, 255, 26, 27, 3, 32, 39, 4, 40, 4080, 41, 45, 46, 48, 49, 5, 50, 51, 6, 7, 720, 8, 80, 800, 804, 808, 81, 810, 8100, 84, 85, 86, 88, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: DES

## File: web/html/audioset.htm
**Ports**: 1, 2, 24, 3, 600

## File: usr/sbin/usb_modeswitch
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoD_Tour.lua
**Ports**: 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: usr/sbin/.dec.sh
**Ports**: 1, 2, 8

## File: sbin/fdisk
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/Wireless/RT2870STA/RT2870STA.dat
**Ports**: 1, 100, 2346, 2347, 3, 33, 4, 5, 64, 7, 70

## File: lib/libhive_RES.so
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 2, 208, 23, 24, 26, 27, 28, 3, 30, 37, 4, 40, 43, 45, 46, 48, 49, 5, 50, 51, 55, 56, 57, 6, 62, 66, 67, 68, 69, 7, 73, 74, 75, 76, 77, 78, 79, 8, 80, 84, 85, 9, 92, 93, 94, 95

## File: sbin/pppoe
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/update.htm
**Ports**: 1
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vou.ko
**Ports**: 1, 10, 100, 1000, 101, 10141, 1080, 11, 112, 12, 1280, 13, 14, 15, 16, 18, 181, 19, 1920, 2, 20, 200, 2017, 21, 22, 222, 24, 25, 255, 28, 3, 30, 32, 33, 34, 39, 4, 40, 400, 4000, 408, 41, 42, 420, 422, 43, 44, 47, 48, 49, 5, 50, 54, 57, 576, 59, 6, 60, 64, 7, 70, 71, 720, 73, 75, 8, 80, 804, 808, 81, 82, 84, 85, 86, 867, 87, 88, 9, 90, 91, 95, 96
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/html/alarmlink.htm
**Ports**: 1, 10, 2, 3, 300, 4, 5, 6, 60, 600, 65535, 7, 8, 9

## File: lib/libhive_common.so
**Ports**: 1, 1073, 16, 1602, 2, 26, 3, 4, 400, 404, 5, 6, 7, 8, 80, 8808, 8813, 9, 93
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_hdmi.ko
**Ports**: 1, 10, 1024, 11, 11025, 1152, 12000, 1280, 13, 14, 16, 16000, 17, 176, 18, 19, 192, 2, 20, 2017, 21, 22050, 23, 24, 24000, 3, 30, 32, 32000, 33, 38, 4, 40, 400, 408, 41, 42, 43, 44, 44100, 45, 46, 47, 48, 480, 48000, 49, 5, 50, 51, 52, 6, 60, 600, 601, 62, 624, 63, 640, 67, 7, 709, 71, 720, 73, 768, 8, 80, 800, 8000, 8002, 804, 81, 819, 82, 83, 832, 84, 85, 870, 88, 89, 9, 90, 91, 96

## File: lib/libpthread-0.9.33.2.so
**Ports**: 1, 2, 20, 2006, 22, 3, 30, 33, 4, 40, 404, 414, 42, 44, 47, 5, 6, 7, 8, 80, 81, 9
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: etc/udev/rules.d/97-bluetooth-serial.rules
**Ports**: 504, 620

## File: bin/iptunnel
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/mkdir
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi_rtc.ko
**Ports**: 1, 10, 2, 3, 4, 5, 7, 8, 88, 9

## File: sbin/ifconfig
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/SAE.lua
**Ports**: 1, 10, 11, 12, 127, 16, 1610, 2, 200, 23, 254, 256, 3, 4, 5, 6, 7, 8, 8192, 9

## File: etc/udev/rules.d/device-mapper.rules
**Ports**: 600, 9

## File: web/html/version.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_chnl.ko
**Ports**: 1, 10, 11, 13, 18, 19, 2, 2017, 23, 3, 33, 4, 40, 46, 5, 6, 7, 8, 80, 81, 84, 85, 86, 9

## File: lib/libm.so.0
**Ports**: 1, 101, 11, 12, 135, 14, 18, 182, 2, 208, 22, 23, 24, 3, 30, 320, 33333, 375, 4, 40, 42, 43, 44, 45, 46, 47, 5, 50, 51, 53, 55, 56, 6, 60, 62, 7, 75, 8, 80, 81, 82, 83, 8353, 84, 85, 87, 9

## File: web/js/PlayControl.js
**Ports**: 1, 4

## File: lib/libthread_db-0.9.33.2.so
**Ports**: 1, 10, 11, 2, 3, 33, 4, 40, 41, 411, 5, 6, 7, 8, 80, 9

## File: web/html/connetcfg.htm
**Ports**: 1, 1025, 128, 65535

## File: web/html/tcpip_ipc.htm
**Ports**: 4, 64

## File: web/webplugin.exe
**Ports**: 1, 10, 1000, 11, 12, 124, 13, 136, 138, 139, 14, 15, 1546, 16, 17, 175, 18, 185, 19, 195, 2, 20, 200, 2006, 21, 22, 23, 233, 24, 25, 251, 26, 263, 27, 2713, 273, 28, 29, 3, 30, 31, 3130, 32, 328, 33, 333, 338, 34, 35, 36, 3652, 37, 38, 388, 39, 392, 394, 4, 40, 402, 41, 411, 42, 421, 429, 43, 44, 45, 451, 46, 47, 471, 472, 48, 483, 49, 5, 50, 51, 52, 53, 54, 55, 56, 5670, 57, 58, 581, 59, 590, 5925, 6, 60, 61, 62, 63, 64, 65, 66, 67, 675, 68, 69, 690, 7, 70, 709, 71, 717, 72, 73, 736, 7364, 74, 741, 75, 76, 77, 774, 78, 781, 786, 79, 8, 80, 81, 816, 82, 83, 84, 85, 857, 86, 87, 877, 88, 89, 9, 90, 91, 92, 927, 93, 94, 944, 947, 95, 950, 96, 961, 965, 97, 978, 98, 99, 991, 9986
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/top
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/ptzCtrl.js
**Ports**: 1, 10

## File: usr/bin/lua/ptz/SUNKWANG.lua
**Ports**: 10, 11, 12, 13, 14, 15, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: usr/bin/lua/PTZCtrl.lua
**Ports**: 1, 10, 14, 15, 16, 1992, 2, 2005, 2006, 22, 2416, 256, 3, 31, 32, 33, 4, 43, 5, 6, 63, 64, 9

## File: sbin/lsmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/free
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/3gnetcfg.js
**Ports**: 1, 12, 16, 2, 31, 32, 5, 65535, 777, 98, 99

## File: usr/bin/lua/ptz/Videon-X.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: sbin/chat
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/defaultcfg.js
**Ports**: 1, 100, 108, 168, 192, 2, 20, 200, 30, 300, 4

## File: web/html/recordcontrol.htm
**Ports**: 1

## File: lib/libutil.so.0
**Ports**: 1, 10, 2, 4, 5, 7, 8
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/echo
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/chnltype.js
**Ports**: 1, 1080, 1920, 2

## File: web/js/alarmindex.js
**Ports**: 1, 100, 11, 19, 2, 20, 3, 30

## File: web/js/chnlname.js
**Ports**: 1, 10, 2, 3, 31, 63

## File: web/js/publicFunc.js
**Ports**: 1, 10, 100, 10001, 102, 1024, 10240, 1050, 1080, 11, 110, 12, 120, 1200, 1216, 12288, 123, 128, 1280, 13, 1366, 14, 140, 1400, 1408, 14336, 144, 1440, 149, 15, 150, 1536, 16, 160, 1600, 16384, 17, 176, 1792, 18, 18432, 1872, 19, 190, 1900, 192, 1920, 198, 1980, 2, 20, 200, 2037, 2048, 20480, 21, 215, 2160, 22, 223, 224, 22528, 23, 24, 240, 24576, 2472, 25, 255, 256, 2560, 26, 27, 28, 288, 29, 3, 30, 300, 31, 32, 320, 321, 325, 3296, 330, 337, 34, 352, 360, 3600, 37, 3744, 37810, 38, 3800, 384, 3840, 39, 39999, 4, 40, 400, 401, 408, 4096, 448, 450, 48, 480, 5, 50, 500, 5050, 512, 54, 576, 59, 592, 6, 60, 600, 601, 6144, 64, 640, 65, 65535, 68, 69, 7, 70, 704, 720, 768, 8, 80, 800, 8192, 85, 854, 896, 9, 90, 96, 960, 9999

## File: usr/bin/lua/ptz/RM110.lua
**Ports**: 128, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: web/webVersion.js
**Ports**: 2, 3, 7

## File: bin/rm
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/killall5
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/insmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/system.js
**Ports**: 1, 2, 6, 9

## File: web/css/alarmindex.css
**Ports**: 100, 30, 65

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_ive.ko
**Ports**: 1, 10, 11, 11111, 118, 13, 15, 16, 18, 19, 191, 2, 2017, 27, 3, 30, 33, 37, 38, 4, 40, 41, 43, 45, 46, 48, 49, 4900, 5, 59, 6, 60, 67, 68, 7, 8, 80, 800, 81, 810, 83, 84, 85, 89, 9, 90, 900
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/osa.ko
**Ports**: 1, 10, 11, 2, 2017, 22, 3, 31, 32, 4, 40, 43, 47, 5, 50, 6, 7, 8, 80, 81, 83, 88, 888, 9
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: init
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/hush
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/audiocfg.htm
**Ports**: 1999

## File: usr/bin/lua/ptz/LG.lua
**Ports**: 1, 10, 11, 12, 128, 13, 14, 15, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: usr/lib/lib.7z.extracted/0/lib/i2c_read
**Ports**: 1, 2, 3, 4, 5, 6, 7, 8, 80, 8808, 8813, 9

## File: web/html/wificfg.htm
**Ports**: 1, 128, 2, 3, 4

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_aenc.ko
**Ports**: 1, 10, 12, 13, 16, 18, 19, 2, 2017, 3, 32, 4, 40, 44, 46, 5, 50, 6, 7, 8, 80, 84, 87, 88, 89, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_jpegd.ko
**Ports**: 1, 10, 13, 18, 19, 2, 2017, 3, 4, 5, 6, 7, 8, 9

## File: usr/bin/lua/ptz/CP-CVI2.0.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 7, 80

## File: usr/bin/lua/ptz/ADMatrix.lua
**Ports**: 1, 10, 13, 16, 1610, 2, 2006, 256, 3, 4, 5, 6, 66, 7

## File: usr/bin/lua/ptz/DH-CC440.lua
**Ports**: 1, 16, 1610, 200, 4, 5, 8, 9

## File: sbin/rmmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/remotestorage.htm
**Ports**: 1, 2, 31, 32, 65535

## File: sbin/lsusb
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/ptzconfig.js
**Ports**: 1, 1200, 19200, 2, 2400, 255, 3, 38400, 4, 4800, 5, 57600, 9600, 9750, 999, 9999

## File: web/Component/level.js
**Ports**: 1, 3

## File: etc/passwd
**Ports**: 1

## File: usr/lib/lib.7z.extracted/0/lib/mmz.ko
**Ports**: 1, 10, 2, 3, 4, 40, 5, 6, 7, 8, 80, 88, 880, 9

## File: web/html/IVSConfig.htm
**Ports**: 10, 3, 300, 6, 600

## File: etc/init.d/S81toe
**Ports**: 100, 200, 8192

## File: usr/data/Data/FontSmallEn.bin
**Ports**: 2, 4, 8

## File: web/js/deviceInitial.js
**Ports**: 1, 10, 12, 17, 2, 20, 3, 31, 6, 63

## File: bin/dnsdomainname
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/Data_Signature
**Ports**: 60

## File: lib/libcrypt.so.0
**Ports**: 1, 2, 3, 4, 44, 5, 6, 7, 8, 80, 9, 91
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/umount
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/Yaan.lua
**Ports**: 1, 10, 11, 12, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: web/js/encodecfg.js
**Ports**: 1, 10, 100, 1024, 10240, 1080, 12, 12288, 125, 128, 1280, 1429, 14336, 15, 1536, 16, 160, 16384, 1667, 1792, 18432, 192, 1920, 2, 20, 200, 2048, 20480, 224, 22528, 230, 24, 240, 24576, 25, 255, 256, 2560, 264, 288, 3, 30, 3072, 32, 320, 33, 3333, 352, 3600, 374, 375, 384, 4, 4096, 448, 45, 450, 48, 5, 50, 500, 512, 5279, 6, 6144, 625, 63, 6370, 6371, 6372, 64, 640, 7, 720, 768, 8, 80, 8165, 8170, 8192, 896, 96, 960

## File: sbin/pppd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/SigFileList
**Ports**: 1, 5, 717, 9750

## File: etc/init.d/S80network
**Ports**: 1, 127, 2

## File: etc/udev/rules.d/99-fuse.rules
**Ports**: 666

## File: lib/libstdc++.so.6
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 2013, 25, 3, 30, 31, 36, 37, 38, 4, 40, 403, 404, 405, 4080, 41, 410, 43, 440, 47, 48, 489, 49, 5, 500, 54, 540, 56, 6, 60, 67, 68, 69, 7, 8, 80, 803, 804, 808, 81, 83, 84, 85, 88, 89, 9, 90, 904, 91, 96
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: TLS

## File: web/js/automaintain.js
**Ports**: 1, 12, 2, 24, 400, 5, 500, 60, 65535, 7

## File: usr/bin/lua/ptz/Banknote.lua
**Ports**: 1, 2, 200, 3, 5, 6, 7, 8

## File: usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vga_hdmi_spi.sh
**Ports**: 1, 10, 32

## File: sbin/pppoe-start
**Ports**: 1412, 80

## File: web/html/logmanage.htm
**Ports**: 1, 64
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/js/Calendar.js
**Ports**: 1, 100, 11, 12, 15, 2, 2037, 28, 29, 3, 30, 31, 32, 4, 400, 42, 6, 9

## File: bin/[[
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/ptzconfig.htm
**Ports**: 1, 1200, 19200, 2, 2400, 38400, 4800, 5, 57600, 6, 7, 8, 9600

## File: web/html/infoindex.htm
**Ports**: 1, 1999, 2, 6, 7, 8

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vfmw.ko
**Ports**: 1, 10, 11, 111, 12, 13, 14, 141, 145, 16, 18, 1892, 19, 2, 20, 2017, 219, 22, 220, 222, 2222, 23, 24, 240, 25, 26, 263, 27, 28, 291, 3, 303, 32, 322, 33, 35, 4, 40, 4000, 409, 41, 42, 43, 44, 45, 458, 46, 47, 48, 5, 5000, 532, 55, 556, 587, 6, 65, 65535, 7, 76, 77, 8, 80, 800, 81, 82, 84, 86, 88, 89, 9, 90, 900, 92, 95

## File: web/jsBase/lib/base64.js
**Ports**: 1, 12, 127, 128, 15, 191, 192, 2, 2048, 224, 3, 31, 4, 6, 63, 64, 9
### Encryption/Encoding: Base64

## File: web/css/infoindex.css
**Ports**: 100, 10001, 50, 8, 80

## File: web/js/ATMConfig.js
**Ports**: 1, 1200, 1440, 15, 150, 19200, 2, 20, 2400, 3, 38400, 4, 4800, 5, 57600, 6, 65535, 70, 8, 9600

## File: web/html/broadcast.htm
**Ports**: 1025, 224, 239, 255, 65000

## File: web/js/alarmcenter.js
**Ports**: 1, 12, 2, 24, 255, 3, 4, 5, 6, 65535, 7, 8

## File: web/js/previewindex.js
**Ports**: 1, 10, 100, 11, 12, 120, 125, 127, 128, 13, 14, 16, 17, 19, 190, 2, 20, 200, 24, 25, 287, 3, 310, 32, 36, 37, 4, 480, 5, 50, 500, 51, 534, 6, 60, 64, 7, 77, 78, 8, 80, 85, 9
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: Base64

## File: usr/bin/ssl/pwdreset.pem
### Encryption/Encoding: RSA

## File: lib/librt-0.9.33.2.so
**Ports**: 1, 2, 4, 40, 5, 6, 7, 8, 80, 9

## File: usr/bin/lua/utils.lua
**Ports**: 1, 12, 16, 1992, 20, 2005, 24, 24576, 3, 8, 9

## File: usr/sbin/3gconfig
**Ports**: 1, 11, 1500, 98

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_ai.ko
**Ports**: 1, 10, 100, 10240, 13, 18, 19, 2, 200, 2017, 250, 3, 30, 350, 4, 40, 41, 43, 44, 46, 5, 500, 55, 6, 7, 71, 73, 8, 80, 800, 81, 83, 84, 88, 9, 99

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_venc.ko
**Ports**: 1, 10, 100, 13, 15, 16, 17, 18, 19, 2, 20, 2017, 21, 25, 264, 265, 3, 35, 38, 4, 40, 400, 41, 418, 42, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 54, 55, 6, 60, 61, 62, 65, 66, 67, 7, 75, 777, 787, 8, 80, 81, 82, 820, 83, 84, 840, 845, 85, 86, 860, 864, 87, 88, 89, 9, 95
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: bin/mktemp
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/jsCore/common.js
**Ports**: 1, 10, 100, 1024, 11, 12, 12345, 128, 1280, 130, 149, 150, 1536, 160, 1792, 192, 2, 20, 2048, 224, 24, 256, 28, 29, 3, 30, 31, 32, 320, 37, 384, 39, 4, 40, 400, 448, 48, 50, 512, 6, 64, 640, 7, 70, 768, 80, 8192, 896, 9, 96

## File: bin/uname
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/localstorage.js
**Ports**: 1, 10, 100, 1024, 1500, 2, 200, 3, 30, 32, 350, 5, 60

## File: web/html/ddnsconfig.htm
**Ports**: 1, 1092, 5, 60, 65535

## File: sbin/upgraded
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/SANTACHI.lua
**Ports**: 1, 10, 16, 1610, 18, 2, 200, 23, 24, 3, 4, 45, 6, 7, 8, 9, 99

## File: web/html/playbackindex.htm
**Ports**: 1, 10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 192, 2, 20, 2012, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 32, 4, 5, 51, 55, 59, 6, 64, 7, 8, 9

## File: etc/udev/udev.conf
**Ports**: 3

## File: web/js/audiocfg.js
**Ports**: 1, 10

## File: sbin/3gpp
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/devmem
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_viu.ko
**Ports**: 1, 10, 11, 1120, 12, 13, 14181, 15, 16, 18, 180, 19, 2, 2017, 22, 26, 270, 28000, 3, 30, 32, 34, 4, 40, 4004, 404, 4096, 41, 42, 43, 44, 444, 45, 46, 47, 4787, 48, 484, 49, 5, 50, 51, 54, 58, 5878, 59, 6, 600, 68, 69, 7, 71, 747, 78, 8, 80, 8000, 81, 828, 844, 86, 88, 884, 89, 9, 90, 99

## File: web/js/upnpconfig.js
**Ports**: 1, 2, 30, 4, 5, 65535

## File: web/Component/chnlGroup.js
**Ports**: 1, 2

## File: usr/bin/lua/ptz/Mercer.lua
**Ports**: 1, 10, 100, 1000, 16, 1610, 2, 200, 3, 4, 5, 6, 8

## File: lib/ld-uClibc-0.9.33.2.so
**Ports**: 1, 12, 13, 2, 21, 3, 4, 40, 44, 5, 6, 7, 8, 80, 800, 81, 88, 9
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: TLS

## File: web/js/videodetect.js
**Ports**: 1, 10, 100, 10000, 120, 15, 16, 18, 2, 22, 24, 25, 255, 26, 3, 30, 300, 33, 350, 4, 451, 50, 500, 580, 600, 64, 7, 8, 9

## File: usr/bin/lua/ptz/DH-SD1.lua
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: sbin/halt
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/ft.js
**Ports**: 2017

## File: bin/less
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/encodecfg.htm
**Ports**: 1, 10, 100, 1024, 128, 1280, 1536, 160, 17, 1792, 192, 2, 2048, 224, 25, 255, 256, 3, 32, 320, 33, 35, 384, 4, 4096, 448, 48, 5, 500, 512, 6, 64, 640, 7, 768, 80, 896, 96

## File: web/html/diskerror.htm
**Ports**: 1, 10, 12, 2, 3, 300, 32, 4, 60, 600, 7

## File: bin/msh
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/Videon_P.lua
**Ports**: 1, 2, 200, 256, 4, 5, 6, 7, 8

## File: usr/bin/lua/ptz/PelcoP-HK.lua
**Ports**: 1, 128, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 8192

## File: web/platformHtm/GAYS.js
**Ports**: 1, 10, 128, 200, 24, 3000, 3600, 65535

## File: web/css/ui.css
**Ports**: 1, 10, 100, 1000, 10000, 111, 2, 2013, 210, 25, 4, 40, 47, 5, 50, 6, 60, 8, 80, 9, 9999

## File: usr/bin/lua/ptz/PELCOD-MING.lua
**Ports**: 14, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: usr/data/Data/Font.bin
**Ports**: 1, 10, 11, 113, 2, 3, 30, 33, 4, 5, 6, 7, 8, 80, 83, 88, 9, 90

## File: web/js/p2pset.js
**Ports**: 1, 2, 3, 4

## File: lib/libgcc_s.so.1
**Ports**: 1, 101, 13, 2, 208, 3, 320, 35, 36, 38, 4, 40, 404, 45, 5, 50, 51, 52, 55, 6, 63, 7, 8, 80, 83, 87, 9, 91
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: lib/libthread_db.so.1
**Ports**: 1, 10, 11, 2, 3, 33, 4, 40, 41, 411, 5, 6, 7, 8, 80, 9

## File: usr/bin/lua/ptz/DH-SD2.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 32, 4, 5, 6, 64, 7, 8, 8192

## File: bin/printenv
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PANASONIC.lua
**Ports**: 1, 10, 100, 16, 1610, 18, 2, 200, 23, 24, 3, 4, 6, 7, 8, 9, 96, 99

## File: web/Data_Signature
**Ports**: 3, 4, 5

## File: bin/iproute
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libdl.so.0
**Ports**: 1, 2, 3, 4, 40, 44, 5, 6, 7, 8, 80, 81
### Encryption/Encoding: TLS

## File: web/html/guiset.htm
**Ports**: 1, 10, 100, 1024, 11, 12, 120, 1280, 13, 14, 15, 16, 2, 20, 200, 3, 4, 5, 6, 7, 720, 768, 8, 9

## File: sbin/lspci
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/IVSConfig.js
**Ports**: 1, 10, 15, 150, 2, 25, 255, 3, 30, 300, 4, 5, 550, 6, 600, 8191

## File: web/css/skin.css
**Ports**: 100, 111, 2, 2013, 210, 333, 5, 7, 777, 8, 888, 999

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_adec.ko
**Ports**: 1, 10, 13, 18, 19, 2, 2017, 3, 4, 42, 46, 5, 6, 7, 8, 84, 9

## File: usr/data/Data/cursors/size1.cur
**Ports**: 8

## File: bin/cat
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hiuser.ko
**Ports**: 10, 3, 4, 6, 7, 8

## File: web/jsBase/lib/md5.js
**Ports**: 1, 10, 11, 12, 127, 128, 14, 15, 16, 17, 2, 20, 21, 22, 23, 24, 255, 28, 3, 32, 36, 4, 40, 44, 48, 5, 52, 56, 6, 60, 64, 7, 8, 9

## File: web/html/localstorage.htm
**Ports**: 1000, 10000

## File: usr/data/Data/cursors/arrow.cur
**Ports**: 8

## File: usr/data/ssl/privkey.pem
**Ports**: 5

## File: web/css/fn.css
**Ports**: 1, 10, 100, 11, 12, 13, 15, 17, 18, 19, 2, 20, 21, 25, 3, 30, 35, 40, 45, 5, 50, 55, 6, 60, 67, 7, 8, 9, 90, 96

## File: web/html/snmpconfig.htm
**Ports**: 1, 65535

## File: web/js/appAbility.js
**Ports**: 1, 10, 1024, 1080, 11, 1920, 2, 3, 300, 4, 480, 5, 576, 6, 60, 7, 8, 8192, 9, 960

## File: bin/iprule
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/sbin/nfs
**Ports**: 1, 10, 2, 213, 3, 6

## File: web/js/findPwd.js
**Ports**: 1, 10, 12, 168, 17, 192, 2, 3, 4, 442, 63, 8

## File: usr/bin/lua/compat-5.1.lua
**Ports**: 1, 12, 19, 2, 2004, 2005, 5, 7

## File: usr/bin/lua/ptz/Mercer-1.lua
**Ports**: 1, 10, 100, 1000, 16, 1610, 2, 200, 3, 4, 5, 6, 8

## File: web/js/alarmlink.js
**Ports**: 1, 10, 100, 16, 2, 255, 3, 300, 33, 350, 4, 5, 6, 60, 600, 64, 7, 8

## File: bin/du
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/profile
**Ports**: 1, 22
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/bin/Challenge
**Ports**: 1, 10, 100, 1000, 10000, 10005, 1001, 10038, 1004, 101, 1010, 1011, 1014, 10141, 1016, 10181, 102, 1024, 103, 104, 1048, 106, 10646, 107, 108, 1080, 1084, 109, 11, 110, 1100, 1101, 11040, 1108, 111, 1111, 11111, 1115, 1140, 11520, 11548, 118, 119, 12, 120, 1200, 1202, 121, 1212, 12186, 122, 123, 12357, 125, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1261, 1264, 1265, 1268, 127, 12728, 1276, 128, 1280, 129, 13, 130, 1300, 1305, 131, 1310, 1315, 13397, 134, 135, 1360, 1366, 1394, 14, 140, 1400, 1404, 14040, 1408, 141, 1410, 1414, 142, 144, 1440, 1451, 147, 148, 1483, 149, 15, 1500, 151, 1515, 152, 1536, 155, 15804, 16, 160, 1600, 163, 16383, 166, 168, 169, 17, 1701, 172, 176, 17958, 18, 180, 18000, 1801, 1808, 181, 182, 185, 186, 188, 189, 1892, 19, 190, 191, 192, 1920, 19200, 1944, 1968, 1969, 1970, 1972, 1973, 1978, 1980, 1981, 1983, 1984, 1985, 1987, 1988, 1989, 1990, 1992, 1994, 1995, 1996, 1997, 1998, 2, 20, 200, 2000, 20000, 2001, 2002, 2003, 2004, 2005, 2006, 20085, 2009, 201, 2010, 2011, 2012, 2014, 2015, 2016, 2017, 202, 2020, 2022, 203, 2030, 2031, 204, 2040, 2048, 206, 207, 208, 20820, 2099, 21, 210, 2105, 211, 2110, 21111, 2115, 21466, 21474, 215, 21518, 2155, 2160, 217, 2193, 22, 2200, 221, 222, 2222, 22222, 223, 224, 225, 226, 228, 23, 2302, 23022, 2303, 231, 2312, 232, 234, 23572, 239, 24, 240, 2400, 24040, 241, 242, 24383, 245, 248, 249, 25, 250, 251, 252, 2530, 254, 255, 256, 2560, 25834, 2592, 26, 261, 262, 2625, 263, 264, 265, 266, 27, 272, 277, 278, 28, 280, 2805, 28080, 281, 28147, 2815, 282, 2820, 2824, 2825, 283, 284, 286, 288, 29, 290, 292, 29340, 2941, 2959, 299, 3, 30, 300, 3000, 3002, 3003, 3004, 301, 302, 3020, 304, 305, 306, 307, 308, 3082, 30830, 309, 31, 310, 3105, 31080, 311, 3110, 3115, 312, 3120, 313, 3130, 3135, 3155, 317, 318, 31802, 32, 320, 3200, 3203, 32160, 32767, 33, 330, 3303, 332, 3322, 333, 3333, 334, 3370, 34, 340, 34080, 341, 3410, 343, 344, 348, 35, 351, 352, 354, 355, 36, 360, 3600, 362, 366, 3666, 368, 37, 3743, 3779, 38, 380, 3800, 381, 382, 3823, 383, 3830, 384, 3840, 38400, 386, 388, 39, 390, 392, 393, 4, 40, 400, 4000, 40000, 4004, 40040, 40080, 401, 4018, 4019, 402, 40200, 4024, 403, 404, 4040, 40404, 4041, 4048, 405, 406, 407, 4070, 408, 4080, 40800, 4085, 409, 41, 410, 4100, 4101, 411, 412, 4124, 413, 414, 4140, 4144, 415, 41571, 416, 41692, 417, 418, 4181, 419, 42, 420, 4200, 421, 422, 423, 4232, 424, 4242, 426, 4282, 429, 43, 430, 4300, 4322, 433, 434, 4340, 436, 438, 44, 440, 4400, 44025, 4404, 44040, 44080, 441, 44100, 442, 443, 444, 4444, 446, 448, 4481, 45, 450, 453, 454, 45678, 457, 458, 4585, 46, 460, 461, 464, 466, 467, 47, 474, 48, 480, 4800, 48000, 482, 4838, 484, 485, 49, 490, 49152, 494, 4980, 499, 5, 50, 500, 5000, 50000, 5001, 5003, 5004, 501, 5010, 5011, 5020, 503, 505, 506, 5060, 5061, 507, 5080, 5083, 5084, 509, 51, 510, 5100, 5101, 5105, 5115, 512, 514, 515, 5155, 518, 519, 52, 5200, 524, 53, 530, 5300, 531, 5320, 53493, 535, 538, 54, 540, 54040, 5408, 542, 543, 545, 546, 548, 55, 550, 552, 555, 5554, 56, 561, 5634, 564, 566, 5678, 56789, 569, 57, 570, 5708, 576, 57600, 577, 58, 580, 5805, 58080, 582, 583, 5898, 59, 592, 599, 6, 60, 600, 6000, 6003, 6004, 601, 602, 6020, 606, 6060, 607, 608, 6083, 6084, 61, 610, 6101, 616, 62, 620, 6252, 626, 627, 629, 63, 630, 631, 633, 636, 639, 64, 640, 6404, 64040, 6412, 642, 646, 65, 650, 653, 66, 660, 666, 6666, 668, 67, 673, 678, 679, 68, 680, 681, 682, 689, 69, 690, 698, 699, 7, 70, 700, 7000, 7001, 7002, 7004, 701, 7011, 703, 704, 705, 706, 7061, 7070, 708, 7080, 7082, 71, 711, 72, 720, 722, 726, 727, 729, 73, 730, 7303, 736, 74, 740, 747, 75, 750, 757, 76, 762, 765, 768, 77, 770, 771, 773, 774, 777, 778, 78, 780, 7808, 781, 784, 788, 789, 79, 794, 798, 8, 80, 800, 8000, 8004, 8008, 801, 802, 8020, 803, 804, 8040, 8041, 8048, 805, 8050, 806, 807, 808, 8080, 809, 81, 810, 8100, 8101, 811, 812, 813, 8130, 814, 8141, 818, 8180, 8185, 8188, 819, 8192, 82, 820, 8200, 8212, 8222, 824, 827, 828, 83, 830, 8300, 8303, 8360, 8365, 838, 839, 84, 840, 841, 843, 844, 848, 85, 850, 858, 8580, 86, 860, 8600, 866, 868, 8686, 87, 874, 878, 879, 88, 880, 8800, 8807, 8808, 881, 8818, 882, 8831, 8859, 886, 887, 888, 8890, 89, 890, 896, 898, 899, 9, 90, 900, 9000, 901, 902, 903, 904, 905, 906, 907, 908, 909, 91, 910, 911, 912, 9130, 918, 92, 920, 922, 9272, 9279, 9282, 929, 93, 930, 936, 939, 94, 940, 9401, 941, 942, 943, 949, 95, 950, 959, 96, 960, 9600, 963, 9640, 966, 9660, 969, 97, 974, 977, 9786, 979, 98, 980, 988, 9889, 99, 9969, 999, 9999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, DES, Hex, RSA, SSL, TLS

## File: usr/bin/lua/ptz/Pelco-9750.lua
**Ports**: 11, 16, 1610, 2, 250, 256, 3, 4, 5, 6, 7, 8, 9, 9750

## File: usr/lib/lib.7z.extracted/0/lib/load_hisimod.sh
**Ports**: 1, 10, 101, 1024, 11, 11200, 12152, 1536, 1920, 2, 2015, 2048, 2500, 256, 31, 35, 37, 38, 39, 4, 40, 4050, 41, 42, 43, 44, 45, 49, 51, 512, 52, 53, 55, 56, 58, 59, 6, 60, 61, 62, 63, 67, 68, 7200, 78, 9120, 93, 95, 96, 97
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/bin/lua/ptz/PELCOD-S.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: etc/protocols
**Ports**: 1, 103, 108, 112, 115, 12, 124, 132, 133, 17, 2, 20, 22, 25, 27, 29, 3, 36, 37, 38, 4, 41, 43, 44, 45, 46, 47, 5, 50, 51, 57, 58, 59, 6, 60, 73, 8, 81, 88, 89, 9, 93, 94, 97, 98, 99

## File: web/js/faceplayback.js
**Ports**: 1, 10, 100, 12, 120, 150, 16, 2, 20, 200, 210, 23, 230, 3, 35, 350, 4, 5, 50, 500, 59, 6, 655, 7, 8, 83, 9

## File: usr/bin/lua/ptz/EPTZ.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: usr/bin/lua/ptz/CATU.lua
**Ports**: 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_rc.ko
**Ports**: 1, 10, 100, 12, 13, 18, 180, 19, 2, 2017, 255, 3, 30, 38, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 54, 6, 7, 70, 8, 80, 81, 82, 83, 84, 85, 86, 868, 87, 9

## File: usr/bin/lua/ptz/PelcoD.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: sbin/poweroff
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/jsBase/lib/qrcode.js
**Ports**: 1, 10, 100, 102, 104, 106, 108, 11, 110, 112, 114, 116, 118, 12, 121, 122, 126, 128, 13, 130, 132, 1335, 134, 136, 138, 14, 142, 146, 15, 150, 154, 158, 16, 162, 166, 17, 170, 18, 19, 2, 20, 21522, 22, 236, 24, 25, 255, 256, 26, 27, 28, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 4095, 41, 42, 43, 44, 46, 47, 48, 49, 5, 50, 52, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 65, 66, 67, 68, 69, 7, 70, 72, 74, 76, 78, 7973, 8, 80, 82, 84, 86, 87, 9, 90, 94, 97, 98

## File: sbin/route
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PHILIPS.lua
**Ports**: 1, 16384, 2, 200, 3, 4, 5, 6, 7, 8

## File: usr/bin/lua/ptz/PelcoP1.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: web/js/index.js
**Ports**: 1, 10, 100, 102, 1100, 1263, 16, 198, 2, 20, 2000, 208, 220, 224, 24, 25, 255, 28, 3, 30, 300, 33, 35, 37, 4, 40, 400, 42, 5, 50, 500, 56, 6, 67, 680, 70, 745, 8, 80, 85, 89, 9
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: Base64

## File: web/html/imageprty.htm
**Ports**: 1, 100, 1000, 15, 2, 20, 3

## File: sbin/ifdown
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoD1.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: usr/bin/lua/ptz/PelcoP.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 5, 6, 8

## File: usr/bin/lua/ptz/Videon_D.lua
**Ports**: 1, 10, 11, 12, 127, 128, 13, 14, 2, 200, 256, 3, 4, 40, 5, 6, 7, 8192, 9

## File: web/index.htm
**Ports**: 1, 100, 11, 110, 13, 2, 200, 2017, 3, 32, 4, 6, 63, 7, 8, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/html/defaultcfg.htm
**Ports**: 1, 2, 3, 4, 5
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/html/serialconfig.htm
**Ports**: 1, 1200, 19200, 2, 2400, 38400, 4800, 5, 57600, 6, 7, 8, 9600

## File: sbin/depmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/recordplan.htm
**Ports**: 1, 10, 100, 12, 14, 16, 18, 2, 20, 22, 24, 3, 30, 4, 5, 6, 8

## File: usr/bin/lua/ATMHead.lua
**Ports**: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/bin/lua/init.lua
**Ports**: 1, 10, 1024, 11, 12, 128, 13, 14, 15, 16, 16384, 17, 18, 19, 2, 20, 2005, 2006, 2048, 21, 22, 23, 24, 25, 255, 256, 26, 27, 28, 29, 3, 30, 31, 32, 32768, 33, 34, 35, 36, 4, 4096, 5, 512, 5264, 58, 59, 6, 61, 62, 64, 7, 8, 8192, 9

## File: web/html/emailconfig.htm
**Ports**: 1, 1440, 2, 3, 30, 3600, 65535
### Encryption/Encoding: SSL, TLS

## File: web/SigFileList
**Ports**: 2
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/js/blackwhite.js
**Ports**: 1, 190, 2, 200, 64

## File: bin/touch
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ATMCtrl.lua
**Ports**: 1, 14, 16, 1992, 2007, 2416, 43, 5

## File: usr/bin/lua/LiveUpdate.lua
**Ports**: 1, 11, 12, 1992, 2005, 2006, 29, 4, 4957, 5, 6
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/js/version.js
**Ports**: 1, 100, 2, 3, 4, 5, 500, 6, 7, 9

## File: usr/sbin/3gpp
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/iscsiconfig.htm
**Ports**: 3, 3260, 65535
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: etc/Data_Signature
**Ports**: 3

## File: usr/lib/lib.7z.extracted/0/lib/hi_media.ko
**Ports**: 1, 10, 18, 2, 3, 31, 4, 6, 7, 8, 80, 9

## File: web/js/autoregister.js
**Ports**: 1, 16, 2, 31, 5, 63, 65535

## File: usr/bin/lua/ptz/PIH-717.lua
**Ports**: 1, 2, 200, 3, 7, 717

## File: bin/sync
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/usermanage.js
**Ports**: 1, 10, 100, 11, 110, 12, 16, 17, 190, 2, 20, 200, 24, 255, 27, 28, 3, 30, 31, 32, 37, 39, 4, 5, 6, 7, 8, 9

## File: web/js/FileList.js
**Ports**: 1, 10, 14, 2, 22, 24, 28, 3, 4, 5, 6, 8

## File: usr/bin/lua/ptz/SHARP.lua
**Ports**: 10, 200, 4, 5, 6

## File: web/js/cfgmanage.js
**Ports**: 1, 2, 20, 300, 500, 60

## File: web/js/alarmboxcfg.js
**Ports**: 1

## File: usr/bin/lua/ptz/Pe5051k.lua
**Ports**: 1, 10, 100, 11, 12, 123, 124, 13, 131, 14, 15, 16, 1610, 2, 200, 3, 4, 5, 6, 7, 8, 9, 999

## File: bin/pwd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/alarmout.js
**Ports**: 1, 2, 8

## File: web/js/imageprty.js
**Ports**: 1, 10, 100, 1000, 10000, 1080, 11, 12, 120, 13, 14, 15, 16, 17, 19, 1920, 2, 2000, 23, 24, 25, 250, 3, 30, 300, 33, 337, 3500, 4, 40, 4000, 450, 47, 5, 50, 500, 55, 554, 59, 6, 60, 600, 690, 7, 70, 8, 80, 8191, 9

## File: sbin/reboot
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: tmp/daemon1
**Ports**: 1, 168, 192, 2, 22, 25, 3

## File: web/js/infoindex.js
**Ports**: 1, 6, 8, 9

## File: web/js/qrcode.js
**Ports**: 1, 10, 100, 101, 102, 104, 106, 107, 108, 109, 11, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 12, 120, 121, 122, 123, 126, 128, 13, 130, 132, 133, 1335, 134, 135, 136, 138, 139, 14, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 15, 150, 151, 152, 153, 154, 158, 16, 162, 166, 17, 170, 18, 19, 2, 20, 21, 21522, 22, 23, 236, 24, 25, 255, 256, 26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 4095, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 7, 70, 71, 72, 73, 74, 75, 76, 78, 7973, 8, 80, 81, 82, 84, 86, 87, 88, 9, 90, 92, 93, 94, 97, 98, 99

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_tde.ko
**Ports**: 1, 10, 11, 13, 133, 15, 18, 19, 2, 2017, 248, 256, 280, 3, 30, 31, 315, 4, 40, 400, 408, 43, 44, 48, 5, 50, 54, 58, 5804, 6, 7, 77, 8, 80, 800, 84, 840, 87, 88, 884, 89, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/bin/lua/ptz/LiLin.lua
**Ports**: 1, 128, 16, 1610, 2, 200, 3, 8

## File: bin/busybox
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/pluginVersion.js
**Ports**: 1, 3

## File: web/js/guiset.js
**Ports**: 1, 10, 100, 1024, 12, 120, 128, 1280, 1536, 16, 160, 1792, 192, 2, 20, 200, 2048, 2160, 224, 25, 255, 256, 27, 3, 30, 32, 320, 350, 36, 375, 382, 384, 3840, 4, 4096, 448, 48, 5, 50, 512, 5569, 5570, 6, 60, 6144, 64, 640, 768, 8, 80, 8191, 8192, 896, 9, 96

## File: usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_i2s.sh
**Ports**: 1, 10, 32

## File: web/Component/schedule.js
**Ports**: 1, 10, 11, 2, 21, 24, 280, 3, 320, 3600, 4, 40, 444, 5, 527, 6, 60, 65531, 65533, 65534, 7, 8

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vda.ko
**Ports**: 1, 10, 100, 11, 12, 128, 13, 16, 18, 19, 2, 2017, 205, 255, 256, 3, 32, 33, 4, 40, 4080, 40840, 41, 43, 45, 46, 48, 49, 5, 6, 69, 7, 8, 80, 83, 86, 87, 9, 92, 99

## File: etc/init.d/S02wndev
**Ports**: 113, 203, 25

## File: usr/data/config.lua
**Ports**: 1, 10, 120, 144, 168, 176, 192, 2, 23, 240, 255, 288, 3, 32, 320, 352, 4, 480, 576, 6, 640, 720

## File: bin/iplink
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/olp.js
**Ports**: 1, 10, 100, 2

## File: web/js/pppoe.js
**Ports**: 1, 16, 2, 3, 31

## File: usr/data/space
**Ports**: 4, 5

## File: usr/bin/lua/ptz/AD1641M.lua
**Ports**: 1, 10, 11, 12, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: bin/ip
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/SIERA-D.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: web/js/ipcFaceNewConfig.js
**Ports**: 1, 10, 100, 2, 255, 3, 300, 35, 350, 374, 4, 450, 7, 8192
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: web/html/ipAccess.htm
**Ports**: 1, 64

## File: web/js/diskerror.js
**Ports**: 1, 10, 100, 12, 13, 14, 15, 16, 17, 18, 2, 255, 3, 30, 300, 32, 350, 6, 60, 600, 7, 9, 99

## File: usr/lib/lib.7z.extracted/0/lib/usbserial.ko
**Ports**: 1, 10, 2, 3, 4, 40, 41, 48, 5, 6, 7, 8, 80, 88, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: lib/librt.so.0
**Ports**: 1, 2, 4, 40, 5, 6, 7, 8, 80, 9

## File: bin/chat
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoP1-A.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: bin/login
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/localconfig.js
**Ports**: 1, 10, 100, 11, 12, 120, 13, 14, 15, 150, 16, 168, 17, 18, 19, 1900, 2, 20, 2037, 2038, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 300, 31, 32, 33, 337, 350, 3600, 37, 39, 4, 400, 5, 59, 6, 60, 64, 65535, 7, 8, 9, 998, 999

## File: web/jsCore/rpcCore.js
**Ports**: 1, 10, 128, 16, 2, 23, 264, 3, 300, 35, 48, 5005, 55, 59, 61, 62, 7, 9
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: AES, Base64, RSA

## File: bin/sleep
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: boot/uImage.extracted/0/Linux-3.10.0.bin
**Ports**: 1, 10, 100, 11, 12, 129, 13, 14, 146, 15, 159, 16, 161, 163, 17, 1700, 18, 183, 186, 19, 19194, 2, 20, 21, 210, 212, 22, 222, 224, 23, 230, 24, 240, 243, 2446, 25, 252, 253, 256, 26, 263, 27, 28, 285, 288, 29, 3, 30, 31, 314, 318, 319, 32, 33, 331, 335, 336, 34, 342, 345, 346, 35, 357, 36, 360, 363, 37, 371, 377, 38, 383, 384, 39, 395, 4, 40, 405, 41, 419, 42, 43, 44, 45, 453, 46, 47, 475, 48, 480, 49, 5, 50, 500, 51, 516, 52, 523, 53, 54, 544, 548, 55, 554, 557, 56, 566, 57, 577, 58, 588, 59, 6, 60, 61, 6116, 615, 62, 621, 623, 63, 634, 64, 65, 659, 66, 67, 673, 68, 69, 696, 7, 70, 709, 71, 719, 72, 73, 730, 737, 739, 74, 75, 752, 753, 757, 759, 76, 764, 766, 77, 78, 783, 789, 79, 791, 798, 8, 80, 808, 81, 82, 826, 828, 83, 837, 84, 844, 845, 847, 85, 855, 859, 86, 862, 87, 88, 89, 894, 896, 9, 90, 901, 91, 911, 914, 918, 92, 923, 93, 938, 94, 9412, 942, 95, 954, 96, 965, 966, 969, 97, 971, 977, 98, 989, 99

## File: bin/wget
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/data/CustomConfig
**Ports**: 3322, 5, 80

## File: usr/lib/lib.7z
**Ports**: 1, 10, 101, 106, 11, 12, 121, 13, 14, 15, 16, 162, 167, 17, 174, 179, 18, 19, 2, 20, 203, 21, 217, 218, 22, 2273, 23, 234, 236, 24, 245, 25, 255, 257, 26, 260, 27, 270, 271, 28, 29, 292, 299, 3, 30, 31, 32, 33, 34, 342, 343, 349, 35, 36, 364, 369, 37, 371, 38, 39, 3950, 396, 4, 40, 404, 41, 42, 422, 426, 428, 43, 437, 44, 45, 453, 46, 467, 47, 470, 475, 477, 48, 489, 49, 497, 5, 50, 501, 51, 52, 529, 53, 537, 54, 548, 55, 56, 560, 564, 57, 571, 58, 581, 582, 59, 591, 595, 6, 60, 61, 62, 627, 63, 64, 643, 65, 66, 67, 68, 685, 69, 7, 70, 706, 71, 72, 724, 729, 73, 732, 74, 741, 743, 75, 753, 7559, 758, 76, 77, 78, 79, 791, 793, 798, 8, 80, 81, 82, 820, 8255, 83, 84, 85, 86, 863, 87, 873, 88, 882, 887, 89, 9, 90, 900, 91, 910, 915, 92, 927, 93, 938, 94, 945, 95, 96, 962, 97, 972, 973, 98, 983, 99, 992
### Encryption/Encoding: Hex

## File: web/css/previewindex.css
**Ports**: 1, 100, 1001, 13, 140, 2, 210, 255, 333, 8, 80

## File: web/favicon.ico
**Ports**: 1, 111, 5, 542, 9, 999

## File: web/js/useronvif.js
**Ports**: 1, 17, 2, 30

## File: web/js/playbackindex.js
**Ports**: 1, 10, 100, 1024, 11, 12, 128, 13, 1394, 14, 144, 1440, 15, 150, 16, 16384, 17, 192, 2, 200, 2012, 2048, 23, 24, 243, 25, 28, 29, 3, 30, 31, 32, 35, 350, 3600, 384, 4, 400, 4096, 42, 48, 5, 50, 576, 59, 6, 60, 655, 7, 8, 9

## File: web/js/broadcast.js
**Ports**: 1, 1025, 2, 224, 239, 3, 36666

## File: web/js/onlineuser.js
**Ports**: 1, 2

## File: sbin/upnp_tv_ctrlpt
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/inittab
**Ports**: 1999, 2004, 38400, 4, 57600, 8, 9600
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/html/general.htm
**Ports**: 1

## File: lib/libdl-0.9.33.2.so
**Ports**: 1, 2, 3, 4, 40, 44, 5, 6, 7, 8, 80, 81
### Encryption/Encoding: TLS

## File: bin/ping6
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: linuxrc
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/ipAccess.js
**Ports**: 1, 190, 2, 200, 64

## File: web/js/ddnsconfig.js
**Ports**: 1, 10, 1092, 12, 13, 15, 16, 2, 22, 3, 4, 5, 500, 60, 65535, 7, 8, 80, 801, 803, 9, 901, 907, 908, 909, 910, 911, 912, 929

## File: sbin/inetd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/connetcfg.js
**Ports**: 1, 1025, 123, 127, 128, 1900, 2, 20, 200, 3, 37777, 37778, 37810, 3800, 39999, 4, 443, 5050, 554, 63, 65535, 80, 800, 9999

## File: web/js/eventScript.js
**Ports**: 1, 2, 3, 4, 500, 6, 8192

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_ao.ko
**Ports**: 1, 10, 100, 10240, 13, 18, 19, 2, 20, 200, 2017, 250, 3, 350, 4, 40, 41, 42, 43, 44, 45, 46, 5, 500, 51, 55, 6, 7, 8, 80, 800, 82, 85, 86, 9

## File: usr/lib/lib.7z.extracted/0/lib/driverbox.ko
**Ports**: 1, 10, 11, 15, 17, 180, 2, 20, 2017, 203, 21, 210, 22, 23, 24, 3, 30, 300, 31, 32, 38, 4, 40, 401, 404, 41, 42, 43, 44, 4438, 45, 46, 47, 48, 482, 49, 5, 50, 51, 58, 59, 6, 60, 61, 62, 64, 65, 66, 68, 7, 7311, 768, 8, 80, 800, 803, 808, 8090, 81, 82, 83, 84, 841, 85, 86, 87, 88, 89, 890, 9, 90, 900, 908, 92, 93, 95, 97, 99
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: Hex

## File: usr/bin/lua/ptz/General.lua
**Ports**: 1, 100, 16, 1610, 2, 200, 256, 3, 32, 4, 5, 6, 7

## File: usr/data/Data/StringAll.7z.extracted/0/StringAll
**Ports**: 1, 10, 100, 1000, 10000, 1025, 11, 110, 12, 120, 128, 13, 14, 15, 16, 17, 18, 180, 19, 2, 20, 200, 2000, 21, 22, 223, 224, 23, 239, 24, 25, 250, 254, 255, 26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 365, 37, 37777, 38, 3800, 39, 4, 40, 4000, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 500, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65535, 7, 701, 8, 801, 803, 85, 9, 90, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: DES, SSL

## File: web/js/snmpconfig.js
**Ports**: 1, 123, 1900, 2, 21, 31, 32, 37810, 3800, 39999, 5, 5050, 65535, 9999

## File: web/html/videomatrix.htm
**Ports**: 1, 10, 100, 11, 12, 120, 13, 14, 15, 16, 2, 3, 4, 5, 6, 7, 8, 9

## File: web/html/automaintain.htm
**Ports**: 1000

## File: usr/bin/lua/ptz/PELCOD-S1.lua
**Ports**: 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: web/css/custom.css
**Ports**: 10, 2, 2013, 210, 5, 8, 888, 9

## File: web/html/usermanage.htm
**Ports**: 1, 11, 2, 3, 63

## File: web/js/chanlhddquota.js
**Ports**: 1, 10, 100, 120, 1500, 2, 25, 350, 4, 50, 75

## File: usr/lib/lib.7z.extracted/0/lib/sysctl_hi3521a_asic.sh
**Ports**: 128, 19, 2, 32, 6, 7, 8

## File: web/html/alarmcenter.htm
**Ports**: 1, 65535

## File: bin/killall
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/Data_Signature
**Ports**: 9

## File: web/js/tcpip_ipc.js
**Ports**: 1, 110, 119, 120, 127, 1280, 15, 1500, 2, 20, 255, 256, 3, 33, 4, 5, 500, 7200

## File: web/js/GroupControl.js
**Ports**: 1, 15, 16, 2, 3, 4, 5, 6, 7, 8, 9

## File: web/js/audioset.js
**Ports**: 1, 1024, 1440, 2, 3, 30, 3600, 4, 500, 6, 60

## File: etc/init.d/S00devs
**Ports**: 1, 13, 204, 32, 5, 63, 64, 65, 66, 67

## File: web/html/videodetect.htm
**Ports**: 1, 10, 100, 2, 3, 300, 32, 4, 5, 50, 6, 600, 65535, 7, 8, 9

## File: bin/dd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/Samsung.lua
**Ports**: 1, 11, 12, 13, 14, 15, 16, 1610, 17, 18, 2, 20, 200, 21, 22, 226, 23, 24, 25, 256, 26, 27, 3, 30, 4, 40, 5, 50, 6, 67, 7, 8, 80, 86, 9

## File: sbin/init
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/[
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/adddevice.htm
**Ports**: 1, 10, 11, 120, 2, 200, 2000, 32, 480, 63, 65535
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/8192cu.ko
**Ports**: 1, 10, 1000, 1010, 109, 11, 1222, 13, 14, 141, 147, 15, 16, 160, 17, 19, 192, 2, 20, 200, 2002, 2016, 202, 203, 21, 210, 222, 23, 230, 23995, 24, 242, 243, 2468, 283, 29, 3, 30, 303, 31, 32, 32002, 33, 34, 350, 36, 4, 40, 400, 4000, 404, 4050, 4080, 41, 42, 43, 44, 440, 444, 45, 46, 47, 48, 4800, 49, 5, 50, 506, 51, 54, 54050, 55, 56, 57, 590, 6, 60, 62, 65, 66, 666, 6666, 667, 7, 70, 700, 7040, 71, 717, 730, 76, 7666, 8, 80, 800, 8001, 8012, 802, 8040, 8051, 8090, 81, 82, 83, 84, 85, 86, 87, 88, 89, 9, 90, 900, 9044, 91, 92
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: web/js/setindex.js
**Ports**: 1, 10, 11, 12, 2, 20, 23, 232, 272, 288, 320, 4, 485, 5, 6, 610, 686, 7, 8, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_sys.ko
**Ports**: 1, 10, 13, 18, 19, 2, 2017, 22, 3, 30, 33, 4, 42, 5, 6, 7, 8, 80, 86, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/js/diskinfo.js
**Ports**: 1, 10, 100, 1024, 2, 2000, 3, 5

## File: bin/tar
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libutil-0.9.33.2.so
**Ports**: 1, 10, 2, 4, 5, 7, 8
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: web/html/setindex.htm
**Ports**: 1, 1999, 2, 6, 7, 8
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: etc/udev/rules.d/75-persistent-net-generator.rules.optional
**Ports**: 390, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_jpege.ko
**Ports**: 1, 10, 13, 16, 18, 19, 2, 2017, 22, 255, 29, 3, 31, 32, 38, 4, 40, 42, 420, 422, 44, 47, 49, 5, 52, 56, 56789, 6, 64, 7, 78, 8, 80, 81, 84, 86, 8888, 89, 9, 92, 9387
### Encryption/Encoding: DES

## File: bin/mount
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/vi
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/jsBase/lib/m1.2.js
**Ports**: 1, 10, 100, 11, 111, 120, 13, 16, 18, 19, 2, 20, 200, 24, 250, 27, 3, 300, 32, 37, 38, 39, 4, 40, 419, 420, 46, 5, 50, 500, 6, 60, 618, 7, 8, 9, 925, 950
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex

## File: web/jsBase/lib/more.js
**Ports**: 1, 100, 16, 2, 20, 25, 250, 255, 3, 360, 4, 4096, 5, 50, 6, 60
### Encryption/Encoding: Hex

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_h264e.ko
**Ports**: 1, 10, 11, 118, 12, 128, 13, 15, 154, 16, 18, 1892, 19, 2, 2017, 22, 23, 24, 255, 3, 30, 304, 31, 32, 333, 34, 38, 39, 4, 40, 41, 42, 43, 44, 47, 48, 5, 51, 52, 53, 54, 6, 63, 64, 69, 7, 70, 8, 80, 802, 81, 85, 9

## File: web/html/cfgmanage.htm
**Ports**: 1, 1000

## File: usr/data/hardware.lua
**Ports**: 1, 2

## File: usr/lib/lib.7z.extracted/0/lib/i2c_write
**Ports**: 1, 2, 3, 4, 40, 5, 6, 8, 80, 8808, 8813, 9

## File: usr/lib/lib.7z.extracted/0/lib/i2c_common.ko
**Ports**: 1, 10, 12696, 2, 2016, 3, 4, 5, 52, 62, 7, 8, 9
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: web/js/wificfg.js
**Ports**: 1, 100, 2, 20, 200, 255, 3, 4, 40, 5, 60, 80
### Encryption/Encoding: AES

## File: bin/vlock
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/ping
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_aio.ko
**Ports**: 1, 10, 16, 2, 20, 3, 38, 4, 41, 42, 44, 46, 47, 48, 5, 6, 61, 7, 8, 83, 84, 85, 87, 88, 9

## File: bin/netstat
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/mknod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: boot/uImage
**Ports**: 1, 10, 100, 11, 12, 129, 13, 14, 146, 15, 159, 16, 161, 163, 17, 1700, 18, 183, 186, 19, 19194, 2, 20, 21, 210, 212, 22, 222, 224, 23, 230, 24, 240, 243, 2446, 25, 252, 253, 256, 26, 263, 27, 28, 285, 288, 29, 3, 30, 31, 314, 318, 319, 32, 33, 331, 335, 336, 34, 342, 345, 346, 35, 357, 36, 360, 363, 37, 371, 377, 38, 383, 384, 39, 395, 4, 40, 405, 41, 419, 42, 43, 44, 45, 453, 46, 47, 475, 48, 480, 49, 5, 50, 500, 51, 516, 52, 523, 53, 54, 544, 548, 55, 554, 557, 56, 566, 57, 577, 58, 588, 59, 6, 60, 61, 6116, 615, 62, 621, 623, 63, 634, 64, 65, 659, 66, 67, 673, 68, 69, 696, 7, 70, 709, 71, 719, 72, 73, 730, 737, 739, 74, 75, 752, 753, 757, 759, 76, 764, 766, 77, 78, 783, 789, 79, 791, 798, 8, 80, 808, 81, 82, 826, 828, 83, 837, 84, 844, 845, 847, 85, 855, 859, 86, 862, 87, 88, 89, 894, 896, 9, 90, 901, 91, 911, 914, 918, 92, 923, 93, 938, 94, 9412, 942, 95, 954, 96, 965, 966, 969, 97, 971, 977, 98, 989, 99

## File: usr/bin/lua/ptz/SONY.lua
**Ports**: 1, 128, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: usr/bin/lua/ptz/SIERA-P.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 4, 5, 6, 7, 8

## File: usr/lib/lib.7z.extracted/0/lib/crgctrl_hi3521a.sh
**Ports**: 13, 148, 32, 74

## File: bin/awk
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/HAIYU.lua
**Ports**: 200, 256, 3, 4, 5, 6, 7

## File: usr/bin/lua/ptz/WV-CS850I.lua
**Ports**: 1, 10, 100, 16, 1610, 18, 2, 200, 23, 24, 3, 4, 5, 6, 7, 8, 88, 9, 96, 99

## File: usr/etc/Global.lua
**Ports**: 1, 10, 1024, 11, 12, 128, 13, 14, 15, 16, 16384, 17, 18, 19, 1992, 2, 20, 2005, 2006, 2048, 21, 22, 23, 24, 25, 255, 256, 26, 27, 28, 29, 3, 30, 31, 32, 32768, 33, 34, 35, 36, 4, 4096, 5, 512, 5264, 6, 60, 64, 7, 8, 8192, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vgs.ko
**Ports**: 1, 10, 100, 101, 11, 12, 128, 1280, 13, 14, 1404, 18, 180, 19, 2, 20, 200, 2017, 2048, 22, 24, 24242, 255, 270, 3, 30, 32, 33, 34, 3840, 4, 40, 400, 40646, 4080, 4096, 41, 42, 420, 43, 44, 444, 45, 47, 480, 5, 50, 55, 6, 60, 61, 66, 7, 77, 771, 8, 80, 800, 81, 82, 83, 84, 843, 844, 85, 855, 858, 86, 88, 884, 886, 89, 9, 90, 91, 92, 99

## File: usr/lib/lib.7z.extracted/0/lib/8192eu.ko
**Ports**: 1, 10, 1000, 101, 1010, 11, 111, 12, 1222, 13, 130, 14, 15, 1500, 16, 17, 18, 2, 20, 200, 2016, 202, 203, 21, 210, 211, 22, 222, 22224, 23, 23995, 24, 240, 2468, 25, 26, 28, 282, 2868, 29, 3, 30, 300, 3003, 303, 3055, 31, 32, 33, 34, 35, 355, 36, 38, 380, 381, 4, 40, 400, 4000, 403, 404, 4080, 41, 42, 43, 43003, 44, 440, 444, 45, 46, 47, 48, 4800, 488, 49, 5, 50, 502, 506, 5242, 53, 54, 544, 55, 555, 5555, 56, 57, 59, 6, 60, 61, 62, 63, 64, 640, 65, 66, 6644, 67, 7, 70, 700, 7080, 71, 717, 72, 7207, 7300, 74, 75, 77, 78, 8, 80, 800, 802, 805, 8051, 81, 82, 822, 83, 84, 85, 86, 864, 87, 870, 88, 8812, 8814, 8821, 8822, 888, 89, 9, 90, 900, 91, 93, 94, 95, 96, 960, 98, 980
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: Hex

## File: web/js/emailconfig.js
**Ports**: 1, 100, 120, 1440, 16, 18, 2, 20, 3, 30, 31, 360, 3600, 4, 40, 5, 60, 63, 65535

## File: lib/ld-uClibc.so.0
**Ports**: 1, 12, 13, 2, 21, 3, 4, 40, 44, 5, 6, 7, 8, 80, 800, 81, 88, 9
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: TLS

## File: etc/init.d/S99dh
**Ports**: 1, 10, 168, 192, 200, 240, 255, 5, 5120, 52, 6, 777

## File: sbin/netinit
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/passwd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/mesg
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/ATMConfig.htm
**Ports**: 1, 10, 11, 12, 1200, 13, 14, 15, 16, 19200, 2, 20, 2400, 25, 3, 38400, 4, 4800, 5, 57600, 6, 600, 7, 8, 9, 9600

## File: bin/gunzip
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/DH-MATRIX.lua
**Ports**: 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vdec.ko
**Ports**: 1, 10, 102, 1030, 1038, 1049, 1086, 1096, 118, 1201, 1209, 124, 1269, 1296, 13, 132, 1322, 1342, 1356, 138, 14, 1441, 1491, 150, 1501, 1512, 1526, 1539, 1548, 156, 1581, 16, 164, 1642, 1655, 1664, 1720, 1726, 1761, 18, 180, 1817, 1833, 1876, 1883, 19, 1903, 1908, 191, 1920, 1925, 1928, 1933, 1940, 1948, 1953, 1956, 1962, 197, 1971, 1983, 1992, 2, 200, 2001, 2010, 2017, 2019, 202, 2027, 203, 2060, 2065, 2076, 2134, 2137, 2146, 219, 2212, 2218, 2248, 225, 2261, 2270, 2285, 2295, 232, 2326, 2342, 2348, 2355, 2374, 238, 24, 2421, 2623, 270, 2702, 2719, 2734, 2759, 2775, 2790, 2803, 2880, 2891, 2904, 292, 2922, 2937, 294, 2952, 297, 2986, 2996, 3, 300, 3011, 302, 3034, 3086, 3171, 318, 32, 3217, 3292, 33, 3305, 3313, 3324, 3334, 3355, 3380, 3408, 3414, 3427, 3435, 3445, 3453, 3497, 3537, 3565, 3573, 3598, 3660, 3670, 3723, 3741, 3768, 377, 3783, 3790, 3828, 3842, 385, 3862, 3874, 3882, 3921, 4, 40, 408, 4096, 41, 4103, 4125, 4151, 4157, 4169, 42, 4204, 4221, 43, 4378, 44, 4461, 4467, 4473, 4485, 4492, 4499, 45, 4506, 4535, 46, 4615, 4671, 4676, 4681, 4686, 4692, 4698, 47, 4704, 4745, 4757, 4769, 4796, 48, 4809, 4815, 4821, 4850, 4900, 4908, 4962, 4997, 5, 50, 5002, 5012, 5051, 5066, 5074, 5096, 516, 5200, 5235, 5318, 5325, 5374, 5404, 5418, 5428, 5440, 5490, 5498, 5505, 5573, 5579, 56, 5624, 6, 60, 603, 612, 661, 680, 689, 7, 727, 73, 745, 773, 797, 8, 80, 81, 82, 83, 836, 850, 859, 87, 873, 88, 880, 9, 90, 91, 96, 961, 971, 979

## File: bin/ps
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/Data_Signature
**Ports**: 7, 8

## File: web/Component/schedule.htm
**Ports**: 1, 10, 12, 14, 16, 18, 2, 20, 22, 24, 3, 4, 5, 6, 7, 8

## File: usr/lib/lib.7z.extracted/0/lib/usb_wwan.ko
**Ports**: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9

## File: bin/kill
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/iscsiconfig.js
**Ports**: 1, 12, 2, 31, 3260, 3650, 50, 65535, 8
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: sbin/hdparm
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/useronvif.htm
**Ports**: 31

## File: lib/libuClibc-0.9.33.2.so
**Ports**: 1, 10, 100, 1020, 105, 109, 11, 110, 111, 1111, 11111, 1121, 12, 1234, 124, 13, 133, 14, 141, 145, 15, 1535, 16, 17, 17641, 18, 186, 1872, 1873, 19, 1912, 1913, 1926, 1927, 1989, 1990, 2, 20, 202, 20212, 2033, 2078, 208, 21, 2133, 22, 222, 2222, 22222, 22223, 22224, 228, 23, 234, 2345, 24, 245, 246, 25, 256, 26, 263, 27, 27751, 28, 288, 29, 3, 30, 300, 303, 306, 31, 32, 320, 321, 33, 333, 3345, 33744, 34, 342, 344, 35, 36, 37, 376, 38, 39, 4, 40, 401, 4050, 408, 4080, 41, 4151, 42, 4289, 43, 432, 4353, 44, 44355, 444, 4467, 45, 46, 47, 48, 49, 498, 5, 50, 51, 51305, 52, 5289, 53, 54, 543, 55, 551, 56, 5666, 5678, 56789, 57, 571, 572, 58, 588, 59, 5945, 6, 60, 600, 61, 613, 62, 620, 6272, 63, 64, 65, 66, 666, 67, 68, 682, 683, 69, 699, 7, 70, 701, 703, 71, 72, 73, 7383, 74, 7407, 75, 757, 76, 769, 77, 777, 78, 785, 789, 79, 793, 794, 8, 80, 800, 807, 808, 8080, 81, 813, 815, 818, 82, 83, 831, 84, 848, 85, 86, 87, 88, 8859, 89, 899, 9, 90, 900, 91, 92, 93, 94, 95, 96, 964, 97, 98, 99, 999, 9999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: lib/libcrypt-0.9.33.2.so
**Ports**: 1, 2, 3, 4, 44, 5, 6, 7, 8, 80, 9, 91
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/eject
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/cttyhack
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/p7zip
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/autoregister.htm
**Ports**: 1, 31, 65535

## File: usr/bin/lua/ptz/QT-2XXD.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: web/jsCore/aes.js
**Ports**: 1, 10, 11, 12, 128, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 255, 256, 257, 26, 27, 28, 283, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65535, 7, 75, 8, 9, 99
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, Hex, SSL

## File: web/cap.js
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 19, 2, 3, 37777, 4, 5, 554, 6, 7, 8, 9

## File: bin/gzip
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoP-SD.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 4, 5, 6, 7, 8

## File: web/html/chanldiscgroup.htm
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/js/adddevice.js
**Ports**: 1, 10, 108, 110, 127, 15, 16, 168, 17, 192, 2, 20, 210, 25001, 255, 256, 275, 3, 31, 32, 37777, 4, 40001, 442, 5, 554, 6, 65535, 7, 8, 80, 9, 9999
