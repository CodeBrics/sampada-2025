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
- **Current Date**: `Saturday, February 01, 2025, 2 PM `

---

### Startup Script: `/bin/busybox`

- **Directory Name**: `/bin`
- **File Name**: `busybox`
- **File Type**: `ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped`
- **MD5 Hash**: `a053573c0e452c7a96c3fc028d2b9e8e`
- **File Size**: `1337336 bytes`
- **Architecture**: `ARM`
- **Current Date**: `Saturday, February 01, 2025, 2 PM `

---

# Scan Summary

- **Total Files Scanned:** 199
- **Total Suspicious Keywords Detected:** 855

<details>
<summary>Click to view detailed results</summary>

### File: `linuxrc`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `init`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

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
| `CopyFileA`     |
| `https://`     |
| `http://`     |
| `CreateProcessA`     |
| `FindFirstFileA`     |
| `FindNextFileA`     |

### File: `web/index.htm`

| Keyword        |
|----------------|
| `base64`     |
| `http://`     |
| `admin`     |
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
| `base64`     |
| `http://`     |
| `admin`     |
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
| `exec`     |
| `/bin/sh`     |

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
| `chmod`     |
| `/bin/sh`     |

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
| `wget`     |
| `http://`     |
| `bash`     |

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
| `chmod`     |
| `exec`     |
| `/bin/sh`     |
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
| `chmod`     |
| `exec`     |
| `/bin/sh`     |
| `password`     |

### File: `lib/libgcc_s.so.1`

| Keyword        |
|----------------|
| `exec`     |

### File: `lib/libpthread.so.0`

| Keyword        |
|----------------|
| `exec`     |
| `/bin/sh`     |

### File: `lib/libpthread-0.9.33.2.so`

| Keyword        |
|----------------|
| `exec`     |
| `/bin/sh`     |

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
| `chmod`     |
| `/bin/sh`     |

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
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `usr/sbin/ii`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `usr/sbin/3gpp`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `usr/sbin/.dec.sh`

| Keyword        |
|----------------|
| `base64`     |
| `bash`     |

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
| `exec`     |
| `https://`     |
| `chmod`     |
| `base64`     |
| `http://`     |
| `openssl`     |
| `password`     |
| `/bin/sh`     |

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
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/ifconfig`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/reboot`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/net3g`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/lsusb`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/netinit`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/upgraded`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/ifdown`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/pppoe-start`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `sbin/ifup`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/fdisk`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/hdparm`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/halt`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/poweroff`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/netinit6`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/lspci`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/getty`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/dvrhelper`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/pppoe`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/pppd`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/upnp_tv_ctrlpt`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/modprobe`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/depmod`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/rmmod`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/chat`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/route`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/insmod`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/makedevs`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/mdev`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/init`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/lsmod`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `sbin/inetd`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `chmod`     |
| `http://`     |
| `/bin/sh`     |

### File: `bin/less`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/vlock`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/[[`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/ifenslave`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/netstat`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/p7zip`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/iprule`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/dnsdomainname`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/gunzip`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/sync`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/vi`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/free`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/awk`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/nice`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/devmem`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/tar`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/eject`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/mount`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/busybox`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/chmod`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/login`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/df`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/wget`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/killall5`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/gzip`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/rm`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/mv`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/cat`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/iplink`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/printenv`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/du`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/grep`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/mkdir`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/ash`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/kill`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/iptunnel`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/umount`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/passwd`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/ps`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/ipaddr`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/cttyhack`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/cp`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/ip`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/ping6`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/sleep`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/hush`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/mesg`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/top`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/hostname`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/sh`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/chat`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/touch`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/uname`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/iproute`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/ls`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/bootenv`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/mktemp`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/pwd`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/msh`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/killall`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/mknod`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/ping`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/echo`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/dd`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `bin/[`

| Keyword        |
|----------------|
| `admin`     |
| `exec`     |
| `bash`     |
| `chmod`     |
| `http://`     |
| `password`     |
| `/bin/sh`     |

### File: `tmp/daemon1`

| Keyword        |
|----------------|
| `bash`     |

</details>

# Vulnerability Report

- **Total Files Analyzed:** 170
- **Files with Port/IP Findings:** 5
- **Files with Vulnerabilities:** 158
- **Files with Encryption/Encoding Findings:** 128

<details>
<summary>Click to view detailed findings</summary>

## File: `lib/libcrypt-0.9.33.2.so`

### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: `sbin/pppoe`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/js/wificfg.js`

### Encryption/Encoding: AES


## File: `sbin/chat`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/js/chanldiscgroup.js`

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `bin/vi`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/usbserial.ko`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `bin/busybox`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/sleep`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/poweroff`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/nice`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/getty`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/js/update.js`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Base64


## File: `bin/cttyhack`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/index.htm`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `web/webplugin.exe`

### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: `bin/awk`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/dnsdomainname`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/msh`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/load_hisimod.sh`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `web/html/defaultcfg.htm`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `sbin/upnp_tv_ctrlpt`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/free`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/hostname`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/fdisk`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/bin/lua/LiveUpdate.lua`

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `sbin/init`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/8192cu.ko`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `sbin/dvrhelper`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_ive.ko`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `web/html/chanldiscgroup.htm`

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `bin/gunzip`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/mount`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z`

### Encryption/Encoding: Hex


## File: `web/jsCore/aes.js`

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, Hex, SSL


## File: `bin/printenv`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/i2c_common.ko`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: `bin/mesg`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/8192eu.ko`

### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: Hex


## File: `usr/sbin/3gpp`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/ifenslave`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/uname`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/js/adddevice.js`

**Ports**: 25001, 37777, 40001


## File: `sbin/ifconfig`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/libutil-0.9.33.2.so`

### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: `bin/iplink`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/eject`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/modprobe`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_venc.ko`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: `sbin/upgraded`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/grep`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/killall`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/mkdir`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/sbin/usb_modeswitch`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/jsCore/rpcCore.js`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, RSA


## File: `bin/bootenv`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/js/iscsiconfig.js`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: `web/jsCore/rsa.js`

### Encryption/Encoding: Hex, RSA


## File: `etc/profile`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `lib/libutil.so.0`

### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: `usr/bin/ssl/pwdreset.pem`

### Encryption/Encoding: RSA


## File: `sbin/lspci`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/mv`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/libuClibc-0.9.33.2.so`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `bin/iptunnel`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/du`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/passwd`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `etc/inittab`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `sbin/makedevs`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/driverbox.ko`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: Hex


## File: `sbin/depmod`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/mdev`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/df`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/ld-uClibc-0.9.33.2.so`

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: TLS


## File: `sbin/net3g`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/js/setindex.js`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `bin/mktemp`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/hdparm`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/chat`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/libhive_common.so`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `usr/bin/DahuaExec`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `bin/[[`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_vou.ko`

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `bin/hush`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/rm`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/netinit6`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/pwd`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/login`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/libpthread.so.0`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_tde.ko`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `bin/dd`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/libdl.so.0`

### Encryption/Encoding: TLS


## File: `bin/top`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/jsBase/lib/more.js`

### Encryption/Encoding: Hex


## File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_jpege.ko`

### Encryption/Encoding: DES


## File: `usr/lib/lib.7z.extracted/0/lib/hifb.ko`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: DES


## File: `bin/ping6`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/libc.so.0`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `web/html/emailconfig.htm`

### Encryption/Encoding: SSL, TLS


## File: `bin/[`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/insmod`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/bin/Challenge`

**Ports**: 3, 8686

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, DES, Hex, RSA, SSL, TLS


## File: `lib/ld-uClibc.so.0`

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: TLS


## File: `linuxrc`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/iproute`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/umount`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/ip`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/jsBase/lib/m1.2.js`

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex


## File: `bin/ps`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/ls`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/halt`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/js/previewindex.js`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: Base64


## File: `bin/echo`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/html/update.htm`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `sbin/ifup`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/sh`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/reboot`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/iprule`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/netinit`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/gzip`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/cp`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: DES, RSA, SSL


## File: `sbin/lsusb`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/rmmod`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/libgcc_s.so.1`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `bin/mknod`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/ash`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/html/version.htm`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `web/js/ipcFaceNewConfig.js`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: `usr/lib/lib.7z.extracted/0/lib/avss.ko`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: AES, RSA


## File: `bin/kill`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/lsmod`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `lib/libstdc++.so.6`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: TLS


## File: `sbin/pppd`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/html/iscsiconfig.htm`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: `lib/libcrypt.so.0`

### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: `bin/ping`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `init`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/killall5`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/SigFileList`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `sbin/3gpp`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/js/index.js`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: Base64


## File: `bin/netstat`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/cat`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/tar`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/inetd`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/html/adddevice.htm`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `web/config/index.htm`

### Encryption/Encoding: Base64


## File: `bin/sync`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/jsBase/lib/base64.js`

### Encryption/Encoding: Base64


## File: `etc/services`

**Ports**: 1646, 4899

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: SSL, TLS


## File: `bin/wget`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `sbin/ifdown`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/bin/lua/ATMHead.lua`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_sys.ko`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `lib/libpthread-0.9.33.2.so`

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: `usr/lib/lib.7z.extracted/0/lib/osa.ko`

### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `sbin/route`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/touch`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `usr/data/Data/StringAll.7z.extracted/0/StringAll`

**Ports**: 3800, 85

### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: DES, SSL


## File: `bin/vlock`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/html/setindex.htm`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `usr/lib/lib.7z.extracted/0/lib/hi3521a_vpss.ko`

**Ports**: 1

### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: `lib/libdl-0.9.33.2.so`

### Encryption/Encoding: TLS


## File: `bin/p7zip`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/chmod`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/ipaddr`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `web/html/logmanage.htm`

### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: `bin/less`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


## File: `bin/devmem`

### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA


</details>
