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
- **Current Date**: `Friday, January 31, 2025, 6 PM `

---

### Startup Script: `/bin/busybox`

- **Directory Name**: `/bin`
- **File Name**: `busybox`
- **File Type**: `ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped`
- **MD5 Hash**: `a053573c0e452c7a96c3fc028d2b9e8e`
- **File Size**: `1337336 bytes`
- **Architecture**: `ARM`
- **Current Date**: `Friday, January 31, 2025, 6 PM `

---

# Scan Summary

- **Total Files Scanned:** 199
- **Total Suspicious Keywords Detected:** 855

<details>
<summary>Click to view detailed results</summary>

### File: `linuxrc`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `init`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `web/olp.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/SigFileList`

| Keyword        |
|----------------|
| `base64`     |

### File: `web/webplugin.exe`

| Keyword        |
|----------------|
| `FindNextFileA`     |
| `FindFirstFileA`     |
| `https://`     |
| `CreateProcessA`     |
| `http://`     |
| `CopyFileA`     |

### File: `web/index.htm`

| Keyword        |
|----------------|
| `admin`     |
| `http://`     |
| `base64`     |
| `password`     |

### File: `web/jsBase/lib/qrcode.js`

| Keyword        |
|----------------|
| `base64`     |

### File: `web/jsBase/lib/m1.2.js`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/jsCore/rpcCore.js`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `password`     |

### File: `web/jsCore/aes.js`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/html/chanldiscgroup.htm`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/html/adddevice.htm`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

### File: `web/html/alarmindex.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/pppoe.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/useronvif.htm`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

### File: `web/html/3gnetcfg.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/previewindex.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/iscsiconfig.htm`

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

### File: `web/html/audiocfg.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/update.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/ddnsconfig.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/infoindex.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/faceplayback.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/wificfg.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/html/setindex.htm`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/html/emailconfig.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/image/icons2.png`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/config/index.htm`

| Keyword        |
|----------------|
| `admin`     |
| `http://`     |
| `base64`     |
| `password`     |

### File: `web/css/oem.css`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/imageprty.js`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/js/chanldiscgroup.js`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/js/usermanage.js`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

### File: `web/js/update.js`

| Keyword        |
|----------------|
| `exec`     |

### File: `web/js/findPwd.js`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

### File: `web/js/pppoe.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/connetcfg.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/ddnsconfig.js`

| Keyword        |
|----------------|
| `http://`     |
| `password`     |

### File: `web/js/index.js`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

### File: `web/js/useronvif.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/deviceInitial.js`

| Keyword        |
|----------------|
| `admin`     |

### File: `web/js/3gnetcfg.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/qrcode.js`

| Keyword        |
|----------------|
| `base64`     |

### File: `web/js/defaultcfg.js`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/js/adddevice.js`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

### File: `web/js/broadcast.js`

| Keyword        |
|----------------|
| `http://`     |

### File: `web/js/loginEx.js`

| Keyword        |
|----------------|
| `admin`     |

### File: `web/js/iscsiconfig.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/wificfg.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/emailconfig.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/previewindex.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/js/remotestorage.js`

| Keyword        |
|----------------|
| `password`     |

### File: `web/platformHtm/GAYS.htm`

| Keyword        |
|----------------|
| `password`     |

### File: `web/platformHtm/GAYS.js`

| Keyword        |
|----------------|
| `password`     |

### File: `etc/services`

| Keyword        |
|----------------|
| `admin`     |
| `http://`     |
| `exec`     |
| `password`     |

### File: `etc/protocols`

| Keyword        |
|----------------|
| `http://`     |

### File: `etc/passwd`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/inittab`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `exec`     |

### File: `etc/passwd-`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/init.d/S81toe`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/init.d/S00devs`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/init.d/S99dh`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `chmod`     |

### File: `etc/init.d/rcS`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/init.d/S01udev`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/init.d/S02wndev`

| Keyword        |
|----------------|
| `bash`     |
| `http://`     |
| `wget`     |

### File: `etc/init.d/S80network`

| Keyword        |
|----------------|
| `bash`     |
| `/bin/sh`     |

### File: `etc/udev/rules.d/75-persistent-net-generator.rules.optional`

| Keyword        |
|----------------|
| `admin`     |

### File: `lib/libuClibc-0.9.33.2.so`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `chmod`     |
| `exec`     |
| `password`     |

### File: `lib/ld-uClibc-0.9.33.2.so`

| Keyword        |
|----------------|
| `exec`     |

### File: `lib/ld-uClibc.so.0`

| Keyword        |
|----------------|
| `exec`     |

### File: `lib/libc.so.0`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `chmod`     |
| `exec`     |
| `password`     |

### File: `lib/libgcc_s.so.1`

| Keyword        |
|----------------|
| `exec`     |

### File: `lib/libpthread.so.0`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `exec`     |

### File: `lib/libpthread-0.9.33.2.so`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `exec`     |

### File: `usr/SigFileList`

| Keyword        |
|----------------|
| `password`     |

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
| `http://`     |
| `exec`     |
| `password`     |

### File: `usr/data/Data/sharePicture/reset3.png`

| Keyword        |
|----------------|
| `http://`     |

### File: `usr/etc/load_modules.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `chmod`     |

### File: `usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vicap.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/crgctrl_hi3521a.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/8192cu.ko`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_i2s.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_tde.ko`

| Keyword        |
|----------------|
| `wget`     |

### File: `usr/lib/lib.7z.extracted/0/lib/load_hisimod.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vga_hdmi_spi.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_vou.ko`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/lib/lib.7z.extracted/0/lib/sysctl_hi3521a_asic.sh`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_vpss.ko`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/sbin/usb_modeswitch`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `usr/sbin/ii`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/sbin/3gpp`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `usr/sbin/.dec.sh`

| Keyword        |
|----------------|
| `bash`     |
| `base64`     |

### File: `usr/sbin/nfs`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/bin/DahuaExec`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/bin/Challenge`

| Keyword        |
|----------------|
| `admin`     |
| `wget`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `https://`     |
| `base64`     |
| `http://`     |
| `exec`     |
| `openssl`     |

### File: `usr/bin/lua/LiveUpdate.lua`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/bin/lua/compat-5.1.lua`

| Keyword        |
|----------------|
| `http://`     |
| `wget`     |

### File: `sbin/3gpp`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/ifconfig`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/reboot`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/net3g`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/lsusb`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/netinit`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/upgraded`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/ifdown`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/pppoe-start`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `sbin/ifup`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/fdisk`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/hdparm`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/halt`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/poweroff`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/netinit6`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/lspci`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/getty`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/dvrhelper`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/pppoe`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/pppd`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/upnp_tv_ctrlpt`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/modprobe`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/depmod`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/rmmod`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/chat`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/route`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/insmod`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/makedevs`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/mdev`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/init`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/lsmod`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `sbin/inetd`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin`

| Keyword        |
|----------------|
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `http://`     |
| `exec`     |

### File: `bin/less`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/vlock`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/[[`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/ifenslave`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/netstat`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/p7zip`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/iprule`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/dnsdomainname`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/gunzip`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/sync`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/vi`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/free`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/awk`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/nice`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/devmem`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/tar`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/eject`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/mount`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/busybox`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/chmod`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/login`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/df`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/wget`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/killall5`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/gzip`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/rm`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/mv`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/cat`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/iplink`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/printenv`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/du`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/grep`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/mkdir`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/ash`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/kill`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/iptunnel`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/umount`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/passwd`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/ps`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/ipaddr`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/cttyhack`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/cp`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/ip`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/ping6`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/sleep`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/hush`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/mesg`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/top`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/hostname`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/sh`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/chat`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/touch`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/uname`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/iproute`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/ls`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/bootenv`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/mktemp`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/pwd`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/msh`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/killall`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/mknod`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/ping`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/echo`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/dd`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `bin/[`

| Keyword        |
|----------------|
| `bash`     |
| `admin`     |
| `/bin/sh`     |
| `chmod`     |
| `password`     |
| `http://`     |
| `exec`     |

### File: `tmp/daemon1`

| Keyword        |
|----------------|
| `bash`     |

</details>
# Vulnerabilities in executable files

## File: sbin/insmod
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/sbin/usb_modeswitch
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libgcc_s.so.1
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: web/js/setindex.js
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/jsCore/aes.js
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, Hex, SSL

## File: etc/profile
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/sbin/3gpp
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/3gpp
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/jsBase/lib/base64.js
### Encryption/Encoding: Base64

## File: bin/dnsdomainname
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libhive_common.so
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: sbin/halt
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/devmem
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/pppd
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/depmod
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/index.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: bin/top
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: init
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/osa.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: sbin/lsusb
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vpss.ko
**Ports**: 1
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: sbin/reboot
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/gzip
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libpthread.so.0
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: usr/lib/lib.7z.extracted/0/lib/driverbox.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: Hex

## File: bin/p7zip
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/ipaddr
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libdl.so.0
### Encryption/Encoding: TLS

## File: bin/tar
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/jsBase/lib/more.js
### Encryption/Encoding: Hex

## File: bin/ps
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/vi
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/awk
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/pwd
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/df
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libdl-0.9.33.2.so
### Encryption/Encoding: TLS

## File: usr/lib/lib.7z.extracted/0/lib/i2c_common.ko
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: sbin/getty
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/ls
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/dd
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/init
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/Challenge
**Ports**: 3, 8686
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, DES, Hex, RSA, SSL, TLS

## File: bin/ifenslave
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/sleep
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/modprobe
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/passwd
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libutil-0.9.33.2.so
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/mkdir
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/load_hisimod.sh
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/html/iscsiconfig.htm
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: bin/login
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/dvrhelper
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/ld-uClibc-0.9.33.2.so
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: TLS

## File: web/js/adddevice.js
**Ports**: 25001, 37777, 40001

## File: bin/ip
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/jsCore/rpcCore.js
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: AES, Base64, RSA

## File: lib/ld-uClibc.so.0
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: TLS

## File: bin/vlock
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/lspci
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/netinit
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hifb.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: DES

## File: web/html/setindex.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: sbin/inetd
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/hdparm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/emailconfig.htm
### Encryption/Encoding: SSL, TLS

## File: bin/touch
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/sh
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/defaultcfg.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: sbin/ifdown
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/upgraded
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/update.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: bin/iproute
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/du
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/[[
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/DahuaExec
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: usr/bin/lua/ATMHead.lua
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/8192cu.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: bin/rm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/kill
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/route
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/rmmod
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libcrypt-0.9.33.2.so
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/cttyhack
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_venc.ko
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: bin/ping
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/killall
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/hush
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/bootenv
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/mktemp
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/iscsiconfig.js
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: bin/mv
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/makedevs
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/index.js
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: Base64

## File: lib/libutil.so.0
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/iprule
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/fdisk
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/chat
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/services
**Ports**: 1646, 4899
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: SSL, TLS

## File: sbin/pppoe
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/mdev
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/chanldiscgroup.htm
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: bin/[
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/free
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/upnp_tv_ctrlpt
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/LiveUpdate.lua
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/js/ipcFaceNewConfig.js
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_sys.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: sbin/ifup
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/gunzip
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/logmanage.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: sbin/netinit6
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/wificfg.js
### Encryption/Encoding: AES

## File: bin/killall5
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/ping6
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/previewindex.js
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: Base64

## File: bin/printenv
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/data/Data/StringAll.7z.extracted/0/StringAll
**Ports**: 3800, 85
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: DES, SSL

## File: usr/bin/ssl/pwdreset.pem
### Encryption/Encoding: RSA

## File: lib/libc.so.0
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: bin/umount
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/chat
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/ifconfig
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/chanldiscgroup.js
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: bin/grep
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/config/index.htm
### Encryption/Encoding: Base64

## File: web/html/version.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: bin/mesg
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/sync
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/inittab
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: bin/uname
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_ive.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: DES, RSA, SSL

## File: bin/mount
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/lsmod
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/adddevice.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: lib/libcrypt.so.0
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/busybox
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/chmod
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/nice
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/jsBase/lib/m1.2.js
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex

## File: bin/cat
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/hostname
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z
### Encryption/Encoding: Hex

## File: bin/cp
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/update.js
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Base64

## File: lib/libstdc++.so.6
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: TLS

## File: usr/lib/lib.7z.extracted/0/lib/avss.ko
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: AES, RSA

## File: bin/mknod
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/msh
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/8192eu.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: Hex

## File: web/SigFileList
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: lib/libuClibc-0.9.33.2.so
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_jpege.ko
### Encryption/Encoding: DES

## File: bin/echo
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_tde.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/usbserial.ko
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: sbin/net3g
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/iplink
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/eject
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: linuxrc
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/wget
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/webplugin.exe
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/ash
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/jsCore/rsa.js
### Encryption/Encoding: Hex, RSA

## File: sbin/poweroff
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/netstat
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libpthread-0.9.33.2.so
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: bin/iptunnel
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/less
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vou.ko
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

