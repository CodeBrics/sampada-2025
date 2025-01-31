# Directory Tree Structure

```- **bin/**
  - bin/Data_Signature (data)
  - bin/SigFileList (ASCII text)
  - bin/[ (symbolic link to busybox)
  - bin/[[ (symbolic link to busybox)
  - bin/ash (symbolic link to busybox)
  - bin/awk (symbolic link to busybox)
  - bin/bootenv (symbolic link to busybox)
  - bin/busybox (ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped)
  - bin/cat (symbolic link to busybox)
  - bin/chat (symbolic link to busybox)
  - bin/chmod (symbolic link to busybox)
  - bin/cp (symbolic link to busybox)
  - bin/cttyhack (symbolic link to busybox)
  - bin/dd (symbolic link to busybox)
  - bin/devmem (symbolic link to busybox)
  - bin/df (symbolic link to busybox)
  - bin/dnsdomainname (symbolic link to busybox)
  - bin/du (symbolic link to busybox)
  - bin/echo (symbolic link to busybox)
  - bin/eject (symbolic link to busybox)
  - bin/free (symbolic link to busybox)
  - bin/grep (symbolic link to busybox)
  - bin/gunzip (symbolic link to busybox)
  - bin/gzip (symbolic link to busybox)
  - bin/hostname (symbolic link to busybox)
  - bin/hush (symbolic link to busybox)
  - bin/ifenslave (symbolic link to busybox)
  - bin/ip (symbolic link to busybox)
  - bin/ipaddr (symbolic link to busybox)
  - bin/iplink (symbolic link to busybox)
  - bin/iproute (symbolic link to busybox)
  - bin/iprule (symbolic link to busybox)
  - bin/iptunnel (symbolic link to busybox)
  - bin/kill (symbolic link to busybox)
  - bin/killall (symbolic link to busybox)
  - bin/killall5 (symbolic link to busybox)
  - bin/less (symbolic link to busybox)
  - bin/login (symbolic link to busybox)
  - bin/ls (symbolic link to busybox)
  - bin/mesg (symbolic link to busybox)
  - bin/mkdir (symbolic link to busybox)
  - bin/mknod (symbolic link to busybox)
  - bin/mktemp (symbolic link to busybox)
  - bin/mount (symbolic link to busybox)
  - bin/msh (symbolic link to busybox)
  - bin/mv (symbolic link to busybox)
  - bin/netstat (symbolic link to busybox)
  - bin/nice (symbolic link to busybox)
  - bin/p7zip (symbolic link to busybox)
  - bin/passwd (symbolic link to busybox)
  - bin/ping (symbolic link to busybox)
  - bin/ping6 (symbolic link to busybox)
  - bin/printenv (symbolic link to busybox)
  - bin/ps (symbolic link to busybox)
  - bin/pwd (symbolic link to busybox)
  - bin/rm (symbolic link to busybox)
  - bin/sh (symbolic link to busybox)
  - bin/sleep (symbolic link to busybox)
  - bin/sync (symbolic link to busybox)
  - bin/tar (symbolic link to busybox)
  - bin/top (symbolic link to busybox)
  - bin/touch (symbolic link to busybox)
  - bin/umount (symbolic link to busybox)
  - bin/uname (symbolic link to busybox)
  - bin/vi (symbolic link to busybox)
  - bin/vlock (symbolic link to busybox)
  - bin/wget (symbolic link to busybox)
- **boot/**
  - boot/uImage (u-boot legacy uImage, Linux-3.10.0, Linux/ARM, OS Kernel Image (Not compressed), 2193136 bytes, Mon Oct 16 03:30:12 2017, Load Address: 0X80008000, Entry Point: 0X80008000, Header CRC: 0XD6076B1F, Data CRC: 0X90665D3C)
  - **boot/uImage.extracted/**
    - **boot/uImage.extracted/0/**
      - boot/uImage.extracted/0/Linux-3.10.0.bin (Linux kernel ARM boot executable zImage (little-endian))
      - **boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/**
        - **boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/**
          - boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin (data)
          - **boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin.extracted/**
            - **boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin.extracted/52C6A0/**
              - **boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin.extracted/52C6A0/dev/**
              - **boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin.extracted/52C6A0/root/**
- **dev/**
- **etc/**
  - etc/Data_Signature (data)
  - etc/SigFileList (ASCII text)
  - etc/SigFilePartition (ASCII text)
  - **etc/Wireless/**
    - **etc/Wireless/RT2870STA/**
      - etc/Wireless/RT2870STA/RT2870STA.dat (ASCII text)
  - etc/fs-version (ASCII text, with CRLF line terminators)
  - etc/fstab (ASCII text)
  - etc/group (ASCII text)
  - **etc/init.d/**
    - etc/init.d/S00devs (POSIX shell script, ASCII text executable)
    - etc/init.d/S01udev (POSIX shell script, ASCII text executable)
    - etc/init.d/S02wndev (Bourne-Again shell script, ASCII text executable)
    - etc/init.d/S80network (POSIX shell script, ASCII text executable)
    - etc/init.d/S81toe (POSIX shell script, ASCII text executable)
    - etc/init.d/S99dh (POSIX shell script, ASCII text executable)
    - etc/init.d/rcS (POSIX shell script, ASCII text executable)
  - etc/inittab (ASCII text)
  - etc/mactab (empty)
  - etc/memstat.conf (ASCII text, with CRLF line terminators)
  - etc/mtab (ASCII text)
  - etc/passwd (ASCII text)
  - etc/passwd- (ASCII text)
  - **etc/ppp/**
    - etc/ppp/options (symbolic link to /dev/null)
    - etc/ppp/pap-secrets (symbolic link to /dev/null)
    - etc/ppp/pppoe-enable (symbolic link to /dev/null)
    - etc/ppp/pppoe-redial_time (symbolic link to /dev/null)
    - etc/ppp/pppoe-start (symbolic link to /dev/null)
    - etc/ppp/pppoesessionctx (symbolic link to /dev/null)
  - etc/profile (ASCII text, with CR, LF line terminators, with escape sequences)
  - etc/protocols (ASCII text)
  - etc/resolv.conf (symbolic link to /dev/null)
  - etc/services (ASCII text)
  - **etc/udev/**
    - **etc/udev/rules.d/**
      - etc/udev/rules.d/54-gphoto.rules (ASCII text)
      - etc/udev/rules.d/60-pcmcia.rules (ASCII text)
      - etc/udev/rules.d/75-cd-aliases-generator.rules.optional (ASCII text)
      - etc/udev/rules.d/75-persistent-net-generator.rules.optional (ASCII text)
      - etc/udev/rules.d/90-hal.rules (ASCII text)
      - etc/udev/rules.d/97-bluetooth-serial.rules (ASCII text)
      - etc/udev/rules.d/99-fuse.rules (ASCII text)
      - etc/udev/rules.d/device-mapper.rules (ASCII text)
    - etc/udev/udev.conf (ASCII text)
- **home/**
- init (symbolic link to sbin/init)
- **lib/**
  - lib/Data_Signature (data)
  - lib/SigFileList (ASCII text)
  - lib/ld-uClibc-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), static-pie linked, stripped)
  - lib/ld-uClibc.so.0 (symbolic link to ld-uClibc-0.9.33.2.so)
  - lib/libc.so.0 (symbolic link to libuClibc-0.9.33.2.so)
  - lib/libcrypt-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter ld-uClibc.so.0, stripped)
  - lib/libcrypt.so.0 (symbolic link to libcrypt-0.9.33.2.so)
  - lib/libdl-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter ld-uClibc.so.0, stripped)
  - lib/libdl.so.0 (symbolic link to libdl-0.9.33.2.so)
  - lib/libgcc_s.so.1 (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, stripped)
  - lib/libhive_RES.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, stripped)
  - lib/libhive_common.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, not stripped)
  - lib/libm-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter ld-uClibc.so.0, stripped)
  - lib/libm.so.0 (symbolic link to libm-0.9.33.2.so)
  - lib/libpthread-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter ld-uClibc.so.0, stripped)
  - lib/libpthread.so.0 (symbolic link to libpthread-0.9.33.2.so)
  - lib/librt-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter ld-uClibc.so.0, stripped)
  - lib/librt.so.0 (symbolic link to librt-0.9.33.2.so)
  - lib/libstdc++.so.6 (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, stripped)
  - lib/libthread_db-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter ld-uClibc.so.0, stripped)
  - lib/libthread_db.so.1 (symbolic link to libthread_db-0.9.33.2.so)
  - lib/libuClibc-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter ld-uClibc.so.0, stripped)
  - lib/libutil-0.9.33.2.so (ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter ld-uClibc.so.0, stripped)
  - lib/libutil.so.0 (symbolic link to libutil-0.9.33.2.so)
- linuxrc (symbolic link to bin/busybox)
- **mnt/**
  - **mnt/custom/**
  - **mnt/dvs/**
  - **mnt/logo/**
  - **mnt/mtd/**
    - **mnt/mtd/Config/**
      - **mnt/mtd/Config/ppp/**
    - **mnt/mtd/ppp/**
  - **mnt/nfs/**
  - **mnt/web/**
- **nfs/**
- **proc/**
  - **proc/dahua/**
- **root/**
- **sbin/**
  - sbin/3gpp (symbolic link to ./pppd)
  - sbin/Data_Signature (data)
  - sbin/SigFileList (ASCII text)
  - sbin/chat (symbolic link to ../bin/busybox)
  - sbin/depmod (symbolic link to ../bin/busybox)
  - sbin/dvrhelper (symbolic link to ../bin/busybox)
  - sbin/fdisk (symbolic link to ../bin/busybox)
  - sbin/getty (symbolic link to ../bin/busybox)
  - sbin/halt (symbolic link to ../bin/busybox)
  - sbin/hdparm (symbolic link to ../bin/busybox)
  - sbin/ifconfig (symbolic link to ../bin/busybox)
  - sbin/ifdown (symbolic link to ../bin/busybox)
  - sbin/ifup (symbolic link to ../bin/busybox)
  - sbin/inetd (symbolic link to ../bin/busybox)
  - sbin/init (symbolic link to ../bin/busybox)
  - sbin/insmod (symbolic link to ../bin/busybox)
  - sbin/lsmod (symbolic link to ../bin/busybox)
  - sbin/lspci (symbolic link to ../bin/busybox)
  - sbin/lsusb (symbolic link to ../bin/busybox)
  - sbin/makedevs (symbolic link to ../bin/busybox)
  - sbin/mdev (symbolic link to ../bin/busybox)
  - sbin/modprobe (symbolic link to ../bin/busybox)
  - sbin/net3g (symbolic link to ../bin/busybox)
  - sbin/netinit (symbolic link to ../bin/busybox)
  - sbin/netinit6 (symbolic link to ../bin/busybox)
  - sbin/poweroff (symbolic link to ../bin/busybox)
  - sbin/pppd (symbolic link to ../bin/busybox)
  - sbin/pppoe (symbolic link to ../bin/busybox)
  - sbin/pppoe-start (POSIX shell script, ASCII text executable)
  - sbin/reboot (symbolic link to ../bin/busybox)
  - sbin/rmmod (symbolic link to ../bin/busybox)
  - sbin/route (symbolic link to ../bin/busybox)
  - sbin/snmpd (symbolic link to ../var/Challenge)
  - sbin/upgraded (symbolic link to ../bin/busybox)
  - sbin/upnp_tv_ctrlpt (symbolic link to ../bin/busybox)
- **share/**
- **slave/**
- **sys/**
- **tmp/**
  - tmp/daemon (ASCII text)
  - tmp/daemon1 (Bourne-Again shell script, ASCII text executable)
  - tmp/daemon2 (ASCII text)
  - **tmp/wireless/**
    - tmp/wireless/1 (empty)
    - tmp/wireless/108 (empty)
    - tmp/wireless/81 (empty)
    - tmp/wireless/99 (empty)
- **usr/**
  - usr/Data_Signature (data)
  - usr/SigFileList (ASCII text)
  - **usr/bin/**
    - usr/bin/Challenge (ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped)
    - usr/bin/DahuaExec (ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped)
    - **usr/bin/lua/**
      - usr/bin/lua/ATMCtrl.lua (ISO-8859 text, with CRLF line terminators)
      - usr/bin/lua/ATMHead.lua (ISO-8859 text, with CRLF line terminators)
      - usr/bin/lua/LiveUpdate.lua (ISO-8859 text)
      - usr/bin/lua/PTZCtrl.lua (ISO-8859 text, with CRLF line terminators)
      - **usr/bin/lua/com/**
        - usr/bin/lua/com/ParseKLPOSStr.lua (ISO-8859 text, with CRLF line terminators)
      - usr/bin/lua/compat-5.1.lua (ASCII text)
      - usr/bin/lua/init.lua (ISO-8859 text, with CRLF line terminators)
      - **usr/bin/lua/ptz/**
        - usr/bin/lua/ptz/AD1641M.lua (ISO-8859 text)
        - usr/bin/lua/ptz/ADMatrix.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Banknote.lua (ISO-8859 text)
        - usr/bin/lua/ptz/CATU.lua (ISO-8859 text)
        - usr/bin/lua/ptz/CP-CVI.lua (ISO-8859 text)
        - usr/bin/lua/ptz/CP-CVI2.0.lua (ISO-8859 text)
        - usr/bin/lua/ptz/DH-CC440.lua (ISO-8859 text)
        - usr/bin/lua/ptz/DH-MATRIX.lua (ISO-8859 text)
        - usr/bin/lua/ptz/DH-SD1.lua (ISO-8859 text)
        - usr/bin/lua/ptz/DH-SD2.lua (ISO-8859 text)
        - usr/bin/lua/ptz/EPTZ.lua (ISO-8859 text)
        - usr/bin/lua/ptz/General.lua (ISO-8859 text)
        - usr/bin/lua/ptz/HAIYU.lua (ISO-8859 text)
        - usr/bin/lua/ptz/HY.lua (ISO-8859 text)
        - usr/bin/lua/ptz/LG.lua (ISO-8859 text)
        - usr/bin/lua/ptz/LiLin.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Mercer-1.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Mercer.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PANASONIC.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PELCOD-MING.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PELCOD-S.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PELCOD-S1.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PHILIPS.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PIH-717.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Pe5051k.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Pelco-9750.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoASCII.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoD-DON.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoD.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoD1.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoD1_Tour.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoD_Tour.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoP-A.lua (Non-ISO extended-ASCII text)
        - usr/bin/lua/ptz/PelcoP-HK.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoP-SD.lua (ISO-8859 text)
        - usr/bin/lua/ptz/PelcoP.lua (Non-ISO extended-ASCII text)
        - usr/bin/lua/ptz/PelcoP1-A.lua (Non-ISO extended-ASCII text)
        - usr/bin/lua/ptz/PelcoP1.lua (Non-ISO extended-ASCII text)
        - usr/bin/lua/ptz/PelcoP5.lua (ISO-8859 text)
        - usr/bin/lua/ptz/QT-2XXD.lua (ISO-8859 text)
        - usr/bin/lua/ptz/RM110.lua (ISO-8859 text)
        - usr/bin/lua/ptz/SAE.lua (ISO-8859 text)
        - usr/bin/lua/ptz/SANLI.lua (ISO-8859 text)
        - usr/bin/lua/ptz/SANTACHI.lua (ISO-8859 text)
        - usr/bin/lua/ptz/SHARP.lua (ASCII text)
        - usr/bin/lua/ptz/SIERA-D.lua (ISO-8859 text)
        - usr/bin/lua/ptz/SIERA-P.lua (ISO-8859 text)
        - usr/bin/lua/ptz/SONY.lua (ISO-8859 text)
        - usr/bin/lua/ptz/SUNKWANG.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Samsung.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Videon-X.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Videon_D.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Videon_P.lua (ISO-8859 text)
        - usr/bin/lua/ptz/WV-CS850I.lua (ISO-8859 text)
        - usr/bin/lua/ptz/WV-CS850II.lua (ISO-8859 text)
        - usr/bin/lua/ptz/WV-CS950.lua (ISO-8859 text)
        - usr/bin/lua/ptz/Yaan.lua (ISO-8859 text)
      - usr/bin/lua/utils.lua (ISO-8859 text, with CRLF line terminators)
    - **usr/bin/secboot/**
      - usr/bin/secboot/public.pem (ASCII text)
    - **usr/bin/ssl/**
      - usr/bin/ssl/pwdreset.pem (ASCII text)
  - **usr/data/**
    - usr/data/CustomConfig (ISO-8859 text)
    - **usr/data/Data/**
      - **usr/data/Data/DeviceSecurity/**
        - usr/data/Data/DeviceSecurity/PatternNormal.png (PNG image data, 70 x 70, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/PatternSelect.png (PNG image data, 70 x 70, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/device_init_step1.png (PNG image data, 30 x 30, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/device_init_step1_finish.png (PNG image data, 30 x 30, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/device_init_step2.png (PNG image data, 30 x 30, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/device_init_step2_finish.png (PNG image data, 30 x 30, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/device_init_step3.png (PNG image data, 30 x 30, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/device_init_step3_finish.png (PNG image data, 30 x 30, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/headPic.png (PNG image data, 80 x 80, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress0.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress1.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress2.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress3.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress4.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress5.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress6.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress7.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress8.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/DeviceSecurity/progress9.png (PNG image data, 580 x 14, 8-bit colormap, non-interlaced)
      - usr/data/Data/Font.bin (data)
      - usr/data/Data/FontSmallEn.bin (data)
      - **usr/data/Data/Intell/**
        - usr/data/Data/Intell/CrossLineDetection.png (PNG image data, 62 x 62, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/CrossRegionDetection.png (PNG image data, 62 x 62, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/LeftDetection.png (PNG image data, 62 x 62, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/TakenAwayDetection.png (PNG image data, 62 x 62, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/bmp_intellback.png (PNG image data, 150 x 200, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/button_set_disable.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, cbSize 1656, bits offset 1078)
        - usr/data/Data/Intell/button_set_normal.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, cbSize 1656, bits offset 1078)
        - usr/data/Data/Intell/button_set_push.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, cbSize 1656, bits offset 1078)
        - usr/data/Data/Intell/checkbox_intelli_0_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 23 important colors, cbSize 676, bits offset 146)
        - usr/data/Data/Intell/checkbox_intelli_0_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 23 important colors, cbSize 676, bits offset 146)
        - usr/data/Data/Intell/checkbox_intelli_1_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 35 important colors, cbSize 724, bits offset 194)
        - usr/data/Data/Intell/checkbox_intelli_1_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 35 important colors, cbSize 724, bits offset 194)
        - usr/data/Data/Intell/checkbox_intelli_disable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/checkbox_intelli_disableselect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/checkbox_intelli_enable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/checkbox_intelli_enableselect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/Intell/delete_normal.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, cbSize 1656, bits offset 1078)
        - usr/data/Data/Intell/delete_select.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, cbSize 1656, bits offset 1078)
        - usr/data/Data/Intell/filteredit_normal.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, cbSize 1656, bits offset 1078)
        - usr/data/Data/Intell/filteredit_select.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, cbSize 1656, bits offset 1078)
      - **usr/data/Data/NavigationBar/**
        - usr/data/Data/NavigationBar/Separator.png (PNG image data, 8 x 59, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/alert_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/alert_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/channel_info_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/channel_info_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/channel_tree_normal.png (PNG image data, 36 x 31, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/NavigationBar/channel_tree_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/collect_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/collect_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/colorSet_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/colorSet_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/disk_error.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/disk_error_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/disk_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/disk_notexist.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/disk_notexist_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/disk_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/home_normal.png (PNG image data, 80 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/home_select.png (PNG image data, 80 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/left_normal.png (PNG image data, 30 x 58, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/left_select.png (PNG image data, 30 x 58, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/menu_exp.png (PNG image data, 900 x 58, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/net_abort.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/net_abort_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/net_arp.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/net_arp_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/network_connected_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/network_connected_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/next_screen_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/next_screen_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/playback_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/playback_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/prev_screen_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/prev_screen_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/ptz_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/ptz_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/remote_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/remote_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/right_normal.png (PNG image data, 30 x 58, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/right_select.png (PNG image data, 30 x 58, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/tour_disable_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/tour_disable_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/tour_enable_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/tour_enable_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/usb_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/usb_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows16_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows16_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows1_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows1_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows25_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows25_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows32_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows32_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows4_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows4_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows6_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows6_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows8_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows8_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows9_normal.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/NavigationBar/windows9_select.png (PNG image data, 36 x 31, 8-bit colormap, non-interlaced)
      - **usr/data/Data/RealPlay/**
        - usr/data/Data/RealPlay/audio_close_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/audio_close_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/audio_disable.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/audio_open_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/audio_open_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/audiotalk_disable.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/audiotalk_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/audiotalk_push.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/audiotalk_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/block_disable.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/block_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/block_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/close_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/close_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/disable.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/hover.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/manual_snap_disable.png (PNG image data, 24 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/manual_snap_normal.png (PNG image data, 24 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/manual_snap_on_normal.png (PNG image data, 24 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/manual_snap_on_select.png (PNG image data, 24 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/manual_snap_selected.png (PNG image data, 24 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/menuplay_backcolor.png (PNG image data, 210 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/netcameraedit_disable.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/netcameraedit_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/netcameraedit_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/pause_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/pause_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/play_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/play_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/play_slider_background.png (PNG image data, 140 x 4, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/play_slider_elapsed.png (PNG image data, 140 x 4, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/realbk_disable.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/realbk_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/realbk_on_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/realbk_on_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/realbk_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/realplay_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/realplay_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/zoomin_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/zoomin_on_normal.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/zoomin_on_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/RealPlay/zoomin_selected.png (PNG image data, 29 x 29, 8-bit colormap, non-interlaced)
      - usr/data/Data/StringAll.7z (7-zip archive data, version 0.4)
      - **usr/data/Data/StringAll.7z.extracted/**
        - **usr/data/Data/StringAll.7z.extracted/0/**
          - usr/data/Data/StringAll.7z.extracted/0/StringAll (Unicode text, UTF-8 (with BOM) text, with very long lines (63563), with no line terminators)
      - **usr/data/Data/afterSaleService/**
        - usr/data/Data/afterSaleService/DahuaTechnology.png (PNG image data, 516 x 289, 8-bit colormap, non-interlaced)
        - usr/data/Data/afterSaleService/after_sale_service.png (PNG image data, 516 x 289, 8-bit colormap, non-interlaced)
        - usr/data/Data/afterSaleService/after_sale_service1.png (PNG image data, 31 x 31, 8-bit colormap, non-interlaced)
        - usr/data/Data/afterSaleService/after_sale_service2.png (PNG image data, 31 x 31, 8-bit colormap, non-interlaced)
      - **usr/data/Data/colorSettingPage/**
        - usr/data/Data/colorSettingPage/Brightness.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/Contrast.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/EqLevel.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/Gamma.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/Hue.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/Saturation.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/VideoPosition.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/colorSet_normal.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/plus0.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/plus1.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/plus2.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/plus3.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/reset0.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/reset1.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/reset2.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/reset3.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/subtractive0.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/subtractive1.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/subtractive2.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/subtractive3.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/unlock_disable.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/unlock_normal.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/colorSettingPage/unlock_select.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
      - **usr/data/Data/ctrl/**
        - **usr/data/Data/ctrl/button/**
          - usr/data/Data/ctrl/button/button_disable.bmp (PC bitmap, Windows 3.x format, 76 x 28 x 8, image size 2130, resolution 2834 x 2834 px/m, 100 important colors, cbSize 2584, bits offset 454)
          - usr/data/Data/ctrl/button/button_normal.bmp (PC bitmap, Windows 3.x format, 76 x 28 x 8, image size 2130, resolution 2834 x 2834 px/m, 110 important colors, cbSize 2624, bits offset 494)
          - usr/data/Data/ctrl/button/button_push.bmp (PC bitmap, Windows 3.x format, 76 x 28 x 8, image size 2130, resolution 2834 x 2834 px/m, 182 important colors, cbSize 2912, bits offset 782)
          - usr/data/Data/ctrl/button/button_select.bmp (PC bitmap, Windows 3.x format, 76 x 28 x 8, image size 2130, resolution 2834 x 2834 px/m, 157 important colors, cbSize 2812, bits offset 682)
      - **usr/data/Data/cursors/**
        - usr/data/Data/cursors/arrow.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @2x4)
        - usr/data/Data/cursors/busy.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @16x16)
        - usr/data/Data/cursors/hand.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @1x1)
        - usr/data/Data/cursors/move.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @16x16)
        - usr/data/Data/cursors/size1.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @16x16)
        - usr/data/Data/cursors/size2.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @15x16)
        - usr/data/Data/cursors/size3.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @16x16)
        - usr/data/Data/cursors/size4.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @16x16)
        - usr/data/Data/cursors/wait.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @2x4)
        - usr/data/Data/cursors/zoomin.cur (MS Windows cursor resource - 1 icon, 32x32, hotspot @9x8)
      - **usr/data/Data/desktopPage/**
        - usr/data/Data/desktopPage/3G_pppon.bmp (PC bitmap, Windows 3.x format, 29 x 29 x 8, image size 930, resolution 11808 x 11808 px/m, 242 important colors, cbSize 1952, bits offset 1022)
        - usr/data/Data/desktopPage/4G_pppon.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 3779 x 3779 px/m, 129 important colors, cbSize 1148, bits offset 570)
        - usr/data/Data/desktopPage/channel_state_lock.bmp (PC bitmap, Windows 3.x format, 108 x 24 x 16, image size 5186, resolution 2834 x 2834 px/m, cbSize 5240, bits offset 54)
        - usr/data/Data/desktopPage/channel_state_mtd.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 164 important colors, cbSize 1288, bits offset 710)
        - usr/data/Data/desktopPage/channel_state_vls.bmp (PC bitmap, Windows 3.x format, 108 x 24 x 16, image size 5186, resolution 2834 x 2834 px/m, cbSize 5240, bits offset 54)
        - usr/data/Data/desktopPage/tour_disable.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 114 important colors, cbSize 1088, bits offset 510)
        - usr/data/Data/desktopPage/tour_enable.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 108 important colors, cbSize 1064, bits offset 486)
        - usr/data/Data/desktopPage/wifi_enable.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 3779 x 3779 px/m, 189 important colors, cbSize 1388, bits offset 810)
      - **usr/data/Data/exitPage/**
        - usr/data/Data/exitPage/logout1.png (PNG image data, 90 x 90, 8-bit colormap, non-interlaced)
        - usr/data/Data/exitPage/logout2.png (PNG image data, 90 x 90, 8-bit colormap, non-interlaced)
        - usr/data/Data/exitPage/reboot1.png (PNG image data, 90 x 90, 8-bit colormap, non-interlaced)
        - usr/data/Data/exitPage/reboot2.png (PNG image data, 90 x 90, 8-bit colormap, non-interlaced)
        - usr/data/Data/exitPage/shutdown1.png (PNG image data, 90 x 90, 8-bit colormap, non-interlaced)
        - usr/data/Data/exitPage/shutdown2.png (PNG image data, 90 x 90, 8-bit colormap, non-interlaced)
      - **usr/data/Data/faceplayer/**
        - usr/data/Data/faceplayer/face_export_normal.png (PNG image data, 128 x 38, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/face_export_select.png (PNG image data, 128 x 38, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/face_search_disable.png (PNG image data, 307 x 38, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/face_search_normal.png (PNG image data, 307 x 38, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/face_search_select.png (PNG image data, 307 x 38, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/firstpage_disable.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 24 important colors, cbSize 936, bits offset 150)
        - usr/data/Data/faceplayer/firstpage_normal.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 23 important colors, cbSize 932, bits offset 146)
        - usr/data/Data/faceplayer/firstpage_push.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 14 important colors, cbSize 896, bits offset 110)
        - usr/data/Data/faceplayer/firstpage_select.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 14 important colors, cbSize 896, bits offset 110)
        - usr/data/Data/faceplayer/lastpage_disable.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 24 important colors, cbSize 936, bits offset 150)
        - usr/data/Data/faceplayer/lastpage_normal.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 23 important colors, cbSize 932, bits offset 146)
        - usr/data/Data/faceplayer/lastpage_push.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 14 important colors, cbSize 896, bits offset 110)
        - usr/data/Data/faceplayer/lastpage_select.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 14 important colors, cbSize 896, bits offset 110)
        - usr/data/Data/faceplayer/left_select.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 14 important colors, cbSize 896, bits offset 110)
        - usr/data/Data/faceplayer/play_back_disable.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_back_normal.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_back_pause_disable.bmp (PC bitmap, Windows 3.x format, 42 x 33 x 8, image size 1454, resolution 2834 x 2834 px/m, cbSize 2532, bits offset 1078)
        - usr/data/Data/faceplayer/play_back_pause_normal.bmp (PC bitmap, Windows 3.x format, 42 x 33 x 8, image size 1454, resolution 2834 x 2834 px/m, cbSize 2532, bits offset 1078)
        - usr/data/Data/faceplayer/play_back_pause_push.bmp (PC bitmap, Windows 3.x format, 42 x 33 x 8, image size 1454, resolution 2834 x 2834 px/m, cbSize 2532, bits offset 1078)
        - usr/data/Data/faceplayer/play_back_pause_select.bmp (PC bitmap, Windows 3.x format, 42 x 33 x 8, image size 1454, resolution 2834 x 2834 px/m, cbSize 2532, bits offset 1078)
        - usr/data/Data/faceplayer/play_back_push.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_back_select.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_fast_disable.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_fast_normal.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_fast_push.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_fast_select.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_nextframe_disable.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_nextframe_normal.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_nextframe_push.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_nextframe_select.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_pause_disable.bmp (PC bitmap, Windows 3.x format, 41 x 33 x 8, image size 1454, resolution 2834 x 2834 px/m, cbSize 2532, bits offset 1078)
        - usr/data/Data/faceplayer/play_pause_normal.bmp (PC bitmap, Windows 3.x format, 41 x 33 x 8, image size 1454, resolution 2834 x 2834 px/m, cbSize 2532, bits offset 1078)
        - usr/data/Data/faceplayer/play_pause_push.bmp (PC bitmap, Windows 3.x format, 41 x 33 x 8, image size 1454, resolution 2834 x 2834 px/m, cbSize 2532, bits offset 1078)
        - usr/data/Data/faceplayer/play_pause_select.bmp (PC bitmap, Windows 3.x format, 41 x 33 x 8, image size 1454, resolution 2834 x 2834 px/m, cbSize 2532, bits offset 1078)
        - usr/data/Data/faceplayer/play_preframe_disable.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_preframe_normal.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_preframe_push.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_preframe_select.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_slow_disable.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_slow_normal.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_slow_push.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_slow_select.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_start_disable.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_start_normal.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_start_push.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_start_select.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_stop_disable.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_stop_normal.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_stop_push.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_stop_select.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_volume_background.png (PNG image data, 62 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_volume_disable.bmp (PC bitmap, Windows 3.x format, 9 x 17 x 8, image size 206, resolution 2834 x 2834 px/m, 42 important colors, cbSize 428, bits offset 222)
        - usr/data/Data/faceplayer/play_volume_elapsed.png (PNG image data, 62 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/faceplayer/play_volume_normal.bmp (PC bitmap, Windows 3.x format, 9 x 17 x 8, image size 206, resolution 2834 x 2834 px/m, 39 important colors, cbSize 416, bits offset 210)
        - usr/data/Data/faceplayer/play_volume_select.bmp (PC bitmap, Windows 3.x format, 9 x 17 x 8, image size 206, resolution 2834 x 2834 px/m, 77 important colors, cbSize 568, bits offset 362)
        - usr/data/Data/faceplayer/right_select.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 14 important colors, cbSize 896, bits offset 110)
      - **usr/data/Data/guiCtrls/**
        - usr/data/Data/guiCtrls/disable_select.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/expand1.bmp (PC bitmap, Windows 3.x format, 19 x 21 x 8, image size 422, resolution 2834 x 2834 px/m, 44 important colors, cbSize 652, bits offset 230)
        - usr/data/Data/guiCtrls/expand2.bmp (PC bitmap, Windows 3.x format, 19 x 21 x 8, image size 422, resolution 2834 x 2834 px/m, 56 important colors, cbSize 700, bits offset 278)
        - usr/data/Data/guiCtrls/netCameraButton.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 11808 x 11808 px/m, 39 important colors, cbSize 740, bits offset 210)
        - usr/data/Data/guiCtrls/password_tip_disable.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/password_tip_normal.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/password_tip_select.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/retrieve_password_disable.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/retrieve_password_normal.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/retrieve_password_select.png (PNG image data, 31 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/select_hover.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/select_hover_noamal.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/shrink1.bmp (PC bitmap, Windows 3.x format, 19 x 21 x 8, image size 422, resolution 2834 x 2834 px/m, 43 important colors, cbSize 648, bits offset 226)
        - usr/data/Data/guiCtrls/shrink2.bmp (PC bitmap, Windows 3.x format, 19 x 21 x 8, image size 422, resolution 2834 x 2834 px/m, 80 important colors, cbSize 796, bits offset 374)
        - usr/data/Data/guiCtrls/signal_select.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/smart_disable.png (PNG image data, 20 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/smart_error.png (PNG image data, 20 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/smart_ok.png (PNG image data, 20 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/guiCtrls/zhaohuimima_disable.png (PNG image data, 31 x 29, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/guiCtrls/zhaohuimima_normal.png (PNG image data, 31 x 29, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/guiCtrls/zhaohuimima_select.png (PNG image data, 31 x 29, 8-bit/color RGB, non-interlaced)
      - **usr/data/Data/infoOnlineUserPage/**
        - usr/data/Data/infoOnlineUserPage/shield_normal.png (PNG image data, 24 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/infoOnlineUserPage/shield_push.png (PNG image data, 24 x 20, 8-bit colormap, non-interlaced)
      - **usr/data/Data/mainMenu/**
        - usr/data/Data/mainMenu/16split_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/1split_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/3G.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/4split_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/6split_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/8split_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/9split_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/autoPtz_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/blank_normal.bmp (PC bitmap, Windows 3.x format, 17 x 17 x 8, image size 342, resolution 2834 x 2834 px/m, 4 important colors, cbSize 412, bits offset 70)
        - usr/data/Data/mainMenu/cameraattribute_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/colorSet_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/config_guide_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/customsplit_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/face_search.bmp (PC bitmap, Windows 3.x format, 17 x 17 x 8, image size 342, resolution 2834 x 2834 px/m, 103 important colors, cbSize 808, bits offset 466)
        - usr/data/Data/mainMenu/face_search.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/main_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/matrix_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/netCamera_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/next_screen_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/originRate_normal.bmp (PC bitmap, Windows 3.x format, 17 x 17 x 8, image size 342, resolution 2834 x 2834 px/m, 29 important colors, cbSize 512, bits offset 170)
        - usr/data/Data/mainMenu/outmode_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/previous_screen_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/ptz_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/record_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/mainMenu/search_normal.png (PNG image data, 17 x 17, 8-bit colormap, non-interlaced)
      - **usr/data/Data/mainPage/**
        - usr/data/Data/mainPage/advanced1.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/advanced2.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, cbSize 7480, bits offset 1078)
        - usr/data/Data/mainPage/backup1.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/backup2.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/config1.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/config2.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/exit1.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/exit2.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/info1.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/info2.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/search1.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
        - usr/data/Data/mainPage/search2.bmp (PC bitmap, Windows 3.x format, 80 x 80 x 8, image size 6402, resolution 2795 x 2795 px/m, 255 important colors, cbSize 7476, bits offset 1074)
      - **usr/data/Data/menu/**
        - usr/data/Data/menu/tpl_menu_bar.bmp (PC bitmap, Windows 3.x format, 72 x 89 x 8, image size 6408, resolution 11811 x 11811 px/m, 256 important colors, cbSize 7486, bits offset 1078)
        - usr/data/Data/menu/tpl_menu_popup_item2.bmp (PC bitmap, Windows 3.x format, 128 x 30 x 8, image size 3840, resolution 11811 x 11811 px/m, 256 important colors, cbSize 4918, bits offset 1078)
        - usr/data/Data/menu/tpl_menu_popup_with_title.bmp (PC bitmap, Windows 3.x format, 128 x 128 x 8, image size 16384, resolution 11811 x 11811 px/m, 256 important colors, cbSize 17462, bits offset 1078)
        - usr/data/Data/menu/tpl_menu_popup_without_title.bmp (PC bitmap, Windows 3.x format, 128 x 64 x 24, image size 24578, resolution 2834 x 2834 px/m, cbSize 24632, bits offset 54)
      - **usr/data/Data/motionSetPage/**
        - usr/data/Data/motionSetPage/blue_down.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/blue_normal.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/blue_select.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/green_down.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/green_normal.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/green_select.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/orange_down.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/orange_normal.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/orange_select.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/yellow_down.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/yellow_normal.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
        - usr/data/Data/motionSetPage/yellow_select.png (PNG image data, 63 x 50, 8-bit colormap, non-interlaced)
      - **usr/data/Data/netCameraPage/**
        - usr/data/Data/netCameraPage/remotdev_editipc_disable.png (PNG image data, 24 x 20, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/netCameraPage/remotdev_editipc_normal.png (PNG image data, 24 x 20, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/netCameraPage/remotdev_editipc_selected.png (PNG image data, 24 x 20, 8-bit/color RGB, non-interlaced)
      - **usr/data/Data/player/**
        - usr/data/Data/player/IVS_select.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/advanced_search_disable.png (PNG image data, 52 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/advanced_search_normal.png (PNG image data, 52 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/advanced_search_select.png (PNG image data, 52 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/back.bmp (PC bitmap, Windows 3.x format, 16 x 15 x 8, image size 242, resolution 2834 x 2834 px/m, 7 important colors, cbSize 324, bits offset 82)
        - usr/data/Data/player/bmp_backup.bmp (PC bitmap, Windows 3.x format, 20 x 20 x 8, image size 402, resolution 3779 x 3779 px/m, 5 important colors, cbSize 476, bits offset 74)
        - usr/data/Data/player/bmp_backup.png (PNG image data, 20 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/bmp_card.png (PNG image data, 30 x 27, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/bmp_channel.png (PNG image data, 34 x 27, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/bmp_time.png (PNG image data, 28 x 28, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/bmp_txn_error.png (PNG image data, 30 x 27, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/bmp_txn_money.png (PNG image data, 30 x 27, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/bmp_txn_type.png (PNG image data, 30 x 27, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/button_close_disabled.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 5 important colors, cbSize 652, bits offset 74)
        - usr/data/Data/player/button_close_normal.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 4 important colors, cbSize 648, bits offset 70)
        - usr/data/Data/player/button_close_pushed.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 66 important colors, cbSize 896, bits offset 318)
        - usr/data/Data/player/button_close_selected.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 22 important colors, cbSize 720, bits offset 142)
        - **usr/data/Data/player/calendar/**
          - usr/data/Data/player/calendar/arraw_disable.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 98 important colors, cbSize 1024, bits offset 446)
          - usr/data/Data/player/calendar/arraw_disable1.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 99 important colors, cbSize 1028, bits offset 450)
          - usr/data/Data/player/calendar/arraw_normal.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 103 important colors, cbSize 1044, bits offset 466)
          - usr/data/Data/player/calendar/arraw_normal1.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 98 important colors, cbSize 1024, bits offset 446)
          - usr/data/Data/player/calendar/arraw_push.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 153 important colors, cbSize 1244, bits offset 666)
          - usr/data/Data/player/calendar/arraw_push1.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 132 important colors, cbSize 1160, bits offset 582)
          - usr/data/Data/player/calendar/arraw_select.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 152 important colors, cbSize 1240, bits offset 662)
          - usr/data/Data/player/calendar/arraw_select1.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 131 important colors, cbSize 1156, bits offset 578)
          - usr/data/Data/player/calendar/buttom_left.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
          - usr/data/Data/player/calendar/buttom_right.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
          - usr/data/Data/player/calendar/button_left.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
          - usr/data/Data/player/calendar/button_right.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
          - usr/data/Data/player/calendar/day_normal.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 4 important colors, cbSize 648, bits offset 70)
          - usr/data/Data/player/calendar/day_recday.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 5 important colors, cbSize 652, bits offset 74)
          - usr/data/Data/player/calendar/day_selected.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 4 important colors, cbSize 648, bits offset 70)
        - usr/data/Data/player/camera_disable.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/camera_normal.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/camera_push.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/camera_select.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/checkbox_alarm_0_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 77 important colors, cbSize 892, bits offset 362)
        - usr/data/Data/player/checkbox_alarm_0_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 78 important colors, cbSize 896, bits offset 366)
        - usr/data/Data/player/checkbox_alarm_1_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 136 important colors, cbSize 1128, bits offset 598)
        - usr/data/Data/player/checkbox_alarm_1_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 137 important colors, cbSize 1132, bits offset 602)
        - usr/data/Data/player/checkbox_all_0_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 75 important colors, cbSize 884, bits offset 354)
        - usr/data/Data/player/checkbox_all_0_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 76 important colors, cbSize 888, bits offset 358)
        - usr/data/Data/player/checkbox_all_1_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 128 important colors, cbSize 1096, bits offset 566)
        - usr/data/Data/player/checkbox_all_1_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 129 important colors, cbSize 1100, bits offset 570)
        - usr/data/Data/player/checkbox_common_0_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 71 important colors, cbSize 868, bits offset 338)
        - usr/data/Data/player/checkbox_common_0_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 72 important colors, cbSize 872, bits offset 342)
        - usr/data/Data/player/checkbox_common_1_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 111 important colors, cbSize 1028, bits offset 498)
        - usr/data/Data/player/checkbox_common_1_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 112 important colors, cbSize 1032, bits offset 502)
        - usr/data/Data/player/checkbox_motion_0_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 72 important colors, cbSize 872, bits offset 342)
        - usr/data/Data/player/checkbox_motion_0_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 73 important colors, cbSize 876, bits offset 346)
        - usr/data/Data/player/checkbox_motion_1_disable.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 116 important colors, cbSize 1048, bits offset 518)
        - usr/data/Data/player/checkbox_motion_1_normal.bmp (PC bitmap, Windows 3.x format, 22 x 22 x 8, image size 530, resolution 2834 x 2834 px/m, 117 important colors, cbSize 1052, bits offset 522)
        - usr/data/Data/player/clip_disable.png (PNG image data, 46 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/clip_end_normal.bmp (PC bitmap, Windows 3.x format, 9 x 16 x 8, image size 194, resolution 2834 x 2834 px/m, 73 important colors, cbSize 540, bits offset 346)
        - usr/data/Data/player/clip_normal.png (PNG image data, 46 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/clip_push.png (PNG image data, 46 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/clip_save_disable.png (PNG image data, 46 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/clip_save_normal.png (PNG image data, 46 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/clip_save_push.png (PNG image data, 46 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/clip_save_select.png (PNG image data, 46 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/clip_select.png (PNG image data, 46 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/clip_start_normal.bmp (PC bitmap, Windows 3.x format, 9 x 16 x 8, image size 194, resolution 2834 x 2834 px/m, 73 important colors, cbSize 540, bits offset 346)
        - usr/data/Data/player/close_filelist_disable.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/close_filelist_normal.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/close_filelist_push.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/close_filelist_select.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/fast.bmp (PC bitmap, Windows 3.x format, 16 x 15 x 8, image size 242, resolution 11808 x 11808 px/m, cbSize 1320, bits offset 1078)
        - usr/data/Data/player/fastback.bmp (PC bitmap, Windows 3.x format, 16 x 15 x 8, image size 242, resolution 11808 x 11808 px/m, cbSize 1320, bits offset 1078)
        - usr/data/Data/player/fileLocked.bmp (PC bitmap, Windows 3.x format, 24 x 20 x 8, image size 482, resolution 2834 x 2834 px/m, 109 important colors, cbSize 972, bits offset 490)
        - usr/data/Data/player/file_list_disable.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/file_list_normal.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/file_list_push.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/file_list_select.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_1hr_disable.png (PNG image data, 49 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_1hr_normal.png (PNG image data, 49 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_1hr_push.png (PNG image data, 49 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_1hr_select.png (PNG image data, 49 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_24hr_disable.png (PNG image data, 50 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_24hr_normal.png (PNG image data, 50 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_24hr_push.png (PNG image data, 50 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_24hr_select.png (PNG image data, 50 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_2hr_disable.png (PNG image data, 49 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_2hr_normal.png (PNG image data, 49 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_2hr_push.png (PNG image data, 49 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_2hr_select.png (PNG image data, 49 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_30min_disable.png (PNG image data, 54 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_30min_normal.png (PNG image data, 54 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_30min_push.png (PNG image data, 54 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/grid_30min_select.png (PNG image data, 54 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/ivs_config.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/ivs_disable.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/ivs_normal.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/ivs_push.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/lockRecSearch_disable.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/lockRecSearch_normal.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/lockRecSearch_push.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/lockRecSearch_selected.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/pause.bmp (PC bitmap, Windows 3.x format, 16 x 15 x 8, image size 242, resolution 2834 x 2834 px/m, 5 important colors, cbSize 316, bits offset 74)
        - usr/data/Data/player/play.bmp (PC bitmap, Windows 3.x format, 16 x 15 x 8, image size 242, resolution 2834 x 2834 px/m, 7 important colors, cbSize 324, bits offset 82)
        - usr/data/Data/player/play_back_disable.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_back_normal.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_back_pause_disable.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_back_pause_normal.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_back_pause_push.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_back_pause_select.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_back_push.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_back_select.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_fast_disable.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_fast_normal.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_fast_push.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_fast_select.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_frame_bottom.png (PNG image data, 1024 x 57, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_frame_interval.png (PNG image data, 1024 x 7, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_frame_repeat.png (PNG image data, 1024 x 16, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_frame_top.png (PNG image data, 1024 x 23, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_nextday_disable.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_nextday_normal.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_nextday_push.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_nextday_select.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_nextframe_disable.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_nextframe_normal.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_nextframe_push.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_nextframe_select.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_pause_disable.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_pause_normal.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_pause_push.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_pause_select.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_preframe_disable.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_preframe_normal.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_preframe_push.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_preframe_select.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_prevday_disable.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_prevday_normal.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_prevday_push.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_prevday_select.png (PNG image data, 40 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_slider_background.png (PNG image data, 670 x 12, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_slider_elapsed.png (PNG image data, 670 x 12, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_slow_disable.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_slow_normal.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_slow_push.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_slow_select.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_start_disable.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_start_normal.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_start_push.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_start_select.png (PNG image data, 41 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_stop_disable.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_stop_normal.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_stop_push.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_stop_select.png (PNG image data, 42 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_volume_background.png (PNG image data, 62 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_volume_disable.bmp (PC bitmap, Windows 3.x format, 9 x 17 x 8, image size 206, resolution 2834 x 2834 px/m, 42 important colors, cbSize 428, bits offset 222)
        - usr/data/Data/player/play_volume_elapsed.png (PNG image data, 62 x 17, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/play_volume_normal.bmp (PC bitmap, Windows 3.x format, 9 x 17 x 8, image size 206, resolution 2834 x 2834 px/m, 39 important colors, cbSize 416, bits offset 210)
        - usr/data/Data/player/play_volume_select.bmp (PC bitmap, Windows 3.x format, 9 x 17 x 8, image size 206, resolution 2834 x 2834 px/m, 77 important colors, cbSize 568, bits offset 362)
        - usr/data/Data/player/reclock_disable.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/reclock_normal.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/reclock_push.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/reclock_selected.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/search_disable.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/search_normal.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/search_push.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/search_select.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/slicediv.png (PNG image data, 12 x 14, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/slow.bmp (PC bitmap, Windows 3.x format, 16 x 15 x 8, image size 242, resolution 2834 x 2834 px/m, 5 important colors, cbSize 316, bits offset 74)
        - usr/data/Data/player/slowback.bmp (PC bitmap, Windows 3.x format, 16 x 15 x 8, image size 242, resolution 2834 x 2834 px/m, 6 important colors, cbSize 320, bits offset 78)
        - usr/data/Data/player/sound_normal.png (PNG image data, 24 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/sound_select.png (PNG image data, 24 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/stop.bmp (PC bitmap, Windows 3.x format, 16 x 15 x 8, image size 242, resolution 2834 x 2834 px/m, 5 important colors, cbSize 316, bits offset 74)
        - usr/data/Data/player/tab10_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab10_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab11_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab11_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab12_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab12_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab13_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab13_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab14_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab14_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab15_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab15_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab16_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab16_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab1_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab1_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab2_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab2_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab3_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab3_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab4_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab4_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab5_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab5_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab6_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab6_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab7_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab7_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab8_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab8_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab9_normal.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab9_select.png (PNG image data, 46 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab_normal.png (PNG image data, 46 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tab_select.png (PNG image data, 46 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tag_list_disable.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tag_list_normal.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tag_list_push.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tag_list_select.png (PNG image data, 51 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tagadd_disable.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tagadd_normal.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tagadd_push.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tagadd_select.png (PNG image data, 34 x 33, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tagmanage_disable.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tagmanage_normal.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tagmanage_push.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/tagmanage_select.png (PNG image data, 45 x 29, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_16ch_disable.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_16ch_normal.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_16ch_push.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_16ch_select.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_1ch_disable.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_1ch_normal.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_1ch_push.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_1ch_select.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_4ch_disable.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_4ch_normal.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_4ch_push.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_4ch_select.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_9ch_disable.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_9ch_normal.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_9ch_push.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_9ch_select.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_fullscreen_disable.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_fullscreen_normal.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_fullscreen_push.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_fullscreen_select.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_selfdef_disable.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_selfdef_normal.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_selfdef_push.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
        - usr/data/Data/player/window_selfdef_select.png (PNG image data, 34 x 34, 8-bit colormap, non-interlaced)
      - **usr/data/Data/popup/**
        - usr/data/Data/popup/bmp_popup.bmp (PC bitmap, Windows 3.x format, 64 x 64 x 8, image size 4098, resolution 2834 x 2834 px/m, 79 important colors, cbSize 4468, bits offset 370)
      - **usr/data/Data/ptz/**
        - usr/data/Data/ptz/down0.png (PNG image data, 40 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/down1.png (PNG image data, 40 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/down2.png (PNG image data, 40 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/down3.png (PNG image data, 40 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/left0.png (PNG image data, 44 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/left1.png (PNG image data, 44 x 40, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/left2.png (PNG image data, 44 x 40, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/left3.png (PNG image data, 44 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/leftdown0.png (PNG image data, 47 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/leftdown1.png (PNG image data, 47 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/leftdown2.png (PNG image data, 47 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/leftdown3.png (PNG image data, 47 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/leftup0.png (PNG image data, 47 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/leftup1.png (PNG image data, 47 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/leftup2.png (PNG image data, 47 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/leftup3.png (PNG image data, 47 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/plus0.png (PNG image data, 32 x 32, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/plus1.png (PNG image data, 32 x 32, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/plus2.png (PNG image data, 32 x 32, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/plus3.png (PNG image data, 32 x 32, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/position0.png (PNG image data, 46 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/position1.png (PNG image data, 46 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/position2.png (PNG image data, 46 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/position3.png (PNG image data, 46 x 40, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/right0.png (PNG image data, 44 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/right1.png (PNG image data, 44 x 40, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/right2.png (PNG image data, 44 x 40, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/right3.png (PNG image data, 44 x 40, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/rightdown0.png (PNG image data, 47 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/rightdown1.png (PNG image data, 47 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/rightdown2.png (PNG image data, 47 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/rightdown3.png (PNG image data, 47 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/rightup0.png (PNG image data, 47 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/rightup1.png (PNG image data, 47 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/rightup2.png (PNG image data, 47 x 46, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/rightup3.png (PNG image data, 47 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/subtractive0.png (PNG image data, 32 x 32, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/subtractive1.png (PNG image data, 32 x 32, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/subtractive2.png (PNG image data, 32 x 32, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/subtractive3.png (PNG image data, 32 x 32, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/ptz/up0.png (PNG image data, 40 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/up1.png (PNG image data, 40 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/up2.png (PNG image data, 40 x 46, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptz/up3.png (PNG image data, 40 x 46, 8-bit colormap, non-interlaced)
      - **usr/data/Data/ptzext/**
        - usr/data/Data/ptzext/autopan_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/autopan_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/autopan_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/autopan_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/autoscan_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/autoscan_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/autoscan_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/autoscan_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/aux_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/aux_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/aux_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/aux_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/flip_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/flip_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/flip_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/flip_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/highspeed_disable.png (PNG image data, 40 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/highspeed_normal.png (PNG image data, 40 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/highspeed_push.png (PNG image data, 40 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/highspeed_select.png (PNG image data, 40 x 40, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/menu_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/menu_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/menu_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/menu_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/pattern_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/pattern_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/pattern_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/pattern_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/preset_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/preset_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/preset_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/preset_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/reset_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/reset_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/reset_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/reset_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/setting_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/setting_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/setting_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/setting_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/toleft_normal.png (PNG image data, 13 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/toleft_select.png (PNG image data, 13 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/toright_normal.png (PNG image data, 13 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/toright_select.png (PNG image data, 13 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/tour_disable.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/tour_normal.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/tour_push.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
        - usr/data/Data/ptzext/tour_select.png (PNG image data, 34 x 35, 8-bit colormap, non-interlaced)
      - **usr/data/Data/sharePicture/**
        - usr/data/Data/sharePicture/PcapInvalid.png (PNG image data, 24 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/PcapStart_normal.png (PNG image data, 24 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/PcapStart_select.png (PNG image data, 24 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/PcapStop_normal.png (PNG image data, 24 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/PcapStop_select.png (PNG image data, 24 x 20, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/bmp_frame.bmp (PC bitmap, Windows 3.x format, 216 x 112 x 16, image size 48386, resolution 2834 x 2834 px/m, cbSize 48440, bits offset 54)
        - usr/data/Data/sharePicture/bmp_tab.bmp (PC bitmap, Windows 3.x format, 256 x 28 x 8, image size 7170, resolution 2834 x 2834 px/m, 57 important colors, cbSize 7452, bits offset 282)
        - usr/data/Data/sharePicture/bmp_tip.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 95 important colors, cbSize 1012, bits offset 434)
        - usr/data/Data/sharePicture/bmp_tipbar.bmp (PC bitmap, Windows 3.x format, 72 x 62 x 8, image size 4466, resolution 2834 x 2834 px/m, 48 important colors, cbSize 4712, bits offset 246)
        - usr/data/Data/sharePicture/bmp_title.bmp (PC bitmap, Windows 3.x format, 152 x 112 x 16, image size 34050, resolution 2834 x 2834 px/m, cbSize 34104, bits offset 54)
        - usr/data/Data/sharePicture/button_close_disabled.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 5 important colors, cbSize 652, bits offset 74)
        - usr/data/Data/sharePicture/button_close_normal.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 4 important colors, cbSize 648, bits offset 70)
        - usr/data/Data/sharePicture/button_close_pushed.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 66 important colors, cbSize 896, bits offset 318)
        - usr/data/Data/sharePicture/button_close_selected.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 22 important colors, cbSize 720, bits offset 142)
        - usr/data/Data/sharePicture/button_disable.bmp (PC bitmap, Windows 3.x format, 76 x 26 x 8, image size 1978, resolution 11808 x 11808 px/m, 82 important colors, cbSize 2360, bits offset 382)
        - usr/data/Data/sharePicture/button_normal.bmp (PC bitmap, Windows 3.x format, 76 x 26 x 8, image size 1978, resolution 11808 x 11808 px/m, 89 important colors, cbSize 2388, bits offset 410)
        - usr/data/Data/sharePicture/button_normal_ex.png (PNG image data, 105 x 30, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/button_push.bmp (PC bitmap, Windows 3.x format, 76 x 26 x 8, image size 1978, resolution 11808 x 11808 px/m, 130 important colors, cbSize 2552, bits offset 574)
        - usr/data/Data/sharePicture/button_select.bmp (PC bitmap, Windows 3.x format, 76 x 26 x 8, image size 1978, resolution 11808 x 11808 px/m, 133 important colors, cbSize 2564, bits offset 586)
        - usr/data/Data/sharePicture/button_select_ex.png (PNG image data, 105 x 30, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/channel_state_lock.bmp (PC bitmap, Windows 3.x format, 108 x 24 x 16, image size 5186, resolution 2834 x 2834 px/m, cbSize 5240, bits offset 54)
        - usr/data/Data/sharePicture/channel_state_mtd.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 164 important colors, cbSize 1288, bits offset 710)
        - usr/data/Data/sharePicture/channel_state_record.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 233 important colors, cbSize 1564, bits offset 986)
        - usr/data/Data/sharePicture/channel_state_vls.bmp (PC bitmap, Windows 3.x format, 108 x 24 x 16, image size 5186, resolution 2834 x 2834 px/m, cbSize 5240, bits offset 54)
        - usr/data/Data/sharePicture/checkbox_select_hover.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/checkbox_select_large_hover.png (PNG image data, 28 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/checkbox_signal_large_select.png (PNG image data, 28 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/checkbox_signal_select.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/config_alarm0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 78 important colors, cbSize 944, bits offset 366)
        - usr/data/Data/sharePicture/config_chnname0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 255 important colors, cbSize 1652, bits offset 1074)
        - usr/data/Data/sharePicture/config_image0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 96 important colors, cbSize 1016, bits offset 438)
        - usr/data/Data/sharePicture/config_ipc0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 251 important colors, cbSize 1636, bits offset 1058)
        - usr/data/Data/sharePicture/config_md0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 9 important colors, cbSize 668, bits offset 90)
        - usr/data/Data/sharePicture/config_net0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 157 important colors, cbSize 1260, bits offset 682)
        - usr/data/Data/sharePicture/config_ptz0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 43 important colors, cbSize 804, bits offset 226)
        - usr/data/Data/sharePicture/config_storage0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 255 important colors, cbSize 1652, bits offset 1074)
        - usr/data/Data/sharePicture/config_sys0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 233 important colors, cbSize 1564, bits offset 986)
        - usr/data/Data/sharePicture/config_sysinfo0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 219 important colors, cbSize 1508, bits offset 930)
        - usr/data/Data/sharePicture/detail_normal.png (PNG image data, 24 x 20, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/detail_push.png (PNG image data, 24 x 20, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/detail_select.png (PNG image data, 24 x 20, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/dir.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/disable_large_normal.png (PNG image data, 28 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/disable_normal.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/dvr.bmp (PC bitmap, Windows 3.x format, 32 x 32 x 8, image size 1026, resolution 2834 x 2834 px/m, 38 important colors, cbSize 1232, bits offset 206)
        - usr/data/Data/sharePicture/file.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/gridLock.png (PNG image data, 27 x 17, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/gridLockSelected.png (PNG image data, 27 x 17, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/gridUnLock.png (PNG image data, 27 x 17, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/gridUnLockSelected.png (PNG image data, 27 x 17, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/info_bps0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 156 important colors, cbSize 1256, bits offset 678)
        - usr/data/Data/sharePicture/info_log0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 65 important colors, cbSize 892, bits offset 314)
        - usr/data/Data/sharePicture/info_netDetect0.bmp (PC bitmap, Windows 3.x format, 24 x 24 x 8, image size 578, resolution 2834 x 2834 px/m, 255 important colors, cbSize 1652, bits offset 1074)
        - usr/data/Data/sharePicture/input_control.png (PNG image data, 38 x 26, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/input_lowercase.png (PNG image data, 38 x 26, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/input_mark.png (PNG image data, 38 x 26, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/input_numeric.png (PNG image data, 38 x 26, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/input_pinyin.png (PNG image data, 38 x 26, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/input_uppercase.png (PNG image data, 38 x 26, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/left_disable.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, cbSize 1864, bits offset 1078)
        - usr/data/Data/sharePicture/left_normal.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 255 important colors, cbSize 1860, bits offset 1074)
        - usr/data/Data/sharePicture/left_push.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, cbSize 1864, bits offset 1078)
        - usr/data/Data/sharePicture/left_select.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, cbSize 1864, bits offset 1078)
        - usr/data/Data/sharePicture/menu_normal.png (PNG image data, 153 x 54, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/menu_tab_normal.png (PNG image data, 147 x 35, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/menu_tab_select.png (PNG image data, 147 x 35, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/play_search_disable.png (PNG image data, 19 x 19, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/play_search_normal.png (PNG image data, 19 x 19, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/play_search_push.png (PNG image data, 19 x 19, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/play_search_select.png (PNG image data, 19 x 19, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/radio_tab_normal.png (PNG image data, 127 x 35, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/radio_tab_select.png (PNG image data, 127 x 35, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/remotdev_del_disable.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/remotdev_del_normal.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/remotdev_del_selected.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/remotdev_edit_disable.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/remotdev_edit_normal.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/remotdev_edit_selected.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/remotdev_stat_disable.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/remotdev_stat_normal.png (PNG image data, 24 x 24, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/remote_info.alarm.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 172 important colors, cbSize 1528, bits offset 742)
        - usr/data/Data/sharePicture/remote_info.notsupport.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 13 important colors, cbSize 892, bits offset 106)
        - usr/data/Data/sharePicture/remote_info.support.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 92 important colors, cbSize 1208, bits offset 422)
        - usr/data/Data/sharePicture/reset0.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/reset1.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/reset2.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/reset3.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/reticle_state_bad.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 86 important colors, cbSize 1184, bits offset 398)
        - usr/data/Data/sharePicture/right_disable.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, cbSize 1864, bits offset 1078)
        - usr/data/Data/sharePicture/right_normal.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, 255 important colors, cbSize 1860, bits offset 1074)
        - usr/data/Data/sharePicture/right_push.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, cbSize 1864, bits offset 1078)
        - usr/data/Data/sharePicture/right_select.bmp (PC bitmap, Windows 3.x format, 28 x 28 x 8, image size 786, resolution 2834 x 2834 px/m, cbSize 1864, bits offset 1078)
        - usr/data/Data/sharePicture/signal1.bmp (PC bitmap, Windows 3.x format, 30 x 24 x 8, image size 770, resolution 2834 x 2834 px/m, 20 important colors, cbSize 904, bits offset 134)
        - usr/data/Data/sharePicture/signal2.bmp (PC bitmap, Windows 3.x format, 30 x 24 x 8, image size 770, resolution 2834 x 2834 px/m, 25 important colors, cbSize 924, bits offset 154)
        - usr/data/Data/sharePicture/signal3.bmp (PC bitmap, Windows 3.x format, 30 x 24 x 8, image size 770, resolution 2834 x 2834 px/m, 30 important colors, cbSize 944, bits offset 174)
        - usr/data/Data/sharePicture/signal4.bmp (PC bitmap, Windows 3.x format, 30 x 24 x 8, image size 770, resolution 2834 x 2834 px/m, 35 important colors, cbSize 964, bits offset 194)
        - usr/data/Data/sharePicture/signal5.bmp (PC bitmap, Windows 3.x format, 30 x 24 x 8, image size 770, resolution 2834 x 2834 px/m, 44 important colors, cbSize 1000, bits offset 230)
        - usr/data/Data/sharePicture/signal_select_large_normal.png (PNG image data, 28 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/signal_select_normal.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/sharePicture/start_normal.bmp (PC bitmap, Windows 3.x format, 24 x 20 x 8, image size 482, resolution 2834 x 2834 px/m, 5 important colors, cbSize 556, bits offset 74)
        - usr/data/Data/sharePicture/sub_window_bottom.png (PNG image data, 122 x 22, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/sub_window_top.png (PNG image data, 122 x 22, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/tip.bmp (PC bitmap, Windows 3.x format, 32 x 32 x 8, image size 1026, resolution 2833 x 2833 px/m, 215 important colors, cbSize 1940, bits offset 914)
        - usr/data/Data/sharePicture/view_disable.png (PNG image data, 24 x 24, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/view_normal.png (PNG image data, 24 x 24, 8-bit/color RGB, non-interlaced)
        - usr/data/Data/sharePicture/view_select.png (PNG image data, 24 x 24, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/vol_background.bmp (PC bitmap, Windows 3.x format, 105 x 20 x 8, image size 2162, resolution 2834 x 2834 px/m, 5 important colors, cbSize 2236, bits offset 74)
        - usr/data/Data/sharePicture/vol_disable.bmp (PC bitmap, Windows 3.x format, 6 x 20 x 8, image size 162, resolution 2834 x 2834 px/m, 32 important colors, cbSize 344, bits offset 182)
        - usr/data/Data/sharePicture/vol_elapsed.bmp (PC bitmap, Windows 3.x format, 105 x 20 x 8, image size 2162, resolution 2834 x 2834 px/m, 90 important colors, cbSize 2576, bits offset 414)
        - usr/data/Data/sharePicture/vol_normal.bmp (PC bitmap, Windows 3.x format, 6 x 20 x 8, image size 162, resolution 2834 x 2834 px/m, 44 important colors, cbSize 392, bits offset 230)
        - usr/data/Data/sharePicture/vol_select.bmp (PC bitmap, Windows 3.x format, 6 x 20 x 8, image size 162, resolution 2834 x 2834 px/m, 44 important colors, cbSize 392, bits offset 230)
        - usr/data/Data/sharePicture/window_bottom.png (PNG image data, 21 x 53, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/window_bottom1.png (PNG image data, 21 x 53, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/window_title.png (PNG image data, 188 x 32, 8-bit/color RGBA, non-interlaced)
        - usr/data/Data/sharePicture/window_top.png (PNG image data, 10 x 43, 8-bit colormap, non-interlaced)
      - **usr/data/Data/slider/**
        - usr/data/Data/slider/slider_line.bmp (PC bitmap, Windows 3.x format, 134 x 5 x 8, image size 682, resolution 2834 x 2834 px/m, 12 important colors, cbSize 784, bits offset 102)
        - usr/data/Data/slider/spot0.bmp (PC bitmap, Windows 3.x format, 14 x 14 x 8, image size 226, resolution 2834 x 2834 px/m, 33 important colors, cbSize 412, bits offset 186)
        - usr/data/Data/slider/spot1.bmp (PC bitmap, Windows 3.x format, 14 x 14 x 8, image size 226, resolution 2834 x 2834 px/m, 39 important colors, cbSize 436, bits offset 210)
        - usr/data/Data/slider/spot2.bmp (PC bitmap, Windows 3.x format, 14 x 14 x 8, image size 226, resolution 2834 x 2834 px/m, 31 important colors, cbSize 404, bits offset 178)
      - **usr/data/Data/storagePage/**
        - usr/data/Data/storagePage/ClearNormal.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/ClearSelected.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/SettingNormal.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/SettingSelected.png (PNG image data, 32 x 32, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkAlarmDisable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkAlarmDisableSelect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkAlarmEnable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkAlarmEnableSelect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkMDAlarmDisable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkMDAlarmDisableSelect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkMDAlarmEnable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkMDAlarmEnableSelect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkMDDisable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkMDDisableSelect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkMDEnable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkMDEnableSelect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkRegularDisable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkRegularDisableSelect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkRegularEnable.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
        - usr/data/Data/storagePage/checkRegularEnableSelect.png (PNG image data, 22 x 22, 8-bit colormap, non-interlaced)
      - **usr/data/Data/tab/**
        - usr/data/Data/tab/tab_normal.bmp (PC bitmap, Windows 3.x format, 147 x 35 x 8, image size 5182, resolution 2834 x 2834 px/m, 38 important colors, cbSize 5388, bits offset 206)
        - usr/data/Data/tab/tab_pushed.bmp (PC bitmap, Windows 3.x format, 147 x 35 x 8, image size 5182, resolution 2834 x 2834 px/m, 39 important colors, cbSize 5392, bits offset 210)
        - usr/data/Data/tab/tab_select.bmp (PC bitmap, Windows 3.x format, 147 x 35 x 8, image size 5182, resolution 2834 x 2834 px/m, 38 important colors, cbSize 5388, bits offset 206)
      - **usr/data/Data/textbox/**
        - usr/data/Data/textbox/textbox1.bmp (PC bitmap, Windows 3.x format, 128 x 128 x 8, image size 16386, resolution 2795 x 2795 px/m, 16 important colors, cbSize 16504, bits offset 118)
        - usr/data/Data/textbox/textbox2.bmp (PC bitmap, Windows 3.x format, 128 x 128 x 8, image size 16386, resolution 2795 x 2795 px/m, 16 important colors, cbSize 16504, bits offset 118)
      - **usr/data/Data/title48/**
        - usr/data/Data/title48/advanced1.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 254 important colors, cbSize 3376, bits offset 1070)
        - usr/data/Data/title48/advanced2.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, cbSize 3384, bits offset 1078)
        - usr/data/Data/title48/backup1.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 253 important colors, cbSize 3372, bits offset 1066)
        - usr/data/Data/title48/backup2.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 252 important colors, cbSize 3368, bits offset 1062)
        - usr/data/Data/title48/config1.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 254 important colors, cbSize 3376, bits offset 1070)
        - usr/data/Data/title48/config2.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 255 important colors, cbSize 3380, bits offset 1074)
        - usr/data/Data/title48/exit1.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 255 important colors, cbSize 3380, bits offset 1074)
        - usr/data/Data/title48/exit2.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 253 important colors, cbSize 3372, bits offset 1066)
        - usr/data/Data/title48/info1.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 255 important colors, cbSize 3380, bits offset 1074)
        - usr/data/Data/title48/info2.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 255 important colors, cbSize 3380, bits offset 1074)
        - usr/data/Data/title48/search1.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 246 important colors, cbSize 3344, bits offset 1038)
        - usr/data/Data/title48/search2.bmp (PC bitmap, Windows 3.x format, 48 x 48 x 8, image size 2306, resolution 2795 x 2795 px/m, 255 important colors, cbSize 3380, bits offset 1074)
      - **usr/data/Data/usbDetectPage/**
        - usr/data/Data/usbDetectPage/usb_disk.png (PNG image data, 57 x 72, 8-bit colormap, non-interlaced)
    - usr/data/config.lua (ISO-8859 text)
    - usr/data/hardware.lua (ASCII text)
    - **usr/data/player/**
    - usr/data/space (ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), statically linked, not stripped)
    - **usr/data/ssl/**
      - usr/data/ssl/ca.crt (PEM certificate)
      - usr/data/ssl/ca.key (ASCII text)
      - usr/data/ssl/cacert.pem (PEM certificate)
      - usr/data/ssl/privkey.pem (ASCII text)
      - usr/data/ssl/pubkey.pem (ASCII text)
  - **usr/etc/**
    - usr/etc/Global.lua (ISO-8859 text, with CRLF line terminators)
    - usr/etc/load_modules.sh (POSIX shell script, ASCII text executable)
    - usr/etc/telnet_cfg (ASCII text)
  - **usr/lib/**
    - usr/lib/lib.7z (7-zip archive data, version 0.4)
    - **usr/lib/lib.7z.extracted/**
      - **usr/lib/lib.7z.extracted/0/**
        - **usr/lib/lib.7z.extracted/0/lib/**
          - usr/lib/lib.7z.extracted/0/lib/8192cu.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=e470f396ec6553bc0a349f024ec34416da2f6ae7, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/8192eu.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=d178dc9e85c504c1b5e323f8c52ee4ba5b552ef9, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/avss.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=66c0cc7d117133d8d0289adc0373a7577f1777a9, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/crgctrl_hi3521a.sh (POSIX shell script, ISO-8859 text executable)
          - usr/lib/lib.7z.extracted/0/lib/driverbox.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=a63dfefe7b40aab2d303e8d0c8174abbbca7ab10, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_adec.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=49385cea1ba10e943a16a71ef82137b40ad90fb9, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_aenc.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=1ba65341fc9e8d0ae00524af7a8a9ea75f793d39, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_ai.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=5c3649c6950e2dcbeed6f70789d7877ce89056cd, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_aio.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=c8992201f6d45daab19cd4fb1ca1ce52f9994cfb, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_ao.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=718693fb1bd20299d3c3c00243a419e199da6b2b, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_base.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=9708d7a9046e1be11ba8e788948349f03c3e5590, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_chnl.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=92ea8b3844f44f01de9e84697408909ee48254a5, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_h264e.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=119810bdefa0a9eddb2e85a47bc735a2c5ac083f, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_hdmi.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=c9825c86610b80899fbf0739a02e49fe26087482, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_ive.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=adba2ed6e5beade94ae718d3bc563ab554203b24, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_jpegd.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=bf5a3352c00aef02989efddf282e4c2042c4aa05, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_jpege.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=bdd8db01c7d439bc93d632b6fcee069c9388ae5d, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_rc.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=ea5799b5116a4ded00424d0e8f9d6d202846418e, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_region.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=c6785d8e07665d9f18e2f058610602d540cbeaa7, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_sys.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=442493f4b48d313c5e4cf9e7a59e2e6d348f03fb, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_tde.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=a1bc3d305bfa5fd266c83c1d546049d39adf0030, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_vda.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=002109f04f118ee5aa9ee1c6d01e84e617752416, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_vdec.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=c1e878227cff1e53ece9d9b7a7888e17370bc4cb, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_venc.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=c36f594cc252cc31e79c9aed60ab160b21c0a835, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_vfmw.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=c97ff118e0b3c524eb1be5f5665ce55f8771d3e7, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_vgs.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=c06591cbb3065f64337bb304970d5620056fc1fe, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_viu.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=cac4bca19414177f0e6b0aa9b5192fdaf6cc9cb0, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_vou.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=ec2c661e05dd9c62eb777f1f1af35590217be9ec, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi3521a_vpss.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=ade4f73297fca2fd32f8a546e914833eb6d88fed, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi_i2c.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=48878dd1a00d2946294b3101178a5565cb6127cf, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi_media.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=3353e9c4286e3c1527755fc37f2621853f148576, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hi_rtc.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=4a4130285446e6e2f685add5079e1afdfdd317d4, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hifb.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=1658218783951d53351d5b147fbee58d08e2f419, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/hiuser.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=13a10a6247da5befe213fa742cfd73e8c2f0b79d, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/i2c_common.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=3ceb6ccc6558ff55e4526cd6b765859ebf3bc3ca, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/i2c_read (ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, with debug_info, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/i2c_write (ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, with debug_info, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/load_hisimod.sh (POSIX shell script, Unicode text, UTF-8 text executable)
          - usr/lib/lib.7z.extracted/0/lib/mmz.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=40dfecd01b26ffdd8b763b12f87b5a4073336286, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/option.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=972cb8b1d3c989938b7f6d67d91154b97ff4d3e8, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/osa.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=9909304c44bc8253865cd91ab0eace8f25b4dd53, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_i2s.sh (POSIX shell script, ISO-8859 text executable)
          - usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vga_hdmi_spi.sh (POSIX shell script, ASCII text executable)
          - usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vicap.sh (POSIX shell script, ISO-8859 text executable)
          - usr/lib/lib.7z.extracted/0/lib/sysctl_hi3521a_asic.sh (POSIX shell script, ISO-8859 text executable)
          - usr/lib/lib.7z.extracted/0/lib/usb_wwan.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=43c64de82f255b72a2b8ca779751c6d317c4fb9f, not stripped)
          - usr/lib/lib.7z.extracted/0/lib/usbserial.ko (ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=7ba74793ff53db5d66b44445040049870373a352, not stripped)
  - **usr/sbin/**
    - usr/sbin/.dec.sh (Bourne-Again shell script, ASCII text executable, with very long lines (674))
    - usr/sbin/3gconfig (ASCII text)
    - usr/sbin/3gpp (symbolic link to ../../sbin/3gpp)
    - usr/sbin/ii (POSIX shell script, ASCII text executable)
    - usr/sbin/nfs (POSIX shell script, ASCII text executable)
    - usr/sbin/usb_modeswitch (symbolic link to ../../bin/busybox)
- **var/**
  - var/Challenge (empty)
- **web/**
  - **web/Component/**
    - web/Component/chnlGroup.js (HTML document, ASCII text, with very long lines (4555), with no line terminators)
    - web/Component/level.js (ASCII text, with very long lines (918), with no line terminators)
    - web/Component/schedule.htm (Unicode text, UTF-8 text, with very long lines (7025), with no line terminators)
    - web/Component/schedule.js (ASCII text, with very long lines (13401), with no line terminators)
  - web/Data_Signature (data)
  - web/SigFileList (ASCII text)
  - web/cap.js (ASCII text, with no line terminators)
  - **web/config/**
    - web/config/index.htm (HTML document, Unicode text, UTF-8 text, with very long lines (1434), with CRLF line terminators)
  - **web/css/**
    - web/css/Intellent.css (Unicode text, UTF-8 text, with CRLF line terminators)
    - web/css/alarmindex.css (Unicode text, UTF-8 (with BOM) text, with CRLF line terminators)
    - web/css/custom.css (Unicode text, UTF-8 text, with CRLF line terminators)
    - web/css/faceplayback.css (ASCII text, with CRLF line terminators)
    - web/css/fn.css (Unicode text, UTF-8 text, with CRLF line terminators)
    - web/css/index.css (Unicode text, UTF-8 (with BOM) text, with CRLF line terminators)
    - web/css/infoindex.css (Unicode text, UTF-8 (with BOM) text, with CRLF line terminators)
    - web/css/oem.css (Unicode text, UTF-8 text, with CRLF line terminators)
    - web/css/playbackindex.css (Unicode text, UTF-8 (with BOM) text, with CRLF line terminators)
    - web/css/previewindex.css (Unicode text, UTF-8 text, with CRLF line terminators)
    - web/css/reset.css (Unicode text, UTF-8 text, with CRLF line terminators)
    - web/css/setindex.css (Unicode text, UTF-8 (with BOM) text, with CRLF line terminators)
    - web/css/skin.css (Unicode text, UTF-8 text, with CRLF line terminators)
    - web/css/ui.css (Unicode text, UTF-8 text, with CRLF line terminators)
  - web/favicon.ico (MS Windows icon resource - 1 icon, 16x16, 32 bits/pixel)
  - **web/html/**
    - web/html/3gnetcfg.htm (HTML document, Unicode text, UTF-8 text, with very long lines (9621), with CRLF line terminators)
    - web/html/ATMConfig.htm (HTML document, Unicode text, UTF-8 text, with very long lines (17978), with no line terminators)
    - web/html/IVSConfig.htm (HTML document, Unicode text, UTF-8 text, with very long lines (11588), with no line terminators)
    - web/html/adddevice.htm (HTML document, Unicode text, UTF-8 text, with very long lines (33354), with no line terminators)
    - web/html/alarmboxcfg.htm (HTML document, Unicode text, UTF-8 text, with very long lines (578), with no line terminators)
    - web/html/alarmcenter.htm (HTML document, Unicode text, UTF-8 text, with very long lines (2378), with no line terminators)
    - web/html/alarmindex.htm (HTML document, Unicode text, UTF-8 text, with very long lines (7920), with no line terminators)
    - web/html/alarmlink.htm (HTML document, Unicode text, UTF-8 text, with very long lines (15712), with no line terminators)
    - web/html/alarmout.htm (HTML document, Unicode text, UTF-8 text, with very long lines (3299), with no line terminators)
    - web/html/audiocfg.htm (HTML document, Unicode text, UTF-8 text, with very long lines (1639), with no line terminators)
    - web/html/audioset.htm (HTML document, Unicode text, UTF-8 text, with very long lines (11017), with no line terminators)
    - web/html/audiosetTemp.htm (HTML document, ASCII text, with no line terminators)
    - web/html/automaintain.htm (HTML document, Unicode text, UTF-8 text, with very long lines (3476), with CRLF line terminators)
    - web/html/autoregister.htm (HTML document, Unicode text, UTF-8 text, with very long lines (1615), with no line terminators)
    - web/html/blackwhite.htm (HTML document, Unicode text, UTF-8 text, with very long lines (5692), with no line terminators)
    - web/html/broadcast.htm (HTML document, Unicode text, UTF-8 text, with very long lines (1608), with no line terminators)
    - web/html/cfgmanage.htm (HTML document, Unicode text, UTF-8 text, with very long lines (2855), with no line terminators)
    - web/html/chanldiscgroup.htm (HTML document, Unicode text, UTF-8 text, with very long lines (8337), with CRLF line terminators)
    - web/html/chanlhddquota.htm (HTML document, Unicode text, UTF-8 text, with very long lines (2342), with CRLF line terminators)
    - web/html/chnlname.htm (HTML document, Unicode text, UTF-8 text, with very long lines (853), with no line terminators)
    - web/html/chnltype.htm (HTML document, ASCII text, with very long lines (979), with no line terminators)
    - web/html/connetcfg.htm (HTML document, Unicode text, UTF-8 text, with very long lines (5584), with no line terminators)
    - web/html/ddnsconfig.htm (HTML document, ASCII text, with very long lines (4931), with no line terminators)
    - web/html/defaultcfg.htm (HTML document, Unicode text, UTF-8 text, with very long lines (2730), with no line terminators)
    - web/html/diskerror.htm (HTML document, Unicode text, UTF-8 text, with very long lines (64490), with no line terminators)
    - web/html/diskinfo.htm (HTML document, Unicode text, UTF-8 text, with very long lines (5554), with no line terminators)
    - web/html/emailconfig.htm (HTML document, ASCII text, with very long lines (4587), with CRLF line terminators)
    - web/html/encodecfg.htm (HTML document, Unicode text, UTF-8 text, with very long lines (28274), with CRLF line terminators)
    - web/html/faceplayback.htm (HTML document, Unicode text, UTF-8 text, with very long lines (10609), with CRLF line terminators)
    - web/html/general.htm (Unicode text, UTF-8 text, with very long lines (2203), with no line terminators)
    - web/html/guiset.htm (HTML document, Unicode text, UTF-8 text, with very long lines (27420), with CRLF line terminators)
    - web/html/https.htm (HTML document, Unicode text, UTF-8 text, with very long lines (2517), with no line terminators)
    - web/html/imageprty.htm (HTML document, Unicode text, UTF-8 text, with very long lines (25115), with no line terminators)
    - web/html/infoindex.htm (HTML document, Unicode text, UTF-8 text, with very long lines (3640), with no line terminators)
    - web/html/ipAccess.htm (HTML document, Unicode text, UTF-8 text, with very long lines (5518), with no line terminators)
    - web/html/ipcFaceNewConfig.htm (HTML document, Unicode text, UTF-8 text, with very long lines (10792), with no line terminators)
    - web/html/iscsiconfig.htm (HTML document, Unicode text, UTF-8 text, with very long lines (5104), with no line terminators)
    - web/html/localconfig.htm (Unicode text, UTF-8 text, with very long lines (32592), with no line terminators)
    - web/html/localstorage.htm (HTML document, Unicode text, UTF-8 text, with very long lines (9257), with no line terminators)
    - web/html/logmanage.htm (HTML document, Unicode text, UTF-8 text, with very long lines (4201), with no line terminators)
    - web/html/onlineuser.htm (HTML document, Unicode text, UTF-8 text, with very long lines (936), with no line terminators)
    - web/html/p2pset.htm (HTML document, Unicode text, UTF-8 text, with very long lines (3652), with no line terminators)
    - web/html/playbackindex.htm (HTML document, Unicode text, UTF-8 text, with very long lines (55503), with no line terminators)
    - web/html/pppoe.htm (HTML document, Unicode text, UTF-8 text, with very long lines (2123), with no line terminators)
    - web/html/previewindex.htm (HTML document, Unicode text, UTF-8 (with BOM) text, with very long lines (398), with CRLF line terminators)
    - web/html/ptzconfig.htm (HTML document, ASCII text, with very long lines (3584), with no line terminators)
    - web/html/recordcontrol.htm (HTML document, ASCII text, with very long lines (2592), with CRLF line terminators)
    - web/html/recordplan.htm (Unicode text, UTF-8 text, with very long lines (26902), with no line terminators)
    - web/html/remotestorage.htm (HTML document, Unicode text, UTF-8 text, with very long lines (6611), with no line terminators)
    - web/html/serialconfig.htm (HTML document, Unicode text, UTF-8 text, with very long lines (2461), with no line terminators)
    - web/html/setindex.htm (HTML document, Unicode text, UTF-8 text, with very long lines (25530), with no line terminators)
    - web/html/snmpconfig.htm (HTML document, Unicode text, UTF-8 text, with very long lines (2382), with no line terminators)
    - web/html/tcpip_ipc.htm (Unicode text, UTF-8 text, with very long lines (10149), with no line terminators)
    - web/html/update.htm (Unicode text, UTF-8 text, with very long lines (6776), with no line terminators)
    - web/html/upnpconfig.htm (HTML document, Unicode text, UTF-8 text, with very long lines (4405), with no line terminators)
    - web/html/usermanage.htm (HTML document, Unicode text, UTF-8 text, with very long lines (23422), with no line terminators)
    - web/html/useronvif.htm (HTML document, Unicode text, UTF-8 text, with very long lines (5412), with no line terminators)
    - web/html/version.htm (ASCII text, with very long lines (2804), with no line terminators)
    - web/html/videodetect.htm (HTML document, Unicode text, UTF-8 text, with very long lines (34698), with no line terminators)
    - web/html/videomatrix.htm (HTML document, Unicode text, UTF-8 text, with very long lines (8945), with no line terminators)
    - web/html/wificfg.htm (HTML document, Unicode text, UTF-8 text, with very long lines (5459), with no line terminators)
  - **web/image/**
    - web/image/alert.gif (GIF image data, version 89a, 28 x 24)
    - web/image/allbg.png (PNG image data, 1 x 600, 8-bit colormap, non-interlaced)
    - web/image/bg.png (PNG image data, 1 x 170, 8-bit grayscale, non-interlaced)
    - web/image/bgl.png (PNG image data, 1 x 734, 8-bit colormap, non-interlaced)
    - web/image/boat.png (PNG image data, 104 x 699, 8-bit colormap, non-interlaced)
    - web/image/btnbar.png (PNG image data, 385 x 73, 8-bit colormap, non-interlaced)
    - web/image/connfail.gif (GIF image data, version 89a, 16 x 16)
    - web/image/connsucss.gif (GIF image data, version 89a, 16 x 16)
    - web/image/custom.png (PNG image data, 90 x 120, 8-bit colormap, non-interlaced)
    - web/image/horizonline.png (PNG image data, 320 x 5, 8-bit grayscale, non-interlaced)
    - web/image/icons.png (PNG image data, 570 x 720, 8-bit colormap, non-interlaced)
    - web/image/icons2.png (PNG image data, 300 x 300, 8-bit/color RGBA, non-interlaced)
    - web/image/lbt.png (PNG image data, 101 x 29, 8-bit colormap, non-interlaced)
    - web/image/lgbg.jpg (JPEG image data, Exif standard: [TIFF image data, little-endian, direntries=0], baseline, precision 8, 515x276, components 3)
    - web/image/lgbg.png (PNG image data, 483 x 317, 8-bit colormap, non-interlaced)
    - web/image/load.gif (GIF image data, version 89a, 16 x 16)
    - web/image/loginlogo.jpg (JPEG image data, Exif standard: [TIFF image data, little-endian, direntries=0], baseline, precision 8, 515x44, components 3)
    - web/image/logo.jpg (JPEG image data, Exif standard: [TIFF image data, little-endian, direntries=0], baseline, precision 8, 256x55, components 3)
    - web/image/pause.png (PNG image data, 33 x 67, 8-bit colormap, non-interlaced)
    - web/image/pic.png (PNG image data, 454 x 250, 8-bit/color RGBA, non-interlaced)
    - web/image/playback.png (PNG image data, 486 x 478, 8-bit colormap, non-interlaced)
    - web/image/playbackbg.png (PNG image data, 237 x 1, 8-bit grayscale, non-interlaced)
    - web/image/playbackline.png (PNG image data, 1 x 400, 8-bit colormap, non-interlaced)
    - web/image/playbacktimebg.png (PNG image data, 1 x 13, 1-bit colormap, non-interlaced)
    - web/image/pre.png (PNG image data, 368 x 17, 8-bit colormap, non-interlaced)
    - web/image/redTip.png (PNG image data, 5 x 5, 8-bit/color RGBA, non-interlaced)
    - web/image/redTipbg.png (PNG image data, 15 x 15, 8-bit/color RGBA, non-interlaced)
    - web/image/set.gif (GIF image data, version 89a, 16 x 16)
    - web/image/timep_boxbg.png (PNG image data, 11 x 80, 2-bit colormap, non-interlaced)
    - web/image/timep_boxbg2.png (PNG image data, 11 x 100, 2-bit colormap, non-interlaced)
    - web/image/timep_boxbg3.png (PNG image data, 11 x 80, 2-bit colormap, non-interlaced)
    - web/image/timep_hourbg.png (PNG image data, 44 x 5, 1-bit colormap, non-interlaced)
    - web/image/timep_weekbg.png (PNG image data, 5 x 40, 1-bit colormap, non-interlaced)
    - web/image/timep_weekbg2.png (PNG image data, 5 x 50, 1-bit colormap, non-interlaced)
    - web/image/updatebg.png (PNG image data, 17 x 56, 8-bit colormap, non-interlaced)
    - web/image/verticalline.png (PNG image data, 5 x 320, 8-bit grayscale, non-interlaced)
  - web/index.htm (HTML document, Unicode text, UTF-8 text, with very long lines (23411), with CRLF line terminators)
  - **web/js/**
    - web/js/3gnetcfg.js (ASCII text, with very long lines (22409), with no line terminators)
    - web/js/ATMConfig.js (HTML document, ASCII text, with very long lines (16724), with no line terminators)
    - web/js/Calendar.js (ASCII text, with very long lines (5306), with no line terminators)
    - web/js/FileList.js (ASCII text, with very long lines (3584), with no line terminators)
    - web/js/Grid.js (ASCII text, with very long lines (795), with no line terminators)
    - web/js/GroupControl.js (ASCII text, with very long lines (4457), with no line terminators)
    - web/js/IVSConfig.js (HTML document, ASCII text, with very long lines (25793), with no line terminators)
    - web/js/IVSFaceSearch.js (ASCII text, with very long lines (2692), with no line terminators)
    - web/js/PlayControl.js (ASCII text, with very long lines (836), with no line terminators)
    - web/js/WindowManager.js (ASCII text, with very long lines (1231), with no line terminators)
    - web/js/adddevice.js (ASCII text, with very long lines (32115))
    - web/js/alarmboxcfg.js (HTML document, ASCII text, with very long lines (1537), with no line terminators)
    - web/js/alarmcenter.js (ASCII text, with very long lines (4440), with no line terminators)
    - web/js/alarmindex.js (ASCII text, with very long lines (5113), with no line terminators)
    - web/js/alarmlink.js (ASCII text, with very long lines (32062))
    - web/js/alarmout.js (ASCII text, with very long lines (13449), with no line terminators)
    - web/js/appAbility.js (ASCII text, with very long lines (16256), with no line terminators)
    - web/js/audiocfg.js (ASCII text, with very long lines (2849), with no line terminators)
    - web/js/audioset.js (ASCII text, with very long lines (9448), with no line terminators)
    - web/js/automaintain.js (ASCII text, with very long lines (3911), with no line terminators)
    - web/js/autoregister.js (ASCII text, with very long lines (2544), with no line terminators)
    - web/js/blackwhite.js (ASCII text, with very long lines (12094), with no line terminators)
    - web/js/broadcast.js (ASCII text, with very long lines (2717), with no line terminators)
    - web/js/cfgmanage.js (ASCII text, with very long lines (3550), with no line terminators)
    - web/js/chanldiscgroup.js (ASCII text, with very long lines (22317), with no line terminators)
    - web/js/chanlhddquota.js (ASCII text, with very long lines (11291), with no line terminators)
    - web/js/chnlname.js (ASCII text, with very long lines (3130), with no line terminators)
    - web/js/chnltype.js (HTML document, ASCII text, with very long lines (20703), with no line terminators)
    - web/js/connetcfg.js (ASCII text, with very long lines (7963), with no line terminators)
    - web/js/ddnsconfig.js (ASCII text, with very long lines (20002), with no line terminators)
    - web/js/defaultcfg.js (ASCII text, with very long lines (2862), with no line terminators)
    - web/js/deviceInitial.js (ASCII text, with very long lines (5081), with no line terminators)
    - web/js/diskerror.js (ASCII text, with very long lines (19918), with no line terminators)
    - web/js/diskinfo.js (HTML document, ASCII text, with very long lines (10306), with no line terminators)
    - web/js/emailconfig.js (ASCII text, with very long lines (10687), with no line terminators)
    - web/js/encodecfg.js (ASCII text, with very long lines (32188))
    - web/js/eventScript.js (ASCII text, with very long lines (5905), with no line terminators)
    - web/js/faceplayback.js (ASCII text, with very long lines (16894), with no line terminators)
    - web/js/findPwd.js (ASCII text, with very long lines (9676), with no line terminators)
    - web/js/ft.js (ASCII text, with no line terminators)
    - web/js/general.js (ASCII text, with very long lines (2725), with no line terminators)
    - web/js/guiset.js (ASCII text, with very long lines (32321))
    - web/js/https.js (ASCII text, with very long lines (2776), with no line terminators)
    - web/js/imageprty.js (ASCII text, with very long lines (32358))
    - web/js/index.js (ASCII text, with very long lines (32046))
    - web/js/infoindex.js (ASCII text, with very long lines (4364), with no line terminators)
    - web/js/ipAccess.js (ASCII text, with very long lines (9757), with no line terminators)
    - web/js/ipcFaceNewConfig.js (ASCII text, with very long lines (24016), with no line terminators)
    - web/js/iscsiconfig.js (HTML document, ASCII text, with very long lines (10051), with no line terminators)
    - web/js/localconfig.js (ASCII text, with very long lines (32119))
    - web/js/localstorage.js (HTML document, ASCII text, with very long lines (19790), with no line terminators)
    - web/js/loginEx.js (ASCII text, with very long lines (5152), with no line terminators)
    - web/js/logmanage.js (ASCII text, with very long lines (12454), with no line terminators)
    - web/js/onlineuser.js (HTML document, ASCII text, with very long lines (1109), with no line terminators)
    - web/js/p2pset.js (ASCII text, with very long lines (5546), with no line terminators)
    - web/js/playbackindex.js (ASCII text, with very long lines (32085))
    - web/js/pppoe.js (ASCII text, with very long lines (2535), with no line terminators)
    - web/js/previewindex.js (HTML document, ASCII text, with very long lines (32094))
    - web/js/ptzCtrl.js (ASCII text, with very long lines (2587), with no line terminators)
    - web/js/ptzconfig.js (ASCII text, with very long lines (8397), with no line terminators)
    - web/js/publicFunc.js (Unicode text, UTF-8 text, with very long lines (32477))
    - web/js/qrcode.js (ASCII text, with very long lines (16824), with no line terminators)
    - web/js/recordcontrol.js (ASCII text, with very long lines (8119), with no line terminators)
    - web/js/recordplan.js (ASCII text, with very long lines (25017), with no line terminators)
    - web/js/remotestorage.js (ASCII text, with very long lines (9102), with no line terminators)
    - web/js/serialconfig.js (ASCII text, with very long lines (3486), with no line terminators)
    - web/js/setindex.js (ASCII text, with very long lines (25181), with no line terminators)
    - web/js/snmpconfig.js (ASCII text, with very long lines (3107), with no line terminators)
    - web/js/system.js (ASCII text, with very long lines (1484), with no line terminators)
    - web/js/tcpip_ipc.js (Unicode text, UTF-8 text, with very long lines (24720), with no line terminators)
    - web/js/update.js (Unicode text, UTF-8 text, with very long lines (11909), with no line terminators)
    - web/js/upnpconfig.js (HTML document, ASCII text, with very long lines (5569), with no line terminators)
    - web/js/usermanage.js (ASCII text, with very long lines (32343))
    - web/js/useronvif.js (HTML document, ASCII text, with very long lines (5859), with no line terminators)
    - web/js/version.js (Unicode text, UTF-8 text, with very long lines (4048), with no line terminators)
    - web/js/videodetect.js (ASCII text, with very long lines (32833))
    - web/js/videomatrix.js (ASCII text, with very long lines (32138))
    - web/js/wificfg.js (HTML document, Unicode text, UTF-8 text, with very long lines (9716), with no line terminators)
  - **web/jsBase/**
    - **web/jsBase/lib/**
      - web/jsBase/lib/base64.js (ASCII text, with very long lines (1466), with no line terminators)
      - web/jsBase/lib/m1.2.js (ASCII text, with very long lines (32155))
      - web/jsBase/lib/md5.js (ASCII text, with very long lines (4302), with no line terminators)
      - web/jsBase/lib/more.js (ASCII text, with very long lines (27050), with no line terminators)
      - web/jsBase/lib/qrcode.js (ASCII text, with very long lines (14489), with no line terminators)
  - **web/jsCore/**
    - web/jsCore/aes.js (ASCII text, with very long lines (13633), with no line terminators)
    - web/jsCore/common.js (ASCII text, with very long lines (10177), with no line terminators)
    - web/jsCore/rpcCore.js (ASCII text, with very long lines (32019))
    - web/jsCore/rsa.js (ASCII text, with very long lines (11802), with no line terminators)
  - web/local.png (ISO-8859 text)
  - web/olp.js (ASCII text, with very long lines (3125), with no line terminators)
  - **web/platformHtm/**
    - web/platformHtm/GAYS.htm (HTML document, Unicode text, UTF-8 (with BOM) text, with CRLF line terminators)
    - web/platformHtm/GAYS.js (Unicode text, UTF-8 text, with CRLF line terminators)
  - web/pluginVersion.js (ASCII text, with no line terminators)
  - web/webVersion.js (ASCII text, with no line terminators)
  - web/webplugin.exe (PE32 executable (GUI) Intel 80386, for MS Windows, Nullsoft Installer self-extracting archive)
```

# Firmware Details

- **File Size**: 22106176 bytes
- **MD5 Hash**: 487471520fbaace46b1677890f4ef4c6
- **File Format**: u-boot legacy uImage, hi3520Dromfs, Linux/ARM, OS Kernel Image (gzip), 13144064 bytes, Wed Nov 29 14:28:44 2017, Load Address: 0XA0060000, Entry Point: 0XA0DA0000, Header CRC: 0X71FF3C3D, Data CRC: 0X3F9F5075
- **Detected URLs**: ['http://192.168.1.108', 'http://203.0.113.25', 'http://amcrest.com', 'http://orange.instaon.com', 'http://www.apple.com', 'http://www.dahuaddns.com', 'http://www.freebsd.org', 'http://www.iana.org', 'http://www.keplerproject.org', 'http://www.quickddns.com', 'http://www.w3.org']
- **Detected IP Addresses**: ['0.0.0.0', '0.9.33.2', '1.0.0.1', '1.1.1.1', '10.6.3.213', '10.6.5.52', '110.119.0.1', '110.119.120.1', '127.0.0.1', '172.8.1.176', '192.168.0.0', '192.168.1.1', '192.168.1.108', '192.168.1.240', '192.168.25.22', '203.0.113.25', '224.0.0.0', '239.255.255.255', '255.255.255.0']
- **Entropy**: None
- **Entropy Analysis**: Error: '>' not supported between instances of 'str' and 'float'
## Metadata
- **Version**: hi3520Dromfs
- **Build_date**: 2017-11-29 14:28:44
- **Developer**: D@0.gN

- **UI Resources**: # UI Resources

## .css
- **web/css/**
  - Intellent.css
  - alarmindex.css
  - custom.css
  - faceplayback.css
  - fn.css
  - index.css
  - infoindex.css
  - oem.css
  - playbackindex.css
  - previewindex.css
  - reset.css
  - setindex.css
  - skin.css
  - ui.css

## .jpg
- **web/image/**
  - lgbg.jpg
  - loginlogo.jpg
  - logo.jpg

## .js
- **web/**
  - cap.js
  - olp.js
  - pluginVersion.js
  - webVersion.js
- **web/Component/**
  - chnlGroup.js
  - level.js
  - schedule.js
- **web/js/**
  - 3gnetcfg.js
  - ATMConfig.js
  - Calendar.js
  - FileList.js
  - Grid.js
  - GroupControl.js
  - IVSConfig.js
  - IVSFaceSearch.js
  - PlayControl.js
  - WindowManager.js
  - adddevice.js
  - alarmboxcfg.js
  - alarmcenter.js
  - alarmindex.js
  - alarmlink.js
  - alarmout.js
  - appAbility.js
  - audiocfg.js
  - audioset.js
  - automaintain.js
  - autoregister.js
  - blackwhite.js
  - broadcast.js
  - cfgmanage.js
  - chanldiscgroup.js
  - chanlhddquota.js
  - chnlname.js
  - chnltype.js
  - connetcfg.js
  - ddnsconfig.js
  - defaultcfg.js
  - deviceInitial.js
  - diskerror.js
  - diskinfo.js
  - emailconfig.js
  - encodecfg.js
  - eventScript.js
  - faceplayback.js
  - findPwd.js
  - ft.js
  - general.js
  - guiset.js
  - https.js
  - imageprty.js
  - index.js
  - infoindex.js
  - ipAccess.js
  - ipcFaceNewConfig.js
  - iscsiconfig.js
  - localconfig.js
  - localstorage.js
  - loginEx.js
  - logmanage.js
  - onlineuser.js
  - p2pset.js
  - playbackindex.js
  - pppoe.js
  - previewindex.js
  - ptzCtrl.js
  - ptzconfig.js
  - publicFunc.js
  - qrcode.js
  - recordcontrol.js
  - recordplan.js
  - remotestorage.js
  - serialconfig.js
  - setindex.js
  - snmpconfig.js
  - system.js
  - tcpip_ipc.js
  - update.js
  - upnpconfig.js
  - usermanage.js
  - useronvif.js
  - version.js
  - videodetect.js
  - videomatrix.js
  - wificfg.js
- **web/jsBase/lib/**
  - base64.js
  - m1.2.js
  - md5.js
  - more.js
  - qrcode.js
- **web/jsCore/**
  - aes.js
  - common.js
  - rpcCore.js
  - rsa.js
- **web/platformHtm/**
  - GAYS.js

## .png
- **usr/data/Data/DeviceSecurity/**
  - PatternNormal.png
  - PatternSelect.png
  - device_init_step1.png
  - device_init_step1_finish.png
  - device_init_step2.png
  - device_init_step2_finish.png
  - device_init_step3.png
  - device_init_step3_finish.png
  - headPic.png
  - progress0.png
  - progress1.png
  - progress2.png
  - progress3.png
  - progress4.png
  - progress5.png
  - progress6.png
  - progress7.png
  - progress8.png
  - progress9.png
- **usr/data/Data/Intell/**
  - CrossLineDetection.png
  - CrossRegionDetection.png
  - LeftDetection.png
  - TakenAwayDetection.png
  - bmp_intellback.png
  - checkbox_intelli_disable.png
  - checkbox_intelli_disableselect.png
  - checkbox_intelli_enable.png
  - checkbox_intelli_enableselect.png
- **usr/data/Data/NavigationBar/**
  - Separator.png
  - alert_normal.png
  - alert_select.png
  - channel_info_normal.png
  - channel_info_select.png
  - channel_tree_normal.png
  - channel_tree_select.png
  - collect_normal.png
  - collect_select.png
  - colorSet_normal.png
  - colorSet_select.png
  - disk_error.png
  - disk_error_select.png
  - disk_normal.png
  - disk_notexist.png
  - disk_notexist_select.png
  - disk_select.png
  - home_normal.png
  - home_select.png
  - left_normal.png
  - left_select.png
  - menu_exp.png
  - net_abort.png
  - net_abort_select.png
  - net_arp.png
  - net_arp_select.png
  - network_connected_normal.png
  - network_connected_select.png
  - next_screen_normal.png
  - next_screen_select.png
  - playback_normal.png
  - playback_select.png
  - prev_screen_normal.png
  - prev_screen_select.png
  - ptz_normal.png
  - ptz_select.png
  - remote_normal.png
  - remote_select.png
  - right_normal.png
  - right_select.png
  - tour_disable_normal.png
  - tour_disable_select.png
  - tour_enable_normal.png
  - tour_enable_select.png
  - usb_normal.png
  - usb_select.png
  - windows16_normal.png
  - windows16_select.png
  - windows1_normal.png
  - windows1_select.png
  - windows25_normal.png
  - windows25_select.png
  - windows32_normal.png
  - windows32_select.png
  - windows4_normal.png
  - windows4_select.png
  - windows6_normal.png
  - windows6_select.png
  - windows8_normal.png
  - windows8_select.png
  - windows9_normal.png
  - windows9_select.png
- **usr/data/Data/RealPlay/**
  - audio_close_normal.png
  - audio_close_selected.png
  - audio_disable.png
  - audio_open_normal.png
  - audio_open_selected.png
  - audiotalk_disable.png
  - audiotalk_normal.png
  - audiotalk_push.png
  - audiotalk_selected.png
  - block_disable.png
  - block_normal.png
  - block_selected.png
  - close_normal.png
  - close_selected.png
  - disable.png
  - hover.png
  - manual_snap_disable.png
  - manual_snap_normal.png
  - manual_snap_on_normal.png
  - manual_snap_on_select.png
  - manual_snap_selected.png
  - menuplay_backcolor.png
  - netcameraedit_disable.png
  - netcameraedit_normal.png
  - netcameraedit_selected.png
  - normal.png
  - pause_normal.png
  - pause_selected.png
  - play_normal.png
  - play_selected.png
  - play_slider_background.png
  - play_slider_elapsed.png
  - realbk_disable.png
  - realbk_normal.png
  - realbk_on_normal.png
  - realbk_on_selected.png
  - realbk_selected.png
  - realplay_normal.png
  - realplay_selected.png
  - zoomin_normal.png
  - zoomin_on_normal.png
  - zoomin_on_selected.png
  - zoomin_selected.png
- **usr/data/Data/afterSaleService/**
  - DahuaTechnology.png
  - after_sale_service.png
  - after_sale_service1.png
  - after_sale_service2.png
- **usr/data/Data/colorSettingPage/**
  - Brightness.png
  - Contrast.png
  - EqLevel.png
  - Gamma.png
  - Hue.png
  - Saturation.png
  - VideoPosition.png
  - colorSet_normal.png
  - plus0.png
  - plus1.png
  - plus2.png
  - plus3.png
  - reset0.png
  - reset1.png
  - reset2.png
  - reset3.png
  - subtractive0.png
  - subtractive1.png
  - subtractive2.png
  - subtractive3.png
  - unlock_disable.png
  - unlock_normal.png
  - unlock_select.png
- **usr/data/Data/exitPage/**
  - logout1.png
  - logout2.png
  - reboot1.png
  - reboot2.png
  - shutdown1.png
  - shutdown2.png
- **usr/data/Data/faceplayer/**
  - face_export_normal.png
  - face_export_select.png
  - face_search_disable.png
  - face_search_normal.png
  - face_search_select.png
  - play_back_disable.png
  - play_back_normal.png
  - play_back_push.png
  - play_back_select.png
  - play_fast_disable.png
  - play_fast_normal.png
  - play_fast_push.png
  - play_fast_select.png
  - play_nextframe_disable.png
  - play_nextframe_normal.png
  - play_nextframe_push.png
  - play_nextframe_select.png
  - play_preframe_disable.png
  - play_preframe_normal.png
  - play_preframe_push.png
  - play_preframe_select.png
  - play_slow_disable.png
  - play_slow_normal.png
  - play_slow_push.png
  - play_slow_select.png
  - play_start_disable.png
  - play_start_normal.png
  - play_start_push.png
  - play_start_select.png
  - play_stop_disable.png
  - play_stop_normal.png
  - play_stop_push.png
  - play_stop_select.png
  - play_volume_background.png
  - play_volume_elapsed.png
- **usr/data/Data/guiCtrls/**
  - disable_select.png
  - password_tip_disable.png
  - password_tip_normal.png
  - password_tip_select.png
  - retrieve_password_disable.png
  - retrieve_password_normal.png
  - retrieve_password_select.png
  - select_hover.png
  - select_hover_noamal.png
  - signal_select.png
  - smart_disable.png
  - smart_error.png
  - smart_ok.png
  - zhaohuimima_disable.png
  - zhaohuimima_normal.png
  - zhaohuimima_select.png
- **usr/data/Data/infoOnlineUserPage/**
  - shield_normal.png
  - shield_push.png
- **usr/data/Data/mainMenu/**
  - 16split_normal.png
  - 1split_normal.png
  - 3G.png
  - 4split_normal.png
  - 6split_normal.png
  - 8split_normal.png
  - 9split_normal.png
  - autoPtz_normal.png
  - cameraattribute_normal.png
  - colorSet_normal.png
  - config_guide_normal.png
  - customsplit_normal.png
  - face_search.png
  - main_normal.png
  - matrix_normal.png
  - netCamera_normal.png
  - next_screen_normal.png
  - outmode_normal.png
  - previous_screen_normal.png
  - ptz_normal.png
  - record_normal.png
  - search_normal.png
- **usr/data/Data/motionSetPage/**
  - blue_down.png
  - blue_normal.png
  - blue_select.png
  - green_down.png
  - green_normal.png
  - green_select.png
  - orange_down.png
  - orange_normal.png
  - orange_select.png
  - yellow_down.png
  - yellow_normal.png
  - yellow_select.png
- **usr/data/Data/netCameraPage/**
  - remotdev_editipc_disable.png
  - remotdev_editipc_normal.png
  - remotdev_editipc_selected.png
- **usr/data/Data/player/**
  - IVS_select.png
  - advanced_search_disable.png
  - advanced_search_normal.png
  - advanced_search_select.png
  - bmp_backup.png
  - bmp_card.png
  - bmp_channel.png
  - bmp_time.png
  - bmp_txn_error.png
  - bmp_txn_money.png
  - bmp_txn_type.png
  - camera_disable.png
  - camera_normal.png
  - camera_push.png
  - camera_select.png
  - clip_disable.png
  - clip_normal.png
  - clip_push.png
  - clip_save_disable.png
  - clip_save_normal.png
  - clip_save_push.png
  - clip_save_select.png
  - clip_select.png
  - close_filelist_disable.png
  - close_filelist_normal.png
  - close_filelist_push.png
  - close_filelist_select.png
  - file_list_disable.png
  - file_list_normal.png
  - file_list_push.png
  - file_list_select.png
  - grid_1hr_disable.png
  - grid_1hr_normal.png
  - grid_1hr_push.png
  - grid_1hr_select.png
  - grid_24hr_disable.png
  - grid_24hr_normal.png
  - grid_24hr_push.png
  - grid_24hr_select.png
  - grid_2hr_disable.png
  - grid_2hr_normal.png
  - grid_2hr_push.png
  - grid_2hr_select.png
  - grid_30min_disable.png
  - grid_30min_normal.png
  - grid_30min_push.png
  - grid_30min_select.png
  - ivs_config.png
  - ivs_disable.png
  - ivs_normal.png
  - ivs_push.png
  - lockRecSearch_disable.png
  - lockRecSearch_normal.png
  - lockRecSearch_push.png
  - lockRecSearch_selected.png
  - play_back_disable.png
  - play_back_normal.png
  - play_back_pause_disable.png
  - play_back_pause_normal.png
  - play_back_pause_push.png
  - play_back_pause_select.png
  - play_back_push.png
  - play_back_select.png
  - play_fast_disable.png
  - play_fast_normal.png
  - play_fast_push.png
  - play_fast_select.png
  - play_frame_bottom.png
  - play_frame_interval.png
  - play_frame_repeat.png
  - play_frame_top.png
  - play_nextday_disable.png
  - play_nextday_normal.png
  - play_nextday_push.png
  - play_nextday_select.png
  - play_nextframe_disable.png
  - play_nextframe_normal.png
  - play_nextframe_push.png
  - play_nextframe_select.png
  - play_pause_disable.png
  - play_pause_normal.png
  - play_pause_push.png
  - play_pause_select.png
  - play_preframe_disable.png
  - play_preframe_normal.png
  - play_preframe_push.png
  - play_preframe_select.png
  - play_prevday_disable.png
  - play_prevday_normal.png
  - play_prevday_push.png
  - play_prevday_select.png
  - play_slider_background.png
  - play_slider_elapsed.png
  - play_slow_disable.png
  - play_slow_normal.png
  - play_slow_push.png
  - play_slow_select.png
  - play_start_disable.png
  - play_start_normal.png
  - play_start_push.png
  - play_start_select.png
  - play_stop_disable.png
  - play_stop_normal.png
  - play_stop_push.png
  - play_stop_select.png
  - play_volume_background.png
  - play_volume_elapsed.png
  - reclock_disable.png
  - reclock_normal.png
  - reclock_push.png
  - reclock_selected.png
  - search_disable.png
  - search_normal.png
  - search_push.png
  - search_select.png
  - slicediv.png
  - sound_normal.png
  - sound_select.png
  - tab10_normal.png
  - tab10_select.png
  - tab11_normal.png
  - tab11_select.png
  - tab12_normal.png
  - tab12_select.png
  - tab13_normal.png
  - tab13_select.png
  - tab14_normal.png
  - tab14_select.png
  - tab15_normal.png
  - tab15_select.png
  - tab16_normal.png
  - tab16_select.png
  - tab1_normal.png
  - tab1_select.png
  - tab2_normal.png
  - tab2_select.png
  - tab3_normal.png
  - tab3_select.png
  - tab4_normal.png
  - tab4_select.png
  - tab5_normal.png
  - tab5_select.png
  - tab6_normal.png
  - tab6_select.png
  - tab7_normal.png
  - tab7_select.png
  - tab8_normal.png
  - tab8_select.png
  - tab9_normal.png
  - tab9_select.png
  - tab_normal.png
  - tab_select.png
  - tag_list_disable.png
  - tag_list_normal.png
  - tag_list_push.png
  - tag_list_select.png
  - tagadd_disable.png
  - tagadd_normal.png
  - tagadd_push.png
  - tagadd_select.png
  - tagmanage_disable.png
  - tagmanage_normal.png
  - tagmanage_push.png
  - tagmanage_select.png
  - window_16ch_disable.png
  - window_16ch_normal.png
  - window_16ch_push.png
  - window_16ch_select.png
  - window_1ch_disable.png
  - window_1ch_normal.png
  - window_1ch_push.png
  - window_1ch_select.png
  - window_4ch_disable.png
  - window_4ch_normal.png
  - window_4ch_push.png
  - window_4ch_select.png
  - window_9ch_disable.png
  - window_9ch_normal.png
  - window_9ch_push.png
  - window_9ch_select.png
  - window_fullscreen_disable.png
  - window_fullscreen_normal.png
  - window_fullscreen_push.png
  - window_fullscreen_select.png
  - window_selfdef_disable.png
  - window_selfdef_normal.png
  - window_selfdef_push.png
  - window_selfdef_select.png
- **usr/data/Data/player/calendar/**
  - buttom_left.png
  - buttom_right.png
  - button_left.png
  - button_right.png
- **usr/data/Data/ptz/**
  - down0.png
  - down1.png
  - down2.png
  - down3.png
  - left0.png
  - left1.png
  - left2.png
  - left3.png
  - leftdown0.png
  - leftdown1.png
  - leftdown2.png
  - leftdown3.png
  - leftup0.png
  - leftup1.png
  - leftup2.png
  - leftup3.png
  - plus0.png
  - plus1.png
  - plus2.png
  - plus3.png
  - position0.png
  - position1.png
  - position2.png
  - position3.png
  - right0.png
  - right1.png
  - right2.png
  - right3.png
  - rightdown0.png
  - rightdown1.png
  - rightdown2.png
  - rightdown3.png
  - rightup0.png
  - rightup1.png
  - rightup2.png
  - rightup3.png
  - subtractive0.png
  - subtractive1.png
  - subtractive2.png
  - subtractive3.png
  - up0.png
  - up1.png
  - up2.png
  - up3.png
- **usr/data/Data/ptzext/**
  - autopan_disable.png
  - autopan_normal.png
  - autopan_push.png
  - autopan_select.png
  - autoscan_disable.png
  - autoscan_normal.png
  - autoscan_push.png
  - autoscan_select.png
  - aux_disable.png
  - aux_normal.png
  - aux_push.png
  - aux_select.png
  - flip_disable.png
  - flip_normal.png
  - flip_push.png
  - flip_select.png
  - highspeed_disable.png
  - highspeed_normal.png
  - highspeed_push.png
  - highspeed_select.png
  - menu_disable.png
  - menu_normal.png
  - menu_push.png
  - menu_select.png
  - pattern_disable.png
  - pattern_normal.png
  - pattern_push.png
  - pattern_select.png
  - preset_disable.png
  - preset_normal.png
  - preset_push.png
  - preset_select.png
  - reset_disable.png
  - reset_normal.png
  - reset_push.png
  - reset_select.png
  - setting_disable.png
  - setting_normal.png
  - setting_push.png
  - setting_select.png
  - toleft_normal.png
  - toleft_select.png
  - toright_normal.png
  - toright_select.png
  - tour_disable.png
  - tour_normal.png
  - tour_push.png
  - tour_select.png
- **usr/data/Data/sharePicture/**
  - PcapInvalid.png
  - PcapStart_normal.png
  - PcapStart_select.png
  - PcapStop_normal.png
  - PcapStop_select.png
  - button_normal_ex.png
  - button_select_ex.png
  - checkbox_select_hover.png
  - checkbox_select_large_hover.png
  - checkbox_signal_large_select.png
  - checkbox_signal_select.png
  - detail_normal.png
  - detail_push.png
  - detail_select.png
  - dir.png
  - disable_large_normal.png
  - disable_normal.png
  - file.png
  - gridLock.png
  - gridLockSelected.png
  - gridUnLock.png
  - gridUnLockSelected.png
  - input_control.png
  - input_lowercase.png
  - input_mark.png
  - input_numeric.png
  - input_pinyin.png
  - input_uppercase.png
  - menu_normal.png
  - menu_tab_normal.png
  - menu_tab_select.png
  - play_search_disable.png
  - play_search_normal.png
  - play_search_push.png
  - play_search_select.png
  - radio_tab_normal.png
  - radio_tab_select.png
  - remotdev_del_disable.png
  - remotdev_del_normal.png
  - remotdev_del_selected.png
  - remotdev_edit_disable.png
  - remotdev_edit_normal.png
  - remotdev_edit_selected.png
  - remotdev_stat_disable.png
  - remotdev_stat_normal.png
  - reset0.png
  - reset1.png
  - reset2.png
  - reset3.png
  - signal_select_large_normal.png
  - signal_select_normal.png
  - sub_window_bottom.png
  - sub_window_top.png
  - view_disable.png
  - view_normal.png
  - view_select.png
  - window_bottom.png
  - window_bottom1.png
  - window_title.png
  - window_top.png
- **usr/data/Data/storagePage/**
  - ClearNormal.png
  - ClearSelected.png
  - SettingNormal.png
  - SettingSelected.png
  - checkAlarmDisable.png
  - checkAlarmDisableSelect.png
  - checkAlarmEnable.png
  - checkAlarmEnableSelect.png
  - checkMDAlarmDisable.png
  - checkMDAlarmDisableSelect.png
  - checkMDAlarmEnable.png
  - checkMDAlarmEnableSelect.png
  - checkMDDisable.png
  - checkMDDisableSelect.png
  - checkMDEnable.png
  - checkMDEnableSelect.png
  - checkRegularDisable.png
  - checkRegularDisableSelect.png
  - checkRegularEnable.png
  - checkRegularEnableSelect.png
- **usr/data/Data/usbDetectPage/**
  - usb_disk.png
- **web/**
  - local.png
- **web/image/**
  - allbg.png
  - bg.png
  - bgl.png
  - boat.png
  - btnbar.png
  - custom.png
  - horizonline.png
  - icons.png
  - icons2.png
  - lbt.png
  - lgbg.png
  - pause.png
  - pic.png
  - playback.png
  - playbackbg.png
  - playbackline.png
  - playbacktimebg.png
  - pre.png
  - redTip.png
  - redTipbg.png
  - timep_boxbg.png
  - timep_boxbg2.png
  - timep_boxbg3.png
  - timep_hourbg.png
  - timep_weekbg.png
  - timep_weekbg2.png
  - updatebg.png
  - verticalline.png

- **Packing**: Archive Detected
- **Architecture**: 0             0x0             uImage header, header size: 64 bytes, header CRC: 0x71FF3C3D, created: 2017-11-29 14:28:44, image size: 13144064 bytes, Data Address: 0xA0060000, Entry Point: 0xA0DA0000, data CRC: 0x3F9F5075, OS: Linux, CPU: ARM, image type: OS Kernel Image, compression type: gzip, image name: "hi3520Dromfs"
## Cryptographic Analysis


- Found Cryptographic Functions:
  * [1;33;40m%02d:%02d:%02d|SecurityUnit-454744|AES_set_encrypt_key,the ret %d|%s:%d|%s(), RAND_bytes(m_tgk_ptr, tgkLengthValue) != 0, RAND_bytes(m_rand_data, m_rand_length) != 0, [1;31;40m%02d:%02d:%02d|SecurityUnit-454744|AES_set_encrypt_key failed|%s:%d|%s(), RAND_bytes((unsigned char*)&csbId, sizeof(csbId)) != 0

- Weak Encryption Detected:
  * [%s:%d] this:%p tid:%d,  default setting add !DES !RC4 succeed!, PSK-3DES-EDE-CBC-SHA, EAP-MD5: Invalid challenge (challenge_len=%lu len=%lu), PBE-SHA1-RC4-40, DES-EDE3-CBC

- Found Hardcoded Base64 Keys:
  * 1L6aFb46JMYaDCzLyTC14/sZhQXRZDxGehazVeWG1T0lh3iO4QC7bzEcHU7vrCRX

- Potential RSA Private Keys Found:
  * Potential RSA Key in: boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin

## Potential Passwords Found
- **Password**: BXw6K8YB | **Found in**: usr/etc/telnet_cfg
- **Password**: admin | **Found in**: usr/data/config.lua
- **Password**: 888888 | **Found in**: usr/data/config.lua
- **Password**: 666666 | **Found in**: usr/data/config.lua
- **Password**: tluafed | **Found in**: usr/data/config.lua

# Security Details

## etc/shadow and etc/passwd files
- etc/passwd
- Content of etc/passwd:
root:$1$jSqQv.uP$jgz4lwEx2pnDh4QwXkh06/:0:0:root:/:/bin/sh

- etc/passwd-
- Content of etc/passwd-:
root:ab8nBoH3mb8.g:0:0::/root:/bin/sh


## etc/ssl directory files
- No files found in /etc/ssl directory

## SSL related files
- usr/bin/ssl/pwdreset.pem
- usr/bin/secboot/public.pem
- usr/data/ssl/privkey.pem
- usr/data/ssl/cacert.pem
- usr/data/ssl/pubkey.pem
- usr/data/ssl/ca.crt
- usr/data/ssl/ca.key

## Configuration files
- etc/resolv.conf
- etc/memstat.conf
- etc/udev/udev.conf

## Script files
- usr/sbin/.dec.sh
- usr/etc/load_modules.sh
- usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_i2s.sh
- usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vicap.sh
- usr/lib/lib.7z.extracted/0/lib/sysctl_hi3521a_asic.sh
- usr/lib/lib.7z.extracted/0/lib/crgctrl_hi3521a.sh
- usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vga_hdmi_spi.sh
- usr/lib/lib.7z.extracted/0/lib/load_hisimod.sh

## Other .bin files
- boot/uImage.extracted/0/Linux-3.10.0.bin
- boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin
- usr/data/Data/FontSmallEn.bin
- usr/data/Data/Font.bin

## Keywords found
- **password**: linuxrc, init, sbin/getty, sbin/lsusb, sbin/ifdown, sbin/makedevs, sbin/pppoe, sbin/ifconfig, sbin/chat, sbin/upnp_tv_ctrlpt, sbin/route, sbin/depmod, sbin/insmod, sbin/reboot, sbin/mdev, sbin/ifup, sbin/init, sbin/lsmod, sbin/hdparm, sbin/3gpp, sbin/net3g, sbin/netinit, sbin/halt, sbin/netinit6, sbin/dvrhelper, sbin/inetd, sbin/fdisk, sbin/modprobe, sbin/rmmod, sbin/pppd, sbin/upgraded, sbin/lspci, sbin/poweroff, bin/killall, bin/mknod, bin/cttyhack, bin/touch, bin/free, bin/mesg, bin/df, bin/killall5, bin/tar, bin/msh, bin/umount, bin/nice, bin/gzip, bin/passwd, bin/mv, bin/eject, bin/chat, bin/[, bin/echo, bin/vi, bin/sleep, bin/sync, bin/iproute, bin/mktemp, bin/top, bin/ping6, bin/dnsdomainname, bin/mkdir, bin/dd, bin/ping, bin/printenv, bin/iptunnel, bin/chmod, bin/bootenv, bin/busybox, bin/login, bin/ps, bin/ls, bin/ifenslave, bin/[[, bin/cat, bin/kill, bin/grep, bin/ip, bin/netstat, bin/mount, bin/wget, bin/pwd, bin/awk, bin/p7zip, bin/sh, bin/iprule, bin/iplink, bin/cp, bin/uname, bin/rm, bin/vlock, bin/ash, bin/devmem, bin/hostname, bin/du, bin/gunzip, bin/ipaddr, bin/hush, bin/less, lib/libc.so.0, lib/libuClibc-0.9.33.2.so, web/index.htm, web/olp.js, web/jsCore/rpcCore.js, web/config/index.htm, web/js/wificfg.js, web/js/ddnsconfig.js, web/js/index.js, web/js/connetcfg.js, web/js/findPwd.js, web/js/adddevice.js, web/js/usermanage.js, web/platformHtm/GAYS.htm, web/platformHtm/GAYS.js, web/html/3gnetcfg.htm, web/html/remotestorage.htm, web/html/usermanage.htm, web/html/useronvif.htm, web/html/pppoe.htm, web/html/emailconfig.htm, web/html/wificfg.htm, web/html/adddevice.htm, web/html/ddnsconfig.htm, web/html/iscsiconfig.htm, usr/sbin/usb_modeswitch, usr/sbin/3gpp, usr/bin/Challenge, usr/data/Data/StringAll.7z.extracted/0/StringAll
- **admin**: linuxrc, init, sbin/getty, sbin/lsusb, sbin/ifdown, sbin/makedevs, sbin/pppoe, sbin/ifconfig, sbin/chat, sbin/upnp_tv_ctrlpt, sbin/route, sbin/depmod, sbin/insmod, sbin/reboot, sbin/mdev, sbin/ifup, sbin/init, sbin/lsmod, sbin/hdparm, sbin/3gpp, sbin/net3g, sbin/netinit, sbin/halt, sbin/netinit6, sbin/dvrhelper, sbin/inetd, sbin/fdisk, sbin/modprobe, sbin/rmmod, sbin/pppd, sbin/upgraded, sbin/lspci, sbin/poweroff, bin/killall, bin/mknod, bin/cttyhack, bin/touch, bin/free, bin/mesg, bin/df, bin/killall5, bin/tar, bin/msh, bin/umount, bin/nice, bin/gzip, bin/passwd, bin/mv, bin/eject, bin/chat, bin/[, bin/echo, bin/vi, bin/sleep, bin/sync, bin/iproute, bin/mktemp, bin/top, bin/ping6, bin/dnsdomainname, bin/mkdir, bin/dd, bin/ping, bin/printenv, bin/iptunnel, bin/chmod, bin/bootenv, bin/busybox, bin/login, bin/ps, bin/ls, bin/ifenslave, bin/[[, bin/cat, bin/kill, bin/grep, bin/ip, bin/netstat, bin/mount, bin/wget, bin/pwd, bin/awk, bin/p7zip, bin/sh, bin/iprule, bin/iplink, bin/cp, bin/uname, bin/rm, bin/vlock, bin/ash, bin/devmem, bin/hostname, bin/du, bin/gunzip, bin/ipaddr, bin/hush, bin/less, web/index.htm, web/jsCore/rpcCore.js, web/config/index.htm, web/js/deviceInitial.js, web/js/loginEx.js, web/js/index.js, web/js/findPwd.js, web/js/adddevice.js, web/js/usermanage.js, web/html/usermanage.htm, web/html/useronvif.htm, web/html/adddevice.htm, usr/sbin/usb_modeswitch, usr/sbin/3gpp, usr/bin/Challenge, usr/data/config.lua, usr/data/Data/StringAll.7z.extracted/0/StringAll
- **root**: linuxrc, init, sbin/getty, sbin/lsusb, sbin/ifdown, sbin/makedevs, sbin/pppoe, sbin/ifconfig, sbin/chat, sbin/upnp_tv_ctrlpt, sbin/route, sbin/depmod, sbin/insmod, sbin/reboot, sbin/mdev, sbin/ifup, sbin/init, sbin/lsmod, sbin/hdparm, sbin/3gpp, sbin/net3g, sbin/netinit, sbin/halt, sbin/netinit6, sbin/dvrhelper, sbin/inetd, sbin/fdisk, sbin/modprobe, sbin/rmmod, sbin/pppd, sbin/upgraded, sbin/lspci, sbin/poweroff, etc/inittab, etc/passwd, etc/group, etc/passwd-, boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin, bin/killall, bin/mknod, bin/cttyhack, bin/touch, bin/free, bin/mesg, bin/df, bin/killall5, bin/tar, bin/msh, bin/umount, bin/nice, bin/gzip, bin/passwd, bin/mv, bin/eject, bin/chat, bin/[, bin/echo, bin/vi, bin/sleep, bin/sync, bin/iproute, bin/mktemp, bin/top, bin/ping6, bin/dnsdomainname, bin/mkdir, bin/dd, bin/ping, bin/printenv, bin/iptunnel, bin/chmod, bin/bootenv, bin/busybox, bin/login, bin/ps, bin/ls, bin/ifenslave, bin/[[, bin/cat, bin/kill, bin/grep, bin/ip, bin/netstat, bin/mount, bin/wget, bin/pwd, bin/awk, bin/p7zip, bin/sh, bin/iprule, bin/iplink, bin/cp, bin/uname, bin/rm, bin/vlock, bin/ash, bin/devmem, bin/hostname, bin/du, bin/gunzip, bin/ipaddr, bin/hush, bin/less, web/webplugin.exe, web/jsBase/lib/m1.2.js, usr/sbin/usb_modeswitch, usr/sbin/3gpp, usr/bin/Challenge
- **123456**: lib/libc.so.0, lib/libuClibc-0.9.33.2.so, usr/bin/Challenge, usr/lib/lib.7z.extracted/0/lib/8192eu.ko, usr/lib/lib.7z.extracted/0/lib/8192cu.ko

## Common web servers used on IoT devices
- usr/bin/Challenge
- web/js/faceplayback.js

## Common binaries
- etc/ppp/pppoesessionctx
- bin/sync
- bin/busybox
- bin/wget
- web/js/encodecfg.js
- web/js/publicFunc.js
- web/html/encodecfg.htm
- usr/etc/telnet_cfg
- usr/lib/lib.7z.extracted/0/lib/hi3521a_aenc.ko
- usr/lib/lib.7z.extracted/0/lib/hi3521a_venc.ko
- usr/data/Data/mainPage/advanced2.bmp
- usr/data/Data/mainPage/advanced1.bmp
- usr/data/Data/player/advanced_search_normal.png
- usr/data/Data/player/advanced_search_select.png
- usr/data/Data/player/advanced_search_disable.png
- usr/data/Data/title48/advanced2.bmp
- usr/data/Data/title48/advanced1.bmp

## URLs, email addresses, and IP addresses found
- **URLs**: http://192.168.1.108, http://203.0.113.25, http://amcrest.com, http://orange.instaon.com, http://www.apple.com, http://www.dahuaddns.com, http://www.freebsd.org, http://www.iana.org, http://www.keplerproject.org, http://www.quickddns.com, http://www.w3.org
- **Emails**: ajt@debian.org, andersen@codepoet.org, resetpwd@cpplusworld.com., support_rpwd@global.dahuatech.com., wang_hengwen@dahuatech.com, wanghw@dhmail.com
- **IP Addresses**: 0.0.0.0, 0.9.33.2, 1.0.0.1, 1.1.1.1, 10.6.3.213, 10.6.5.52, 110.119.0.1, 110.119.120.1, 127.0.0.1, 172.8.1.176, 192.168.0.0, 192.168.1.1, 192.168.1.108, 192.168.1.240, 192.168.25.22, 203.0.113.25, 224.0.0.0, 239.255.255.255, 255.255.255.0


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
- **Current Date**: `Friday, January 31, 2025, 5 PM `

---

### Startup Script: `/bin/busybox`

- **Directory Name**: `/bin`
- **File Name**: `busybox`
- **File Type**: `ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped`
- **MD5 Hash**: `a053573c0e452c7a96c3fc028d2b9e8e`
- **File Size**: `1337336 bytes`
- **Architecture**: `ARM`
- **Current Date**: `Friday, January 31, 2025, 5 PM `

---

# Detected Suspicious Strings

### File: `linuxrc`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `init`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/getty`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/lsusb`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/ifdown`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/makedevs`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/pppoe`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/ifconfig`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/chat`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/upnp_tv_ctrlpt`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/route`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/depmod`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/insmod`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/reboot`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/mdev`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/ifup`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/init`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/lsmod`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/hdparm`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/3gpp`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/net3g`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/netinit`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/halt`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/netinit6`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/dvrhelper`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/inetd`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/fdisk`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/modprobe`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/rmmod`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/pppd`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/pppoe-start`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `sbin/upgraded`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/lspci`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `sbin/poweroff`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `etc/inittab`

| Keyword        |
|----------------|
| `exec`     |
| `/bin/sh`     |

### File: `etc/passwd`

| Keyword        |
|----------------|
| `/bin/sh`     |

### File: `etc/services`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `http://`     |
| `exec`     |

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
| `wget`     |
| `http://`     |

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
| `admin`     |
| `chmod`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/killall`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/mknod`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/cttyhack`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/touch`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/free`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/mesg`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/df`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/killall5`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/tar`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/msh`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/umount`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/nice`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/gzip`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/passwd`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/mv`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/eject`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/chat`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/[`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/echo`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/vi`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/sleep`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/sync`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/iproute`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/mktemp`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/top`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/ping6`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/dnsdomainname`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/mkdir`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/dd`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/ping`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/printenv`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/iptunnel`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/chmod`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/bootenv`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/busybox`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/login`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/ps`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/ls`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/ifenslave`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/[[`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/cat`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/kill`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/grep`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/ip`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/netstat`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/mount`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/wget`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/pwd`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/awk`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/p7zip`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/sh`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/iprule`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/iplink`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/cp`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/uname`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/rm`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/vlock`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/ash`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/devmem`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/hostname`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/du`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/gunzip`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/ipaddr`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/hush`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `bin/less`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
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
| `exec`     |
| `/bin/sh`     |

### File: `lib/libc.so.0`

| Keyword        |
|----------------|
| `/bin/sh`     |
| `password`     |
| `exec`     |
| `chmod`     |

### File: `lib/libpthread.so.0`

| Keyword        |
|----------------|
| `exec`     |
| `/bin/sh`     |

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
| `/bin/sh`     |
| `password`     |
| `exec`     |
| `chmod`     |

### File: `web/webplugin.exe`

| Keyword        |
|----------------|
| `https://`     |
| `FindNextFileA`     |
| `http://`     |
| `CreateProcessA`     |
| `FindFirstFileA`     |
| `CopyFileA`     |

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
| `admin`     |
| `password`     |

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
| `admin`     |
| `password`     |

### File: `web/js/qrcode.js`

| Keyword        |
|----------------|
| `base64`     |

### File: `web/js/adddevice.js`

| Keyword        |
|----------------|
| `admin`     |
| `password`     |

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
| `admin`     |
| `password`     |

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
| `admin`     |
| `password`     |

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
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
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
| `admin`     |
| `password`     |
| `chmod`     |
| `bash`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `usr/etc/load_modules.sh`

| Keyword        |
|----------------|
| `chmod`     |
| `/bin/sh`     |

### File: `usr/bin/Challenge`

| Keyword        |
|----------------|
| `https://`     |
| `admin`     |
| `password`     |
| `wget`     |
| `chmod`     |
| `base64`     |
| `openssl`     |
| `http://`     |
| `/bin/sh`     |
| `exec`     |

### File: `usr/bin/DahuaExec`

| Keyword        |
|----------------|
| `exec`     |

### File: `usr/bin/lua/compat-5.1.lua`

| Keyword        |
|----------------|
| `wget`     |
| `http://`     |

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
| `exec`     |
| `http://`     |

### File: `usr/data/Data/sharePicture/reset3.png`

| Keyword        |
|----------------|
| `http://`     |

# Vulnerabilities in executable files

## File: web/js/recordplan.js
**Ports**: 1, 100, 150, 2, 20, 24, 3, 30, 4, 40, 43200, 5, 6, 60, 7, 70, 8, 80

## File: web/html/version.htm
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/bin/lua/utils.lua
**Ports**: 1, 12, 16, 1992, 20, 2005, 24, 24576, 3, 8, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vou.ko
**Ports**: 1, 10, 100, 1000, 101, 10141, 1080, 11, 112, 12, 1280, 13, 14, 15, 16, 18, 181, 19, 1920, 2, 20, 200, 2017, 21, 22, 222, 24, 25, 255, 28, 3, 30, 32, 33, 34, 39, 4, 40, 400, 4000, 408, 41, 42, 420, 422, 43, 44, 47, 48, 49, 5, 50, 54, 57, 576, 59, 6, 60, 64, 7, 70, 71, 720, 73, 75, 8, 80, 804, 808, 81, 82, 84, 85, 86, 867, 87, 88, 9, 90, 91, 95, 96
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: sbin/upnp_tv_ctrlpt
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: boot/uImage.extracted/0/Linux-3.10.0.bin.extracted/1F58/decompressed.bin
**Ports**: 1, 10, 100, 101, 1010, 10101, 10104, 10107, 102, 10245, 10286, 103, 1030, 10310, 10327, 104, 10430, 10700, 1071, 10711, 10712, 10715, 108, 11, 110, 111, 1142, 115, 11611, 11657, 11673, 11694, 117, 11731, 118, 1181, 119, 12, 120, 12084, 121, 12103, 12134, 1215, 12152, 1230, 1232, 12357, 12363, 124, 12611, 12781, 128, 12809, 12827, 12845, 12857, 12869, 12882, 12913, 12958, 12985, 12987, 13, 1300, 13020, 13029, 13033, 13045, 13051, 13057, 13064, 13091, 131, 13189, 13197, 132, 133, 13321, 13353, 13370, 134, 13464, 135, 13505, 13575, 13582, 136, 14, 140, 141, 142, 14622, 14680, 148, 14871, 14903, 14947, 15, 15007, 1505, 1509, 15101, 1515, 15335, 15402, 15550, 15691, 157, 15780, 158, 15941, 15966, 16, 16039, 16048, 16089, 16096, 16097, 16098, 16100, 16121, 16140, 16155, 16176, 16197, 16221, 16240, 16251, 16260, 16341, 164, 16410, 16416, 16531, 16537, 16551, 16553, 16723, 16740, 16757, 16761, 16772, 16779, 16800, 16820, 16823, 16845, 16863, 16896, 169, 16914, 16934, 16951, 16961, 16965, 17, 170, 17009, 17042, 17044, 17060, 17083, 17166, 17176, 17198, 17224, 17241, 17275, 17302, 17308, 17314, 17315, 17326, 17361, 17381, 17390, 17405, 17413, 17487, 17534, 17563, 17663, 17667, 17744, 17764, 17772, 17773, 17774, 17776, 17821, 17839, 17852, 17864, 17873, 17874, 17875, 17965, 17988, 17990, 18, 180, 18003, 18008, 1803, 18057, 18070, 18083, 181, 18148, 18183, 1820, 1824, 18240, 18315, 18316, 18317, 18344, 18595, 18645, 18650, 18699, 18709, 18805, 18854, 18878, 18879, 18880, 18881, 18882, 18954, 19, 19009, 19020, 19060, 19079, 19082, 19095, 19132, 19139, 19152, 19157, 19164, 19165, 19211, 19212, 19217, 19219, 19246, 19276, 193, 19364, 19388, 19414, 19422, 19433, 19453, 19459, 19461, 19470, 19482, 19496, 19514, 19556, 19569, 19588, 19595, 19617, 19628, 19630, 19656, 19692, 19752, 19809, 19810, 19811, 19816, 19838, 19892, 19897, 19938, 19942, 19952, 1996, 19964, 19969, 19982, 19990, 2, 20, 200, 2000, 2001, 2003, 2005, 2006, 2009, 2012, 2017, 202, 20202, 204, 2048, 205, 207, 21, 2100, 2104, 2105, 2111, 215, 2151, 22, 222, 2222, 22242, 23, 2300, 235, 23995, 24, 240, 242, 244, 248, 249, 25, 255, 256, 2560, 257, 258, 26, 2600, 2608, 266, 27, 270, 28, 280, 282, 28242, 288, 29, 3, 30, 300, 3000, 30016, 30021, 30034, 30035, 30036, 30040, 302, 30211, 30223, 30241, 30252, 30260, 303, 30300, 30327, 304, 30432, 30454, 30481, 305, 30565, 30595, 30607, 30629, 30640, 30642, 30643, 30648, 30651, 30675, 30738, 30739, 30775, 30805, 30806, 30817, 30840, 30851, 30940, 30942, 30969, 30980, 30981, 31, 31088, 3110, 31160, 31161, 31214, 31275, 31289, 313, 31315, 31322, 31323, 31413, 31618, 31681, 31825, 32, 3200, 32124, 32129, 32154, 32159, 32186, 32213, 3226, 32261, 323, 324, 32457, 32465, 3250, 32637, 32681, 32773, 3280, 32839, 32842, 32888, 33, 330, 33191, 332, 33222, 33223, 33239, 33249, 33254, 33273, 33282, 333, 33302, 33307, 33312, 33317, 3333, 33330, 33338, 33408, 33519, 33520, 33522, 33543, 33626, 33720, 33724, 33779, 3380, 33875, 3390, 34, 340, 3404, 34108, 34110, 343, 345, 34573, 34574, 34597, 35, 35028, 35029, 35067, 35078, 35082, 35207, 35224, 35225, 35226, 35245, 35265, 35292, 35365, 35396, 35420, 35450, 35516, 35547, 35594, 356, 35678, 357, 35750, 35856, 35860, 35869, 35888, 36, 360, 3600, 36026, 3605, 36112, 36145, 36264, 36301, 36304, 36351, 36465, 36609, 36669, 36670, 36671, 36672, 36813, 36814, 36911, 37, 37543, 37552, 37561, 37575, 37611, 37648, 37704, 37714, 37765, 37815, 37933, 38, 380, 38032, 38033, 38121, 38137, 38207, 38218, 38228, 38245, 383, 38382, 38425, 38426, 38427, 38436, 38464, 38469, 38474, 38479, 38519, 38529, 38544, 38568, 38581, 38582, 38682, 38701, 38708, 38818, 38851, 38864, 38894, 38994, 38995, 38996, 39, 39014, 39110, 39136, 39137, 39164, 3925, 3926, 39273, 39277, 39308, 39324, 39349, 39397, 39405, 3941, 39412, 39463, 39522, 39639, 39647, 39685, 39688, 39765, 39793, 39800, 39801, 39805, 39811, 39814, 39842, 39903, 39938, 39944, 4, 40, 400, 4000, 401, 40137, 40194, 4020, 40211, 4027, 403, 404, 4040, 40404, 40407, 40411, 40463, 40467, 40509, 40516, 40662, 40671, 40676, 40700, 40704, 40759, 408, 4080, 40808, 409, 4096, 40998, 41, 410, 4100, 411, 4110, 41102, 41103, 41175, 41184, 41191, 4120, 41236, 41317, 414, 4141, 41506, 41586, 418, 41866, 41883, 41897, 41961, 41988, 42, 420, 42025, 42075, 42086, 42094, 42260, 42261, 42265, 42266, 42368, 42375, 42456, 42472, 42561, 4269, 42825, 42978, 43, 43084, 43089, 43094, 431, 43327, 43338, 43349, 43383, 43392, 43416, 43459, 43500, 43502, 43503, 43542, 43576, 43594, 44, 440, 4404, 44044, 44176, 443, 444, 4444, 44844, 44863, 44904, 45, 451, 452, 456, 45670, 46, 461, 47, 477, 48, 480, 4814, 49, 4920, 5, 50, 500, 5000, 505, 51, 512, 52, 5200, 523, 53, 535, 54, 541, 54555, 55, 555, 5555, 55555, 5585, 56, 561, 5614, 5615, 5616, 5617, 5632, 5633, 5634, 5635, 5687, 5688, 569, 57, 5719, 5781, 58, 5892, 59, 5924, 596, 6, 60, 600, 6070, 61, 6119, 61200, 6131, 62, 6233, 6234, 6288, 63, 64, 640, 6404, 646, 65, 6538, 6586, 6588, 6594, 66, 6617, 666, 6666, 67, 6705, 68, 6840, 685, 6879, 6898, 69, 6926, 7, 70, 706, 708, 71, 7132, 7175, 72, 721, 7280, 7283, 73, 731, 7325, 737, 74, 7425, 7477, 75, 7523, 755, 76, 7624, 7642, 765, 77, 7704, 777, 7777, 78, 780, 781, 7851, 7868, 789, 79, 7951, 797, 8, 80, 800, 8000, 8001, 801, 8012, 8019, 802, 803, 8031, 8034, 804, 8040, 805, 808, 8080, 809, 81, 8100, 811, 814, 818, 82, 820, 8296, 83, 8305, 84, 840, 841, 847, 8475, 848, 85, 86, 8610, 866, 8696, 87, 870, 876, 88, 880, 8818, 884, 888, 8888, 89, 9, 90, 900, 901, 909, 91, 9120, 92, 921, 93, 930, 94, 940, 9462, 949, 95, 9546, 96, 960, 9660, 97, 9721, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: DES, RSA, SSL

## File: usr/bin/lua/com/ParseKLPOSStr.lua
**Ports**: 1, 10, 128, 16, 2, 2000, 3, 32, 7, 8

## File: sbin/depmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/imageprty.htm
**Ports**: 1, 100, 1000, 15, 2, 20, 3

## File: web/js/logmanage.js
**Ports**: 1, 10, 100, 12, 1900, 2, 20, 200, 23, 400

## File: web/js/general.js
**Ports**: 1, 1024, 255, 3

## File: web/js/WindowManager.js
**Ports**: 1, 2, 3, 4

## File: usr/bin/lua/ptz/PHILIPS.lua
**Ports**: 1, 16384, 2, 200, 3, 4, 5, 6, 7, 8

## File: web/js/ATMConfig.js
**Ports**: 1, 1200, 1440, 15, 150, 19200, 2, 20, 2400, 3, 38400, 4, 4800, 5, 57600, 6, 65535, 70, 8, 9600

## File: web/jsCore/aes.js
**Ports**: 1, 10, 11, 12, 128, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 255, 256, 257, 26, 27, 28, 283, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65535, 7, 75, 8, 9, 99
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, Hex, SSL

## File: lib/libstdc++.so.6
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 2013, 25, 3, 30, 31, 36, 37, 38, 4, 40, 403, 404, 405, 4080, 41, 410, 43, 440, 47, 48, 489, 49, 5, 500, 54, 540, 56, 6, 60, 67, 68, 69, 7, 8, 80, 803, 804, 808, 81, 83, 84, 85, 88, 89, 9, 90, 904, 91, 96
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: TLS

## File: web/html/audiocfg.htm
**Ports**: 1999

## File: web/html/ATMConfig.htm
**Ports**: 1, 10, 11, 12, 1200, 13, 14, 15, 16, 19200, 2, 20, 2400, 25, 3, 38400, 4, 4800, 5, 57600, 6, 600, 7, 8, 9, 9600

## File: usr/bin/lua/ptz/PANASONIC.lua
**Ports**: 1, 10, 100, 16, 1610, 18, 2, 200, 23, 24, 3, 4, 6, 7, 8, 9, 96, 99

## File: web/js/update.js
**Ports**: 1, 10, 100, 16, 2, 20, 200, 251, 3, 30, 300, 4, 5, 500, 6, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Base64

## File: usr/bin/lua/ptz/PelcoP1-A.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: usr/data/CustomConfig
**Ports**: 3322, 5, 80

## File: usr/bin/lua/ptz/Pe5051k.lua
**Ports**: 1, 10, 100, 11, 12, 123, 124, 13, 131, 14, 15, 16, 1610, 2, 200, 3, 4, 5, 6, 7, 8, 9, 999

## File: usr/lib/lib.7z.extracted/0/lib/8192cu.ko
**Ports**: 1, 10, 1000, 1010, 109, 11, 1222, 13, 14, 141, 147, 15, 16, 160, 17, 19, 192, 2, 20, 200, 2002, 2016, 202, 203, 21, 210, 222, 23, 230, 23995, 24, 242, 243, 2468, 283, 29, 3, 30, 303, 31, 32, 32002, 33, 34, 350, 36, 4, 40, 400, 4000, 404, 4050, 4080, 41, 42, 43, 44, 440, 444, 45, 46, 47, 48, 4800, 49, 5, 50, 506, 51, 54, 54050, 55, 56, 57, 590, 6, 60, 62, 65, 66, 666, 6666, 667, 7, 70, 700, 7040, 71, 717, 730, 76, 7666, 8, 80, 800, 8001, 8012, 802, 8040, 8051, 8090, 81, 82, 83, 84, 85, 86, 87, 88, 89, 9, 90, 900, 9044, 91, 92
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/html/ipAccess.htm
**Ports**: 1, 64

## File: usr/data/ssl/ca.key
**Ports**: 8

## File: lib/libuClibc-0.9.33.2.so
**Ports**: 1, 10, 100, 1020, 105, 109, 11, 110, 111, 1111, 11111, 1121, 12, 1234, 124, 13, 133, 14, 141, 145, 15, 1535, 16, 17, 17641, 18, 186, 1872, 1873, 19, 1912, 1913, 1926, 1927, 1989, 1990, 2, 20, 202, 20212, 2033, 2078, 208, 21, 2133, 22, 222, 2222, 22222, 22223, 22224, 228, 23, 234, 2345, 24, 245, 246, 25, 256, 26, 263, 27, 27751, 28, 288, 29, 3, 30, 300, 303, 306, 31, 32, 320, 321, 33, 333, 3345, 33744, 34, 342, 344, 35, 36, 37, 376, 38, 39, 4, 40, 401, 4050, 408, 4080, 41, 4151, 42, 4289, 43, 432, 4353, 44, 44355, 444, 4467, 45, 46, 47, 48, 49, 498, 5, 50, 51, 51305, 52, 5289, 53, 54, 543, 55, 551, 56, 5666, 5678, 56789, 57, 571, 572, 58, 588, 59, 5945, 6, 60, 600, 61, 613, 62, 620, 6272, 63, 64, 65, 66, 666, 67, 68, 682, 683, 69, 699, 7, 70, 701, 703, 71, 72, 73, 7383, 74, 7407, 75, 757, 76, 769, 77, 777, 78, 785, 789, 79, 793, 794, 8, 80, 800, 807, 808, 8080, 81, 813, 815, 818, 82, 83, 831, 84, 848, 85, 86, 87, 88, 8859, 89, 899, 9, 90, 900, 91, 92, 93, 94, 95, 96, 964, 97, 98, 99, 999, 9999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vga_hdmi_spi.sh
**Ports**: 1, 10, 32

## File: bin/p7zip
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/alarmlink.htm
**Ports**: 1, 10, 2, 3, 300, 4, 5, 6, 60, 600, 65535, 7, 8, 9

## File: web/html/cfgmanage.htm
**Ports**: 1, 1000

## File: web/js/pppoe.js
**Ports**: 1, 16, 2, 3, 31

## File: bin/gunzip
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/chanldiscgroup.htm
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/css/skin.css
**Ports**: 100, 111, 2, 2013, 210, 333, 5, 7, 777, 8, 888, 999

## File: bin/mesg
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/css/faceplayback.css
**Ports**: 100, 33, 555, 67

## File: usr/bin/lua/ptz/DH-SD2.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 32, 4, 5, 6, 64, 7, 8, 8192

## File: usr/bin/lua/ptz/PELCOD-MING.lua
**Ports**: 14, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: web/index.htm
**Ports**: 1, 100, 11, 110, 13, 2, 200, 2017, 3, 32, 4, 6, 63, 7, 8, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: bin/less
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/udev/rules.d/60-pcmcia.rules
**Ports**: 1, 16

## File: etc/udev/udev.conf
**Ports**: 3

## File: etc/profile
**Ports**: 1, 22
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: lib/libutil.so.0
**Ports**: 1, 10, 2, 4, 5, 7, 8
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: web/html/adddevice.htm
**Ports**: 1, 10, 11, 120, 2, 200, 2000, 32, 480, 63, 65535
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/css/custom.css
**Ports**: 10, 2, 2013, 210, 5, 8, 888, 9

## File: usr/Data_Signature
**Ports**: 7, 8

## File: usr/sbin/nfs
**Ports**: 1, 10, 2, 213, 3, 6

## File: bin/killall5
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/cp
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/init
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/kill
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/mdev
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/cfgmanage.js
**Ports**: 1, 2, 20, 300, 500, 60

## File: web/js/IVSConfig.js
**Ports**: 1, 10, 15, 150, 2, 25, 255, 3, 30, 300, 4, 5, 550, 6, 600, 8191

## File: usr/data/space
**Ports**: 4, 5

## File: web/html/audioset.htm
**Ports**: 1, 2, 24, 3, 600

## File: sbin/netinit6
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/hostname
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/grep
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/ddnsconfig.htm
**Ports**: 1, 1092, 5, 60, 65535

## File: web/Component/level.js
**Ports**: 1, 3

## File: web/js/chanldiscgroup.js
**Ports**: 1, 100, 1500, 2, 250, 4, 400, 50, 55, 8
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/html/guiset.htm
**Ports**: 1, 10, 100, 1024, 11, 12, 120, 1280, 13, 14, 15, 16, 2, 20, 200, 3, 4, 5, 6, 7, 720, 768, 8, 9

## File: usr/data/Data/cursors/size1.cur
**Ports**: 8

## File: sbin/poweroff
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/snmpconfig.htm
**Ports**: 1, 65535

## File: usr/bin/lua/ptz/PelcoP5.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 4, 5, 6, 7, 8

## File: web/js/diskinfo.js
**Ports**: 1, 10, 100, 1024, 2, 2000, 3, 5

## File: web/Data_Signature
**Ports**: 3, 4, 5

## File: web/js/upnpconfig.js
**Ports**: 1, 2, 30, 4, 5, 65535

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_ive.ko
**Ports**: 1, 10, 11, 11111, 118, 13, 15, 16, 18, 19, 191, 2, 2017, 27, 3, 30, 33, 37, 38, 4, 40, 41, 43, 45, 46, 48, 49, 4900, 5, 59, 6, 60, 67, 68, 7, 8, 80, 800, 81, 810, 83, 84, 85, 89, 9, 90, 900
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_rc.ko
**Ports**: 1, 10, 100, 12, 13, 18, 180, 19, 2, 2017, 255, 3, 30, 38, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 54, 6, 7, 70, 8, 80, 81, 82, 83, 84, 85, 86, 868, 87, 9

## File: usr/bin/lua/ptz/LiLin.lua
**Ports**: 1, 128, 16, 1610, 2, 200, 3, 8

## File: web/js/PlayControl.js
**Ports**: 1, 4

## File: web/js/diskerror.js
**Ports**: 1, 10, 100, 12, 13, 14, 15, 16, 17, 18, 2, 255, 3, 30, 300, 32, 350, 6, 60, 600, 7, 9, 99

## File: bin/ps
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/Pelco-9750.lua
**Ports**: 11, 16, 1610, 2, 250, 256, 3, 4, 5, 6, 7, 8, 9, 9750

## File: usr/lib/lib.7z.extracted/0/lib/usbserial.ko
**Ports**: 1, 10, 2, 3, 4, 40, 41, 48, 5, 6, 7, 8, 80, 88, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/platformHtm/GAYS.js
**Ports**: 1, 10, 128, 200, 24, 3000, 3600, 65535

## File: lib/libcrypt.so.0
**Ports**: 1, 2, 3, 4, 44, 5, 6, 7, 8, 80, 9, 91
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: web/jsBase/lib/md5.js
**Ports**: 1, 10, 11, 12, 127, 128, 14, 15, 16, 17, 2, 20, 21, 22, 23, 24, 255, 28, 3, 32, 36, 4, 40, 44, 48, 5, 52, 56, 6, 60, 64, 7, 8, 9

## File: web/js/appAbility.js
**Ports**: 1, 10, 1024, 1080, 11, 1920, 2, 3, 300, 4, 480, 5, 576, 6, 60, 7, 8, 8192, 9, 960

## File: usr/lib/lib.7z.extracted/0/lib/i2c_read
**Ports**: 1, 2, 3, 4, 5, 6, 7, 8, 80, 8808, 8813, 9

## File: lib/libthread_db.so.1
**Ports**: 1, 10, 11, 2, 3, 33, 4, 40, 41, 411, 5, 6, 7, 8, 80, 9

## File: web/js/playbackindex.js
**Ports**: 1, 10, 100, 1024, 11, 12, 128, 13, 1394, 14, 144, 1440, 15, 150, 16, 16384, 17, 192, 2, 200, 2012, 2048, 23, 24, 243, 25, 28, 29, 3, 30, 31, 32, 35, 350, 3600, 384, 4, 400, 4096, 42, 48, 5, 50, 576, 59, 6, 60, 655, 7, 8, 9

## File: usr/SigFileList
**Ports**: 1, 5, 717, 9750

## File: bin/bootenv
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/librt.so.0
**Ports**: 1, 2, 4, 40, 5, 6, 7, 8, 80, 9

## File: usr/bin/ssl/pwdreset.pem
### Encryption/Encoding: RSA

## File: usr/bin/lua/ptz/SANLI.lua
**Ports**: 1, 128, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 64, 7, 8, 80

## File: web/html/tcpip_ipc.htm
**Ports**: 4, 64

## File: sbin/insmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/driverbox.ko
**Ports**: 1, 10, 11, 15, 17, 180, 2, 20, 2017, 203, 21, 210, 22, 23, 24, 3, 30, 300, 31, 32, 38, 4, 40, 401, 404, 41, 42, 43, 44, 4438, 45, 46, 47, 48, 482, 49, 5, 50, 51, 58, 59, 6, 60, 61, 62, 64, 65, 66, 68, 7, 7311, 768, 8, 80, 800, 803, 808, 8090, 81, 82, 83, 84, 841, 85, 86, 87, 88, 89, 890, 9, 90, 900, 908, 92, 93, 95, 97, 99
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: Hex

## File: web/js/iscsiconfig.js
**Ports**: 1, 12, 2, 31, 3260, 3650, 50, 65535, 8
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: bin/mktemp
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/connetcfg.js
**Ports**: 1, 1025, 123, 127, 128, 1900, 2, 20, 200, 3, 37777, 37778, 37810, 3800, 39999, 4, 443, 5050, 554, 63, 65535, 80, 800, 9999

## File: web/js/Calendar.js
**Ports**: 1, 100, 11, 12, 15, 2, 2037, 28, 29, 3, 30, 31, 32, 4, 400, 42, 6, 9

## File: web/html/localstorage.htm
**Ports**: 1000, 10000

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vda.ko
**Ports**: 1, 10, 100, 11, 12, 128, 13, 16, 18, 19, 2, 2017, 205, 255, 256, 3, 32, 33, 4, 40, 4080, 40840, 41, 43, 45, 46, 48, 49, 5, 6, 69, 7, 8, 80, 83, 86, 87, 9, 92, 99

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_base.ko
**Ports**: 1, 10, 11, 128, 13, 1554, 1608, 18, 19, 2, 2017, 3, 31, 326, 33, 4, 40, 400, 41, 44, 45, 495, 5, 57, 6, 7, 72, 8, 80, 82, 9, 95

## File: web/js/autoregister.js
**Ports**: 1, 16, 2, 31, 5, 63, 65535

## File: etc/passwd
**Ports**: 1

## File: web/config/index.htm
**Ports**: 1, 10, 100, 1000, 10000, 172, 176, 1999, 2, 200, 210, 3, 30, 4, 400, 42, 5, 500, 6, 60, 7, 8, 9, 9999
### Encryption/Encoding: Base64

## File: web/js/p2pset.js
**Ports**: 1, 2, 3, 4

## File: bin/ping
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_adec.ko
**Ports**: 1, 10, 13, 18, 19, 2, 2017, 3, 4, 42, 46, 5, 6, 7, 8, 84, 9

## File: web/html/recordplan.htm
**Ports**: 1, 10, 100, 12, 14, 16, 18, 2, 20, 22, 24, 3, 30, 4, 5, 6, 8

## File: sbin/ifup
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/protocols
**Ports**: 1, 103, 108, 112, 115, 12, 124, 132, 133, 17, 2, 20, 22, 25, 27, 29, 3, 36, 37, 38, 4, 41, 43, 44, 45, 46, 47, 5, 50, 51, 57, 58, 59, 6, 60, 73, 8, 81, 88, 89, 9, 93, 94, 97, 98, 99

## File: sbin/Data_Signature
**Ports**: 4, 6, 9

## File: usr/lib/lib.7z.extracted/0/lib/hiuser.ko
**Ports**: 10, 3, 4, 6, 7, 8

## File: sbin/reboot
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/halt
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/webVersion.js
**Ports**: 2, 3, 7

## File: etc/services
**Ports**: 1, 1000, 1001, 10080, 10081, 10082, 10083, 101, 102, 104, 105, 106, 107, 1080, 109, 1099, 11, 110, 1109, 111, 11201, 1127, 113, 115, 116, 117, 1178, 119, 1210, 1214, 123, 1236, 1241, 129, 13, 1300, 1313, 1314, 135, 1352, 137, 138, 139, 143, 1433, 1434, 15, 1524, 1525, 1529, 15345, 161, 162, 163, 164, 1645, 1646, 1649, 17, 17001, 17002, 17003, 17004, 174, 177, 178, 179, 18, 1812, 1813, 19, 191, 194, 1957, 1958, 1959, 199, 2, 20, 2000, 20011, 20012, 2003, 201, 2010, 202, 204, 2053, 206, 209, 21, 210, 2101, 2102, 2103, 2104, 2105, 2111, 2121, 213, 2150, 22, 220, 22273, 23, 2401, 2430, 2431, 2432, 2433, 24554, 25, 2583, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2628, 27374, 29, 2988, 2989, 3, 3050, 3130, 3306, 345, 346, 347, 3493, 3632, 369, 3690, 37, 370, 371, 372, 389, 39, 4, 406, 42, 4224, 43, 443, 444, 445, 45, 4557, 4559, 4600, 465, 487, 4899, 49, 4949, 5, 50, 500, 5002, 512, 513, 514, 515, 5151, 517, 518, 520, 5222, 525, 526, 5269, 53, 530, 5308, 531, 532, 533, 5354, 5355, 538, 540, 543, 5432, 544, 548, 5555, 5556, 556, 563, 5674, 5675, 5680, 57, 57000, 587, 6, 6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 60177, 60179, 607, 610, 611, 612, 631, 6346, 6347, 636, 65, 655, 6566, 6667, 67, 68, 69, 7, 70, 7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 7009, 706, 7100, 749, 750, 751, 752, 754, 760, 761, 765, 77, 775, 777, 779, 783, 79, 80, 8021, 808, 8080, 8081, 8088, 87, 871, 873, 88, 9, 901, 9101, 9102, 9103, 9359, 95, 9673, 98, 989, 99, 990, 992, 993, 994, 995
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: SSL, TLS

## File: usr/data/ssl/privkey.pem
**Ports**: 5

## File: web/html/general.htm
**Ports**: 1

## File: web/olp.js
**Ports**: 1, 10, 100, 2

## File: web/js/encodecfg.js
**Ports**: 1, 10, 100, 1024, 10240, 1080, 12, 12288, 125, 128, 1280, 1429, 14336, 15, 1536, 16, 160, 16384, 1667, 1792, 18432, 192, 1920, 2, 20, 200, 2048, 20480, 224, 22528, 230, 24, 240, 24576, 25, 255, 256, 2560, 264, 288, 3, 30, 3072, 32, 320, 33, 3333, 352, 3600, 374, 375, 384, 4, 4096, 448, 45, 450, 48, 5, 50, 500, 512, 5279, 6, 6144, 625, 63, 6370, 6371, 6372, 64, 640, 7, 720, 768, 8, 80, 8165, 8170, 8192, 896, 96, 960

## File: usr/bin/lua/ptz/HY.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 5, 6, 8, 9

## File: web/js/FileList.js
**Ports**: 1, 10, 14, 2, 22, 24, 28, 3, 4, 5, 6, 8

## File: web/html/automaintain.htm
**Ports**: 1000

## File: bin/iptunnel
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/DH-SD1.lua
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: web/jsCore/rpcCore.js
**Ports**: 1, 10, 128, 16, 2, 23, 264, 3, 300, 35, 48, 5005, 55, 59, 61, 62, 7, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, RSA

## File: usr/bin/lua/ptz/WV-CS950.lua
**Ports**: 1, 10, 100, 13, 14, 15, 16, 1610, 17, 2, 2007, 23, 3, 350, 4, 5, 6, 64, 7, 8, 9, 96, 99

## File: usr/bin/lua/ptz/PelcoD.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vdec.ko
**Ports**: 1, 10, 102, 1030, 1038, 1049, 1086, 1096, 118, 1201, 1209, 124, 1269, 1296, 13, 132, 1322, 1342, 1356, 138, 14, 1441, 1491, 150, 1501, 1512, 1526, 1539, 1548, 156, 1581, 16, 164, 1642, 1655, 1664, 1720, 1726, 1761, 18, 180, 1817, 1833, 1876, 1883, 19, 1903, 1908, 191, 1920, 1925, 1928, 1933, 1940, 1948, 1953, 1956, 1962, 197, 1971, 1983, 1992, 2, 200, 2001, 2010, 2017, 2019, 202, 2027, 203, 2060, 2065, 2076, 2134, 2137, 2146, 219, 2212, 2218, 2248, 225, 2261, 2270, 2285, 2295, 232, 2326, 2342, 2348, 2355, 2374, 238, 24, 2421, 2623, 270, 2702, 2719, 2734, 2759, 2775, 2790, 2803, 2880, 2891, 2904, 292, 2922, 2937, 294, 2952, 297, 2986, 2996, 3, 300, 3011, 302, 3034, 3086, 3171, 318, 32, 3217, 3292, 33, 3305, 3313, 3324, 3334, 3355, 3380, 3408, 3414, 3427, 3435, 3445, 3453, 3497, 3537, 3565, 3573, 3598, 3660, 3670, 3723, 3741, 3768, 377, 3783, 3790, 3828, 3842, 385, 3862, 3874, 3882, 3921, 4, 40, 408, 4096, 41, 4103, 4125, 4151, 4157, 4169, 42, 4204, 4221, 43, 4378, 44, 4461, 4467, 4473, 4485, 4492, 4499, 45, 4506, 4535, 46, 4615, 4671, 4676, 4681, 4686, 4692, 4698, 47, 4704, 4745, 4757, 4769, 4796, 48, 4809, 4815, 4821, 4850, 4900, 4908, 4962, 4997, 5, 50, 5002, 5012, 5051, 5066, 5074, 5096, 516, 5200, 5235, 5318, 5325, 5374, 5404, 5418, 5428, 5440, 5490, 5498, 5505, 5573, 5579, 56, 5624, 6, 60, 603, 612, 661, 680, 689, 7, 727, 73, 745, 773, 797, 8, 80, 81, 82, 83, 836, 850, 859, 87, 873, 88, 880, 9, 90, 91, 96, 961, 971, 979

## File: usr/bin/lua/ptz/LG.lua
**Ports**: 1, 10, 11, 12, 128, 13, 14, 15, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_venc.ko
**Ports**: 1, 10, 100, 13, 15, 16, 17, 18, 19, 2, 20, 2017, 21, 25, 264, 265, 3, 35, 38, 4, 40, 400, 41, 418, 42, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 54, 55, 6, 60, 61, 62, 65, 66, 67, 7, 75, 777, 787, 8, 80, 81, 82, 820, 83, 84, 840, 845, 85, 86, 860, 864, 87, 88, 89, 9, 95
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: web/js/usermanage.js
**Ports**: 1, 10, 100, 11, 110, 12, 16, 17, 190, 2, 20, 200, 24, 255, 27, 28, 3, 30, 31, 32, 37, 39, 4, 5, 6, 7, 8, 9

## File: web/js/automaintain.js
**Ports**: 1, 12, 2, 24, 400, 5, 500, 60, 65535, 7

## File: bin/ls
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/useronvif.htm
**Ports**: 31

## File: sbin/pppoe-start
**Ports**: 1412, 80

## File: web/js/alarmlink.js
**Ports**: 1, 10, 100, 16, 2, 255, 3, 300, 33, 350, 4, 5, 6, 60, 600, 64, 7, 8

## File: bin/iproute
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/platformHtm/GAYS.htm
**Ports**: 1, 10, 2, 3, 4, 5, 6

## File: usr/lib/lib.7z.extracted/0/lib/hi_rtc.ko
**Ports**: 1, 10, 2, 3, 4, 5, 7, 8, 88, 9

## File: web/js/serialconfig.js
**Ports**: 1, 1200, 19200, 2, 2400, 3, 38400, 4800, 5, 57600, 9600

## File: usr/lib/lib.7z.extracted/0/lib/osa.ko
**Ports**: 1, 10, 11, 2, 2017, 22, 3, 31, 32, 4, 40, 43, 47, 5, 50, 6, 7, 8, 80, 81, 83, 88, 888, 9
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/8192eu.ko
**Ports**: 1, 10, 1000, 101, 1010, 11, 111, 12, 1222, 13, 130, 14, 15, 1500, 16, 17, 18, 2, 20, 200, 2016, 202, 203, 21, 210, 211, 22, 222, 22224, 23, 23995, 24, 240, 2468, 25, 26, 28, 282, 2868, 29, 3, 30, 300, 3003, 303, 3055, 31, 32, 33, 34, 35, 355, 36, 38, 380, 381, 4, 40, 400, 4000, 403, 404, 4080, 41, 42, 43, 43003, 44, 440, 444, 45, 46, 47, 48, 4800, 488, 49, 5, 50, 502, 506, 5242, 53, 54, 544, 55, 555, 5555, 56, 57, 59, 6, 60, 61, 62, 63, 64, 640, 65, 66, 6644, 67, 7, 70, 700, 7080, 71, 717, 72, 7207, 7300, 74, 75, 77, 78, 8, 80, 800, 802, 805, 8051, 81, 82, 822, 83, 84, 85, 86, 864, 87, 870, 88, 8812, 8814, 8821, 8822, 888, 89, 9, 90, 900, 91, 93, 94, 95, 96, 960, 98, 980
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: Hex

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_region.ko
**Ports**: 1, 10, 111, 15, 16, 2, 20, 2017, 24, 3, 32, 36, 4, 40, 41, 42, 45, 47, 48, 5, 50, 52, 55, 57, 6, 64, 65, 67, 7, 70, 73, 75, 8, 80, 81, 82, 84, 85, 88, 9, 96

## File: usr/lib/lib.7z.extracted/0/lib/load_hisimod.sh
**Ports**: 1, 10, 101, 1024, 11, 11200, 12152, 1536, 1920, 2, 2015, 2048, 2500, 256, 31, 35, 37, 38, 39, 4, 40, 4050, 41, 42, 43, 44, 45, 49, 51, 512, 52, 53, 55, 56, 58, 59, 6, 60, 61, 62, 63, 67, 68, 7200, 78, 9120, 93, 95, 96, 97
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/css/ui.css
**Ports**: 1, 10, 100, 1000, 10000, 111, 2, 2013, 210, 25, 4, 40, 47, 5, 50, 6, 60, 8, 80, 9, 9999

## File: sbin/hdparm
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/SigFileList
**Ports**: 2
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/js/index.js
**Ports**: 1, 10, 100, 102, 1100, 1263, 16, 198, 2, 20, 2000, 208, 220, 224, 24, 25, 255, 28, 3, 30, 300, 33, 35, 37, 4, 40, 400, 42, 5, 50, 500, 56, 6, 67, 680, 70, 745, 8, 80, 85, 89, 9
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: Base64

## File: usr/sbin/usb_modeswitch
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/logmanage.htm
**Ports**: 1, 64
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_h264e.ko
**Ports**: 1, 10, 11, 118, 12, 128, 13, 15, 154, 16, 18, 1892, 19, 2, 2017, 22, 23, 24, 255, 3, 30, 304, 31, 32, 333, 34, 38, 39, 4, 40, 41, 42, 43, 44, 47, 48, 5, 51, 52, 53, 54, 6, 63, 64, 69, 7, 70, 8, 80, 802, 81, 85, 9

## File: web/js/alarmindex.js
**Ports**: 1, 100, 11, 19, 2, 20, 3, 30

## File: web/html/upnpconfig.htm
**Ports**: 1, 65535

## File: sbin/3gpp
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/SigFileList
**Ports**: 54, 60, 75, 90, 97, 99

## File: bin/mkdir
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/getty
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi_i2c.ko
**Ports**: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9

## File: sbin/rmmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/mount
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/Component/chnlGroup.js
**Ports**: 1, 2

## File: web/js/alarmboxcfg.js
**Ports**: 1

## File: usr/bin/lua/ptz/PELCOD-S.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: etc/udev/rules.d/97-bluetooth-serial.rules
**Ports**: 504, 620

## File: bin/ipaddr
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/data/Data/StringAll.7z.extracted/0/StringAll
**Ports**: 1, 10, 100, 1000, 10000, 1025, 11, 110, 12, 120, 128, 13, 14, 15, 16, 17, 18, 180, 19, 2, 20, 200, 2000, 21, 22, 223, 224, 23, 239, 24, 25, 250, 254, 255, 26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 365, 37, 37777, 38, 3800, 39, 4, 40, 4000, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 500, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65535, 7, 701, 8, 801, 803, 85, 9, 90, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: DES, SSL

## File: sbin/lsmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/alarmout.js
**Ports**: 1, 2, 8

## File: usr/bin/lua/ptz/CP-CVI2.0.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 7, 80

## File: web/js/audiocfg.js
**Ports**: 1, 10

## File: bin/pwd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libpthread.so.0
**Ports**: 1, 2, 20, 2006, 22, 3, 30, 33, 4, 40, 404, 414, 42, 44, 47, 5, 6, 7, 8, 80, 81, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: bin/dd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/Banknote.lua
**Ports**: 1, 2, 200, 3, 5, 6, 7, 8

## File: usr/bin/lua/ptz/WV-CS850II.lua
**Ports**: 1, 10, 100, 13, 14, 15, 16, 1610, 17, 2, 200, 3, 4, 5, 6, 64, 7, 8, 9, 99

## File: usr/lib/lib.7z.extracted/0/lib/crgctrl_hi3521a.sh
**Ports**: 13, 148, 32, 74

## File: web/js/defaultcfg.js
**Ports**: 1, 100, 108, 168, 192, 2, 20, 200, 30, 300, 4

## File: lib/libthread_db-0.9.33.2.so
**Ports**: 1, 10, 11, 2, 3, 33, 4, 40, 41, 411, 5, 6, 7, 8, 80, 9

## File: bin/killall
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/inetd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/mknod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/compat-5.1.lua
**Ports**: 1, 12, 19, 2, 2004, 2005, 5, 7

## File: usr/lib/lib.7z.extracted/0/lib/option.ko
**Ports**: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9

## File: lib/libgcc_s.so.1
**Ports**: 1, 101, 13, 2, 208, 3, 320, 35, 36, 38, 4, 40, 404, 45, 5, 50, 51, 52, 55, 6, 63, 7, 8, 80, 83, 87, 9, 91
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: bin/mv
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libhive_common.so
**Ports**: 1, 1073, 16, 1602, 2, 26, 3, 4, 400, 404, 5, 6, 7, 8, 80, 8808, 8813, 9, 93
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_aenc.ko
**Ports**: 1, 10, 12, 13, 16, 18, 19, 2, 2017, 3, 32, 4, 40, 44, 46, 5, 50, 6, 7, 8, 80, 84, 87, 88, 89, 9

## File: usr/lib/lib.7z.extracted/0/lib/hifb.ko
**Ports**: 1, 10, 13, 140, 16, 1620, 18, 180, 19, 2, 2017, 255, 26, 27, 3, 32, 39, 4, 40, 4080, 41, 45, 46, 48, 49, 5, 50, 51, 6, 7, 720, 8, 80, 800, 804, 808, 81, 810, 8100, 84, 85, 86, 88, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
### Encryption/Encoding: DES

## File: usr/lib/lib.7z.extracted/0/lib/mmz.ko
**Ports**: 1, 10, 2, 3, 4, 40, 5, 6, 7, 8, 80, 88, 880, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vfmw.ko
**Ports**: 1, 10, 11, 111, 12, 13, 14, 141, 145, 16, 18, 1892, 19, 2, 20, 2017, 219, 22, 220, 222, 2222, 23, 24, 240, 25, 26, 263, 27, 28, 291, 3, 303, 32, 322, 33, 35, 4, 40, 4000, 409, 41, 42, 43, 44, 45, 458, 46, 47, 48, 5, 5000, 532, 55, 556, 587, 6, 65, 65535, 7, 76, 77, 8, 80, 800, 81, 82, 84, 86, 88, 89, 9, 90, 900, 92, 95

## File: usr/lib/lib.7z.extracted/0/lib/avss.ko
**Ports**: 1, 10, 2, 2017, 29, 3, 32, 35, 4, 5, 6, 7, 8, 9
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
### Encryption/Encoding: AES, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_ai.ko
**Ports**: 1, 10, 100, 10240, 13, 18, 19, 2, 200, 2017, 250, 3, 30, 350, 4, 40, 41, 43, 44, 46, 5, 500, 55, 6, 7, 71, 73, 8, 80, 800, 81, 83, 84, 88, 9, 99

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_ao.ko
**Ports**: 1, 10, 100, 10240, 13, 18, 19, 2, 20, 200, 2017, 250, 3, 350, 4, 40, 41, 42, 43, 44, 45, 46, 5, 500, 51, 55, 6, 7, 8, 80, 800, 82, 85, 86, 9

## File: web/jsBase/lib/m1.2.js
**Ports**: 1, 10, 100, 11, 111, 120, 13, 16, 18, 19, 2, 20, 200, 24, 250, 27, 3, 300, 32, 37, 38, 39, 4, 40, 419, 420, 46, 5, 50, 500, 6, 60, 618, 7, 8, 9, 925, 950
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex

## File: etc/init.d/S80network
**Ports**: 1, 127, 2

## File: usr/bin/lua/ptz/HAIYU.lua
**Ports**: 200, 256, 3, 4, 5, 6, 7

## File: bin/df
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ATMHead.lua
**Ports**: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/jsBase/lib/qrcode.js
**Ports**: 1, 10, 100, 102, 104, 106, 108, 11, 110, 112, 114, 116, 118, 12, 121, 122, 126, 128, 13, 130, 132, 1335, 134, 136, 138, 14, 142, 146, 15, 150, 154, 158, 16, 162, 166, 17, 170, 18, 19, 2, 20, 21522, 22, 236, 24, 25, 255, 256, 26, 27, 28, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 4095, 41, 42, 43, 44, 46, 47, 48, 49, 5, 50, 52, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 65, 66, 67, 68, 69, 7, 70, 72, 74, 76, 78, 7973, 8, 80, 82, 84, 86, 87, 9, 90, 94, 97, 98

## File: etc/udev/rules.d/75-persistent-net-generator.rules.optional
**Ports**: 390, 9

## File: web/js/ddnsconfig.js
**Ports**: 1, 10, 1092, 12, 13, 15, 16, 2, 22, 3, 4, 5, 500, 60, 65535, 7, 8, 80, 801, 803, 9, 901, 907, 908, 909, 910, 911, 912, 929

## File: web/js/recordcontrol.js
**Ports**: 1, 16, 2, 24, 25, 32, 50, 512, 600

## File: usr/lib/lib.7z.extracted/0/lib/sysctl_hi3521a_asic.sh
**Ports**: 128, 19, 2, 32, 6, 7, 8

## File: lib/SigFileList
**Ports**: 1, 2, 33, 6, 9

## File: init
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/devmem
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_sys.ko
**Ports**: 1, 10, 13, 18, 19, 2, 2017, 22, 3, 30, 33, 4, 42, 5, 6, 7, 8, 80, 86, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/bin/lua/PTZCtrl.lua
**Ports**: 1, 10, 14, 15, 16, 1992, 2, 2005, 2006, 22, 2416, 256, 3, 31, 32, 33, 4, 43, 5, 6, 63, 64, 9

## File: web/css/previewindex.css
**Ports**: 1, 100, 1001, 13, 140, 2, 210, 255, 333, 8, 80

## File: web/js/ipcFaceNewConfig.js
**Ports**: 1, 10, 100, 2, 255, 3, 300, 35, 350, 374, 4, 450, 7, 8192
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: usr/bin/lua/ptz/SUNKWANG.lua
**Ports**: 10, 11, 12, 13, 14, 15, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: lib/libc.so.0
**Ports**: 1, 10, 100, 1020, 105, 109, 11, 110, 111, 1111, 11111, 1121, 12, 1234, 124, 13, 133, 14, 141, 145, 15, 1535, 16, 17, 17641, 18, 186, 1872, 1873, 19, 1912, 1913, 1926, 1927, 1989, 1990, 2, 20, 202, 20212, 2033, 2078, 208, 21, 2133, 22, 222, 2222, 22222, 22223, 22224, 228, 23, 234, 2345, 24, 245, 246, 25, 256, 26, 263, 27, 27751, 28, 288, 29, 3, 30, 300, 303, 306, 31, 32, 320, 321, 33, 333, 3345, 33744, 34, 342, 344, 35, 36, 37, 376, 38, 39, 4, 40, 401, 4050, 408, 4080, 41, 4151, 42, 4289, 43, 432, 4353, 44, 44355, 444, 4467, 45, 46, 47, 48, 49, 498, 5, 50, 51, 51305, 52, 5289, 53, 54, 543, 55, 551, 56, 5666, 5678, 56789, 57, 571, 572, 58, 588, 59, 5945, 6, 60, 600, 61, 613, 62, 620, 6272, 63, 64, 65, 66, 666, 67, 68, 682, 683, 69, 699, 7, 70, 701, 703, 71, 72, 73, 7383, 74, 7407, 75, 757, 76, 769, 77, 777, 78, 785, 789, 79, 793, 794, 8, 80, 800, 807, 808, 8080, 81, 813, 815, 818, 82, 83, 831, 84, 848, 85, 86, 87, 88, 8859, 89, 899, 9, 90, 900, 91, 92, 93, 94, 95, 96, 964, 97, 98, 99, 999, 9999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/jsCore/common.js
**Ports**: 1, 10, 100, 1024, 11, 12, 12345, 128, 1280, 130, 149, 150, 1536, 160, 1792, 192, 2, 20, 2048, 224, 24, 256, 28, 29, 3, 30, 31, 32, 320, 37, 384, 39, 4, 40, 400, 448, 48, 50, 512, 6, 64, 640, 7, 70, 768, 80, 8192, 896, 9, 96

## File: etc/Wireless/RT2870STA/RT2870STA.dat
**Ports**: 1, 100, 2346, 2347, 3, 33, 4, 5, 64, 7, 70

## File: web/css/oem.css
**Ports**: 100, 13, 2, 210, 333, 900, 999

## File: bin/wget
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/librt-0.9.33.2.so
**Ports**: 1, 2, 4, 40, 5, 6, 7, 8, 80, 9

## File: sbin/lspci
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/localstorage.js
**Ports**: 1, 10, 100, 1024, 1500, 2, 200, 3, 30, 32, 350, 5, 60

## File: web/html/playbackindex.htm
**Ports**: 1, 10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 192, 2, 20, 2012, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 32, 4, 5, 51, 55, 59, 6, 64, 7, 8, 9

## File: web/js/chnlname.js
**Ports**: 1, 10, 2, 3, 31, 63

## File: lib/libm-0.9.33.2.so
**Ports**: 1, 101, 11, 12, 135, 14, 18, 182, 2, 208, 22, 23, 24, 3, 30, 320, 33333, 375, 4, 40, 42, 43, 44, 45, 46, 47, 5, 50, 51, 53, 55, 56, 6, 60, 62, 7, 75, 8, 80, 81, 82, 83, 8353, 84, 85, 87, 9

## File: usr/etc/Global.lua
**Ports**: 1, 10, 1024, 11, 12, 128, 13, 14, 15, 16, 16384, 17, 18, 19, 1992, 2, 20, 2005, 2006, 2048, 21, 22, 23, 24, 25, 255, 256, 26, 27, 28, 29, 3, 30, 31, 32, 32768, 33, 34, 35, 36, 4, 4096, 5, 512, 5264, 6, 60, 64, 7, 8, 8192, 9

## File: bin/iprule
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/modprobe
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/webplugin.exe
**Ports**: 1, 10, 1000, 11, 12, 124, 13, 136, 138, 139, 14, 15, 1546, 16, 17, 175, 18, 185, 19, 195, 2, 20, 200, 2006, 21, 22, 23, 233, 24, 25, 251, 26, 263, 27, 2713, 273, 28, 29, 3, 30, 31, 3130, 32, 328, 33, 333, 338, 34, 35, 36, 3652, 37, 38, 388, 39, 392, 394, 4, 40, 402, 41, 411, 42, 421, 429, 43, 44, 45, 451, 46, 47, 471, 472, 48, 483, 49, 5, 50, 51, 52, 53, 54, 55, 56, 5670, 57, 58, 581, 59, 590, 5925, 6, 60, 61, 62, 63, 64, 65, 66, 67, 675, 68, 69, 690, 7, 70, 709, 71, 717, 72, 73, 736, 7364, 74, 741, 75, 76, 77, 774, 78, 781, 786, 79, 8, 80, 81, 816, 82, 83, 84, 85, 857, 86, 87, 877, 88, 89, 9, 90, 91, 92, 927, 93, 94, 944, 947, 95, 950, 96, 961, 965, 97, 978, 98, 99, 991, 9986
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: web/js/remotestorage.js
**Ports**: 1, 10, 16, 19, 2, 3, 31, 32, 5, 60, 600, 65535, 7

## File: web/js/chanlhddquota.js
**Ports**: 1, 10, 100, 120, 1500, 2, 25, 350, 4, 50, 75

## File: usr/data/Data/cursors/hand.cur
**Ports**: 9

## File: bin/passwd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/sbin/3gconfig
**Ports**: 1, 11, 1500, 98

## File: web/js/ft.js
**Ports**: 2017

## File: usr/data/Data/cursors/arrow.cur
**Ports**: 8

## File: usr/data/config.lua
**Ports**: 1, 10, 120, 144, 168, 176, 192, 2, 23, 240, 255, 288, 3, 32, 320, 352, 4, 480, 576, 6, 640, 720

## File: web/js/snmpconfig.js
**Ports**: 1, 123, 1900, 2, 21, 31, 32, 37810, 3800, 39999, 5, 5050, 65535, 9999

## File: web/html/infoindex.htm
**Ports**: 1, 1999, 2, 6, 7, 8

## File: web/html/broadcast.htm
**Ports**: 1025, 224, 239, 255, 65000

## File: usr/lib/lib.7z
**Ports**: 1, 10, 101, 106, 11, 12, 121, 13, 14, 15, 16, 162, 167, 17, 174, 179, 18, 19, 2, 20, 203, 21, 217, 218, 22, 2273, 23, 234, 236, 24, 245, 25, 255, 257, 26, 260, 27, 270, 271, 28, 29, 292, 299, 3, 30, 31, 32, 33, 34, 342, 343, 349, 35, 36, 364, 369, 37, 371, 38, 39, 3950, 396, 4, 40, 404, 41, 42, 422, 426, 428, 43, 437, 44, 45, 453, 46, 467, 47, 470, 475, 477, 48, 489, 49, 497, 5, 50, 501, 51, 52, 529, 53, 537, 54, 548, 55, 56, 560, 564, 57, 571, 58, 581, 582, 59, 591, 595, 6, 60, 61, 62, 627, 63, 64, 643, 65, 66, 67, 68, 685, 69, 7, 70, 706, 71, 72, 724, 729, 73, 732, 74, 741, 743, 75, 753, 7559, 758, 76, 77, 78, 79, 791, 793, 798, 8, 80, 81, 82, 820, 8255, 83, 84, 85, 86, 863, 87, 873, 88, 882, 887, 89, 9, 90, 900, 91, 910, 915, 92, 927, 93, 938, 94, 945, 95, 96, 962, 97, 972, 973, 98, 983, 99, 992
### Encryption/Encoding: Hex

## File: sbin/upgraded
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoD_Tour.lua
**Ports**: 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: usr/lib/lib.7z.extracted/0/lib/hi_media.ko
**Ports**: 1, 10, 18, 2, 3, 31, 4, 6, 7, 8, 80, 9

## File: web/Component/schedule.htm
**Ports**: 1, 10, 12, 14, 16, 18, 2, 20, 22, 24, 3, 4, 5, 6, 7, 8

## File: usr/lib/lib.7z.extracted/0/lib/usb_wwan.ko
**Ports**: 1, 10, 2, 3, 4, 5, 6, 7, 8, 9

## File: bin/[[
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/update.htm
**Ports**: 1
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: bin/printenv
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/du
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: boot/uImage
**Ports**: 1, 10, 100, 11, 12, 129, 13, 14, 146, 15, 159, 16, 161, 163, 17, 1700, 18, 183, 186, 19, 19194, 2, 20, 21, 210, 212, 22, 222, 224, 23, 230, 24, 240, 243, 2446, 25, 252, 253, 256, 26, 263, 27, 28, 285, 288, 29, 3, 30, 31, 314, 318, 319, 32, 33, 331, 335, 336, 34, 342, 345, 346, 35, 357, 36, 360, 363, 37, 371, 377, 38, 383, 384, 39, 395, 4, 40, 405, 41, 419, 42, 43, 44, 45, 453, 46, 47, 475, 48, 480, 49, 5, 50, 500, 51, 516, 52, 523, 53, 54, 544, 548, 55, 554, 557, 56, 566, 57, 577, 58, 588, 59, 6, 60, 61, 6116, 615, 62, 621, 623, 63, 634, 64, 65, 659, 66, 67, 673, 68, 69, 696, 7, 70, 709, 71, 719, 72, 73, 730, 737, 739, 74, 75, 752, 753, 757, 759, 76, 764, 766, 77, 78, 783, 789, 79, 791, 798, 8, 80, 808, 81, 82, 826, 828, 83, 837, 84, 844, 845, 847, 85, 855, 859, 86, 862, 87, 88, 89, 894, 896, 9, 90, 901, 91, 911, 914, 918, 92, 923, 93, 938, 94, 9412, 942, 95, 954, 96, 965, 966, 969, 97, 971, 977, 98, 989, 99

## File: boot/uImage.extracted/0/Linux-3.10.0.bin
**Ports**: 1, 10, 100, 11, 12, 129, 13, 14, 146, 15, 159, 16, 161, 163, 17, 1700, 18, 183, 186, 19, 19194, 2, 20, 21, 210, 212, 22, 222, 224, 23, 230, 24, 240, 243, 2446, 25, 252, 253, 256, 26, 263, 27, 28, 285, 288, 29, 3, 30, 31, 314, 318, 319, 32, 33, 331, 335, 336, 34, 342, 345, 346, 35, 357, 36, 360, 363, 37, 371, 377, 38, 383, 384, 39, 395, 4, 40, 405, 41, 419, 42, 43, 44, 45, 453, 46, 47, 475, 48, 480, 49, 5, 50, 500, 51, 516, 52, 523, 53, 54, 544, 548, 55, 554, 557, 56, 566, 57, 577, 58, 588, 59, 6, 60, 61, 6116, 615, 62, 621, 623, 63, 634, 64, 65, 659, 66, 67, 673, 68, 69, 696, 7, 70, 709, 71, 719, 72, 73, 730, 737, 739, 74, 75, 752, 753, 757, 759, 76, 764, 766, 77, 78, 783, 789, 79, 791, 798, 8, 80, 808, 81, 82, 826, 828, 83, 837, 84, 844, 845, 847, 85, 855, 859, 86, 862, 87, 88, 89, 894, 896, 9, 90, 901, 91, 911, 914, 918, 92, 923, 93, 938, 94, 9412, 942, 95, 954, 96, 965, 966, 969, 97, 971, 977, 98, 989, 99

## File: bin/ping6
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/LiveUpdate.lua
**Ports**: 1, 11, 12, 1992, 2005, 2006, 29, 4, 4957, 5, 6
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/jsCore/rsa.js
**Ports**: 1, 10, 11, 12, 127, 128, 14, 15, 16, 16383, 192, 2, 2048, 224, 24, 255, 256, 26, 28, 3, 30, 32, 32767, 36, 4, 5, 52, 6, 63, 65535, 7, 8, 9
### Encryption/Encoding: Hex, RSA

## File: sbin/chat
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/gzip
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libm.so.0
**Ports**: 1, 101, 11, 12, 135, 14, 18, 182, 2, 208, 22, 23, 24, 3, 30, 320, 33333, 375, 4, 40, 42, 43, 44, 45, 46, 47, 5, 50, 51, 53, 55, 56, 6, 60, 62, 7, 75, 8, 80, 81, 82, 83, 8353, 84, 85, 87, 9

## File: web/js/eventScript.js
**Ports**: 1, 2, 3, 4, 500, 6, 8192

## File: web/html/ipcFaceNewConfig.htm
**Ports**: 1, 10, 100, 3, 300, 35, 50, 500, 600

## File: web/css/setindex.css
**Ports**: 1, 10, 100, 1000, 10001, 101, 5, 50, 6, 7, 70, 8, 80

## File: web/js/blackwhite.js
**Ports**: 1, 190, 2, 200, 64

## File: etc/Data_Signature
**Ports**: 3

## File: web/js/infoindex.js
**Ports**: 1, 6, 8, 9

## File: web/js/previewindex.js
**Ports**: 1, 10, 100, 11, 12, 120, 125, 127, 128, 13, 14, 16, 17, 19, 190, 2, 20, 200, 24, 25, 287, 3, 310, 32, 36, 37, 4, 480, 5, 50, 500, 51, 534, 6, 60, 64, 7, 77, 78, 8, 80, 85, 9
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
### Encryption/Encoding: Base64

## File: bin/nice
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/guiset.js
**Ports**: 1, 10, 100, 1024, 12, 120, 128, 1280, 1536, 16, 160, 1792, 192, 2, 20, 200, 2048, 2160, 224, 25, 255, 256, 27, 3, 30, 32, 320, 350, 36, 375, 382, 384, 3840, 4, 4096, 448, 48, 5, 50, 512, 5569, 5570, 6, 60, 6144, 64, 640, 768, 8, 80, 8191, 8192, 896, 9, 96

## File: usr/data/Data/StringAll.7z
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 24, 25, 27, 28, 29, 3, 30, 31, 32, 329, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 45, 47, 48, 49, 5, 50, 5266, 53, 55, 57, 58, 59, 6, 60, 61, 619, 62, 63, 64, 66, 665, 68, 69, 7, 70, 71, 73, 736, 74, 75, 758, 77, 78, 788, 8, 80, 83, 84, 85, 87, 89, 9, 90, 91, 94, 95, 96, 97, 98

## File: usr/bin/lua/ptz/PelcoP.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 5, 6, 8

## File: etc/init.d/S00devs
**Ports**: 1, 13, 204, 32, 5, 63, 64, 65, 66, 67

## File: bin/ifenslave
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/Videon-X.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: usr/bin/lua/ptz/PelcoD-DON.lua
**Ports**: 14, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: usr/bin/lua/ptz/Mercer-1.lua
**Ports**: 1, 10, 100, 1000, 16, 1610, 2, 200, 3, 4, 5, 6, 8

## File: web/html/encodecfg.htm
**Ports**: 1, 10, 100, 1024, 128, 1280, 1536, 160, 17, 1792, 192, 2, 2048, 224, 25, 255, 256, 3, 32, 320, 33, 35, 384, 4, 4096, 448, 48, 5, 500, 512, 6, 64, 640, 7, 768, 80, 896, 96

## File: bin/sleep
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/sh
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/css/fn.css
**Ports**: 1, 10, 100, 11, 12, 13, 15, 17, 18, 19, 2, 20, 21, 25, 3, 30, 35, 40, 45, 5, 50, 55, 6, 60, 67, 7, 8, 9, 90, 96

## File: usr/bin/lua/ptz/PelcoP-A.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 5, 6, 7, 8

## File: web/js/Grid.js
**Ports**: 1, 4

## File: usr/bin/lua/ptz/RM110.lua
**Ports**: 128, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_viu.ko
**Ports**: 1, 10, 11, 1120, 12, 13, 14181, 15, 16, 18, 180, 19, 2, 2017, 22, 26, 270, 28000, 3, 30, 32, 34, 4, 40, 4004, 404, 4096, 41, 42, 43, 44, 444, 45, 46, 47, 4787, 48, 484, 49, 5, 50, 51, 54, 58, 5878, 59, 6, 600, 68, 69, 7, 71, 747, 78, 8, 80, 8000, 81, 828, 844, 86, 88, 884, 89, 9, 90, 99

## File: bin/cat
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_chnl.ko
**Ports**: 1, 10, 11, 13, 18, 19, 2, 2017, 23, 3, 33, 4, 40, 46, 5, 6, 7, 8, 80, 81, 84, 85, 86, 9

## File: usr/bin/lua/ptz/PelcoD1_Tour.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: lib/libcrypt-0.9.33.2.so
**Ports**: 1, 2, 3, 4, 44, 5, 6, 7, 8, 80, 9, 91
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: bin/iplink
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/i2c_write
**Ports**: 1, 2, 3, 4, 40, 5, 6, 8, 80, 8808, 8813, 9

## File: web/js/chnltype.js
**Ports**: 1, 1080, 1920, 2

## File: web/html/videodetect.htm
**Ports**: 1, 10, 100, 2, 3, 300, 32, 4, 5, 50, 6, 600, 65535, 7, 8, 9

## File: web/js/ptzconfig.js
**Ports**: 1, 1200, 19200, 2, 2400, 255, 3, 38400, 4, 4800, 5, 57600, 9600, 9750, 999, 9999

## File: usr/bin/Challenge
**Ports**: 1, 10, 100, 1000, 10000, 10005, 1001, 10038, 1004, 101, 1010, 1011, 1014, 10141, 1016, 10181, 102, 1024, 103, 104, 1048, 106, 10646, 107, 108, 1080, 1084, 109, 11, 110, 1100, 1101, 11040, 1108, 111, 1111, 11111, 1115, 1140, 11520, 11548, 118, 119, 12, 120, 1200, 1202, 121, 1212, 12186, 122, 123, 12357, 125, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1261, 1264, 1265, 1268, 127, 12728, 1276, 128, 1280, 129, 13, 130, 1300, 1305, 131, 1310, 1315, 13397, 134, 135, 1360, 1366, 1394, 14, 140, 1400, 1404, 14040, 1408, 141, 1410, 1414, 142, 144, 1440, 1451, 147, 148, 1483, 149, 15, 1500, 151, 1515, 152, 1536, 155, 15804, 16, 160, 1600, 163, 16383, 166, 168, 169, 17, 1701, 172, 176, 17958, 18, 180, 18000, 1801, 1808, 181, 182, 185, 186, 188, 189, 1892, 19, 190, 191, 192, 1920, 19200, 1944, 1968, 1969, 1970, 1972, 1973, 1978, 1980, 1981, 1983, 1984, 1985, 1987, 1988, 1989, 1990, 1992, 1994, 1995, 1996, 1997, 1998, 2, 20, 200, 2000, 20000, 2001, 2002, 2003, 2004, 2005, 2006, 20085, 2009, 201, 2010, 2011, 2012, 2014, 2015, 2016, 2017, 202, 2020, 2022, 203, 2030, 2031, 204, 2040, 2048, 206, 207, 208, 20820, 2099, 21, 210, 2105, 211, 2110, 21111, 2115, 21466, 21474, 215, 21518, 2155, 2160, 217, 2193, 22, 2200, 221, 222, 2222, 22222, 223, 224, 225, 226, 228, 23, 2302, 23022, 2303, 231, 2312, 232, 234, 23572, 239, 24, 240, 2400, 24040, 241, 242, 24383, 245, 248, 249, 25, 250, 251, 252, 2530, 254, 255, 256, 2560, 25834, 2592, 26, 261, 262, 2625, 263, 264, 265, 266, 27, 272, 277, 278, 28, 280, 2805, 28080, 281, 28147, 2815, 282, 2820, 2824, 2825, 283, 284, 286, 288, 29, 290, 292, 29340, 2941, 2959, 299, 3, 30, 300, 3000, 3002, 3003, 3004, 301, 302, 3020, 304, 305, 306, 307, 308, 3082, 30830, 309, 31, 310, 3105, 31080, 311, 3110, 3115, 312, 3120, 313, 3130, 3135, 3155, 317, 318, 31802, 32, 320, 3200, 3203, 32160, 32767, 33, 330, 3303, 332, 3322, 333, 3333, 334, 3370, 34, 340, 34080, 341, 3410, 343, 344, 348, 35, 351, 352, 354, 355, 36, 360, 3600, 362, 366, 3666, 368, 37, 3743, 3779, 38, 380, 3800, 381, 382, 3823, 383, 3830, 384, 3840, 38400, 386, 388, 39, 390, 392, 393, 4, 40, 400, 4000, 40000, 4004, 40040, 40080, 401, 4018, 4019, 402, 40200, 4024, 403, 404, 4040, 40404, 4041, 4048, 405, 406, 407, 4070, 408, 4080, 40800, 4085, 409, 41, 410, 4100, 4101, 411, 412, 4124, 413, 414, 4140, 4144, 415, 41571, 416, 41692, 417, 418, 4181, 419, 42, 420, 4200, 421, 422, 423, 4232, 424, 4242, 426, 4282, 429, 43, 430, 4300, 4322, 433, 434, 4340, 436, 438, 44, 440, 4400, 44025, 4404, 44040, 44080, 441, 44100, 442, 443, 444, 4444, 446, 448, 4481, 45, 450, 453, 454, 45678, 457, 458, 4585, 46, 460, 461, 464, 466, 467, 47, 474, 48, 480, 4800, 48000, 482, 4838, 484, 485, 49, 490, 49152, 494, 4980, 499, 5, 50, 500, 5000, 50000, 5001, 5003, 5004, 501, 5010, 5011, 5020, 503, 505, 506, 5060, 5061, 507, 5080, 5083, 5084, 509, 51, 510, 5100, 5101, 5105, 5115, 512, 514, 515, 5155, 518, 519, 52, 5200, 524, 53, 530, 5300, 531, 5320, 53493, 535, 538, 54, 540, 54040, 5408, 542, 543, 545, 546, 548, 55, 550, 552, 555, 5554, 56, 561, 5634, 564, 566, 5678, 56789, 569, 57, 570, 5708, 576, 57600, 577, 58, 580, 5805, 58080, 582, 583, 5898, 59, 592, 599, 6, 60, 600, 6000, 6003, 6004, 601, 602, 6020, 606, 6060, 607, 608, 6083, 6084, 61, 610, 6101, 616, 62, 620, 6252, 626, 627, 629, 63, 630, 631, 633, 636, 639, 64, 640, 6404, 64040, 6412, 642, 646, 65, 650, 653, 66, 660, 666, 6666, 668, 67, 673, 678, 679, 68, 680, 681, 682, 689, 69, 690, 698, 699, 7, 70, 700, 7000, 7001, 7002, 7004, 701, 7011, 703, 704, 705, 706, 7061, 7070, 708, 7080, 7082, 71, 711, 72, 720, 722, 726, 727, 729, 73, 730, 7303, 736, 74, 740, 747, 75, 750, 757, 76, 762, 765, 768, 77, 770, 771, 773, 774, 777, 778, 78, 780, 7808, 781, 784, 788, 789, 79, 794, 798, 8, 80, 800, 8000, 8004, 8008, 801, 802, 8020, 803, 804, 8040, 8041, 8048, 805, 8050, 806, 807, 808, 8080, 809, 81, 810, 8100, 8101, 811, 812, 813, 8130, 814, 8141, 818, 8180, 8185, 8188, 819, 8192, 82, 820, 8200, 8212, 8222, 824, 827, 828, 83, 830, 8300, 8303, 8360, 8365, 838, 839, 84, 840, 841, 843, 844, 848, 85, 850, 858, 8580, 86, 860, 8600, 866, 868, 8686, 87, 874, 878, 879, 88, 880, 8800, 8807, 8808, 881, 8818, 882, 8831, 8859, 886, 887, 888, 8890, 89, 890, 896, 898, 899, 9, 90, 900, 9000, 901, 902, 903, 904, 905, 906, 907, 908, 909, 91, 910, 911, 912, 9130, 918, 92, 920, 922, 9272, 9279, 9282, 929, 93, 930, 936, 939, 94, 940, 9401, 941, 942, 943, 949, 95, 950, 959, 96, 960, 9600, 963, 9640, 966, 9660, 969, 97, 974, 977, 9786, 979, 98, 980, 988, 9889, 99, 9969, 999, 9999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: AES, Base64, DES, Hex, RSA, SSL, TLS

## File: web/html/previewindex.htm
**Ports**: 1, 10, 100, 11, 12, 128, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 31, 32, 36, 3600, 4, 5, 6, 62, 64, 7, 8, 80, 9, 900

## File: usr/bin/lua/ptz/PELCOD-S1.lua
**Ports**: 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: bin/umount
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/netinit
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/SONY.lua
**Ports**: 1, 128, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: usr/bin/lua/ptz/Samsung.lua
**Ports**: 1, 11, 12, 13, 14, 15, 16, 1610, 17, 18, 2, 20, 200, 21, 22, 226, 23, 24, 25, 256, 26, 27, 3, 30, 4, 40, 5, 50, 6, 67, 7, 8, 80, 86, 9

## File: web/js/setindex.js
**Ports**: 1, 10, 11, 12, 2, 20, 23, 232, 272, 288, 320, 4, 485, 5, 6, 610, 686, 7, 8, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vpss.ko
**Ports**: 1, 10, 100, 1000, 11, 12, 1280, 13, 14, 1418, 16, 17, 177, 180, 19, 2, 20, 200, 2017, 202, 24, 25, 255, 26, 270, 28, 3, 31, 32, 33, 333, 35, 4, 40, 400, 401, 4096, 41, 42, 431, 433, 44, 45, 4585, 46, 48, 49, 5, 50, 54, 545, 55, 550, 58, 6, 60, 61, 611, 63, 65, 66, 661, 7, 70, 74, 77, 7707, 771, 776, 8, 80, 801, 81, 82, 83, 833, 84, 840, 846, 85, 8554, 86, 8606, 866, 87, 88, 881, 888, 89, 8906, 895, 9, 90, 96, 966, 999
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: sbin/pppoe
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/SAE.lua
**Ports**: 1, 10, 11, 12, 127, 16, 1610, 2, 200, 23, 254, 256, 3, 4, 5, 6, 7, 8, 8192, 9

## File: sbin/fdisk
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_hdmi.ko
**Ports**: 1, 10, 1024, 11, 11025, 1152, 12000, 1280, 13, 14, 16, 16000, 17, 176, 18, 19, 192, 2, 20, 2017, 21, 22050, 23, 24, 24000, 3, 30, 32, 32000, 33, 38, 4, 40, 400, 408, 41, 42, 43, 44, 44100, 45, 46, 47, 48, 480, 48000, 49, 5, 50, 51, 52, 6, 60, 600, 601, 62, 624, 63, 640, 67, 7, 709, 71, 720, 73, 768, 8, 80, 800, 8000, 8002, 804, 81, 819, 82, 83, 832, 84, 85, 870, 88, 89, 9, 90, 91, 96

## File: web/jsBase/lib/base64.js
**Ports**: 1, 12, 127, 128, 15, 191, 192, 2, 2048, 224, 3, 31, 4, 6, 63, 64, 9
### Encryption/Encoding: Base64

## File: web/html/connetcfg.htm
**Ports**: 1, 1025, 128, 65535

## File: usr/bin/lua/ptz/PelcoD1.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: usr/bin/lua/init.lua
**Ports**: 1, 10, 1024, 11, 12, 128, 13, 14, 15, 16, 16384, 17, 18, 19, 2, 20, 2005, 2006, 2048, 21, 22, 23, 24, 25, 255, 256, 26, 27, 28, 29, 3, 30, 31, 32, 32768, 33, 34, 35, 36, 4, 4096, 5, 512, 5264, 58, 59, 6, 61, 62, 64, 7, 8, 8192, 9

## File: web/Component/schedule.js
**Ports**: 1, 10, 11, 2, 21, 24, 280, 3, 320, 3600, 4, 40, 444, 5, 527, 6, 60, 65531, 65533, 65534, 7, 8

## File: web/html/localconfig.htm
**Ports**: 1, 10, 11, 12, 13, 2, 2012, 24, 3, 30, 4, 45, 5, 6, 60, 63, 64, 65535, 7, 8, 9, 998

## File: etc/inittab
**Ports**: 1999, 2004, 38400, 4, 57600, 8, 9600
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: bin/Data_Signature
**Ports**: 9

## File: bin/busybox
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/videodetect.js
**Ports**: 1, 10, 100, 10000, 120, 15, 16, 18, 2, 22, 24, 25, 255, 26, 3, 30, 300, 33, 350, 4, 451, 50, 500, 580, 600, 64, 7, 8, 9

## File: web/html/blackwhite.htm
**Ports**: 1, 64

## File: web/js/deviceInitial.js
**Ports**: 1, 10, 12, 17, 2, 20, 3, 31, 6, 63

## File: usr/etc/load_modules.sh
**Ports**: 2, 777

## File: bin/uname
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/https.js
**Ports**: 1, 127, 2, 20, 200, 3, 4, 63, 80, 800

## File: bin/eject
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/IVSConfig.htm
**Ports**: 10, 3, 300, 6, 600

## File: web/css/reset.css
**Ports**: 10, 100, 2013, 400, 5, 8

## File: usr/bin/lua/ptz/SIERA-P.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 4, 5, 6, 7, 8

## File: etc/init.d/S02wndev
**Ports**: 113, 203, 25

## File: usr/bin/lua/ptz/SANTACHI.lua
**Ports**: 1, 10, 16, 1610, 18, 2, 200, 23, 24, 3, 4, 45, 6, 7, 8, 9, 99

## File: web/html/diskerror.htm
**Ports**: 1, 10, 12, 2, 3, 300, 32, 4, 60, 600, 7

## File: sbin/ifdown
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/udev/rules.d/54-gphoto.rules
**Ports**: 1, 2, 4, 5, 6, 660, 8, 98

## File: web/js/imageprty.js
**Ports**: 1, 10, 100, 1000, 10000, 1080, 11, 12, 120, 13, 14, 15, 16, 17, 19, 1920, 2, 2000, 23, 24, 25, 250, 3, 30, 300, 33, 337, 3500, 4, 40, 4000, 450, 47, 5, 50, 500, 55, 554, 59, 6, 60, 600, 690, 7, 70, 8, 80, 8191, 9

## File: bin/rm
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/favicon.ico
**Ports**: 1, 111, 5, 542, 9, 999

## File: etc/init.d/S81toe
**Ports**: 100, 200, 8192

## File: sbin/ifconfig
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libhive_RES.so
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 2, 208, 23, 24, 26, 27, 28, 3, 30, 37, 4, 40, 43, 45, 46, 48, 49, 5, 50, 51, 55, 56, 57, 6, 62, 66, 67, 68, 69, 7, 73, 74, 75, 76, 77, 78, 79, 8, 80, 84, 85, 9, 92, 93, 94, 95

## File: web/js/wificfg.js
**Ports**: 1, 100, 2, 20, 200, 255, 3, 4, 40, 5, 60, 80
### Encryption/Encoding: AES

## File: bin/echo
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/ip
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/serialconfig.htm
**Ports**: 1, 1200, 19200, 2, 2400, 38400, 4800, 5, 57600, 6, 7, 8, 9600

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_vgs.ko
**Ports**: 1, 10, 100, 101, 11, 12, 128, 1280, 13, 14, 1404, 18, 180, 19, 2, 20, 200, 2017, 2048, 22, 24, 24242, 255, 270, 3, 30, 32, 33, 34, 3840, 4, 40, 400, 40646, 4080, 4096, 41, 42, 420, 43, 44, 444, 45, 47, 480, 5, 50, 55, 6, 60, 61, 66, 7, 77, 771, 8, 80, 800, 81, 82, 83, 84, 843, 844, 85, 855, 858, 86, 88, 884, 886, 89, 9, 90, 91, 92, 99

## File: usr/bin/lua/ptz/Videon_D.lua
**Ports**: 1, 10, 11, 12, 127, 128, 13, 14, 2, 200, 256, 3, 4, 40, 5, 6, 7, 8192, 9

## File: web/js/publicFunc.js
**Ports**: 1, 10, 100, 10001, 102, 1024, 10240, 1050, 1080, 11, 110, 12, 120, 1200, 1216, 12288, 123, 128, 1280, 13, 1366, 14, 140, 1400, 1408, 14336, 144, 1440, 149, 15, 150, 1536, 16, 160, 1600, 16384, 17, 176, 1792, 18, 18432, 1872, 19, 190, 1900, 192, 1920, 198, 1980, 2, 20, 200, 2037, 2048, 20480, 21, 215, 2160, 22, 223, 224, 22528, 23, 24, 240, 24576, 2472, 25, 255, 256, 2560, 26, 27, 28, 288, 29, 3, 30, 300, 31, 32, 320, 321, 325, 3296, 330, 337, 34, 352, 360, 3600, 37, 3744, 37810, 38, 3800, 384, 3840, 39, 39999, 4, 40, 400, 401, 408, 4096, 448, 450, 48, 480, 5, 50, 500, 5050, 512, 54, 576, 59, 592, 6, 60, 600, 601, 6144, 64, 640, 65, 65535, 68, 69, 7, 70, 704, 720, 768, 8, 80, 800, 8192, 85, 854, 896, 9, 90, 96, 960, 9999

## File: usr/bin/lua/ptz/WV-CS850I.lua
**Ports**: 1, 10, 100, 16, 1610, 18, 2, 200, 23, 24, 3, 4, 5, 6, 7, 8, 88, 9, 96, 99

## File: bin/sync
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: sbin/makedevs
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoP-SD.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 4, 5, 6, 7, 8

## File: lib/libutil-0.9.33.2.so
**Ports**: 1, 10, 2, 4, 5, 7, 8
### Vulnerabilities:
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.

## File: etc/udev/rules.d/99-fuse.rules
**Ports**: 666

## File: etc/init.d/rcS
**Ports**: 9

## File: usr/bin/lua/ptz/DH-CC440.lua
**Ports**: 1, 16, 1610, 200, 4, 5, 8, 9

## File: usr/bin/lua/ptz/PIH-717.lua
**Ports**: 1, 2, 200, 3, 7, 717

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_tde.ko
**Ports**: 1, 10, 11, 13, 133, 15, 18, 19, 2, 2017, 248, 256, 280, 3, 30, 31, 315, 4, 40, 400, 408, 43, 44, 48, 5, 50, 54, 58, 5804, 6, 7, 77, 8, 80, 800, 84, 840, 87, 88, 884, 89, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/bin/lua/ptz/General.lua
**Ports**: 1, 100, 16, 1610, 2, 200, 256, 3, 32, 4, 5, 6, 7

## File: web/js/localconfig.js
**Ports**: 1, 10, 100, 11, 12, 120, 13, 14, 15, 150, 16, 168, 17, 18, 19, 1900, 2, 20, 2037, 2038, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 300, 31, 32, 33, 337, 350, 3600, 37, 39, 4, 400, 5, 59, 6, 60, 64, 65535, 7, 8, 9, 998, 999

## File: usr/sbin/.dec.sh
**Ports**: 1, 2, 8

## File: web/html/iscsiconfig.htm
**Ports**: 3, 3260, 65535
### Vulnerabilities:
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.

## File: web/css/infoindex.css
**Ports**: 100, 10001, 50, 8, 80

## File: usr/bin/lua/ptz/DH-MATRIX.lua
**Ports**: 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_jpegd.ko
**Ports**: 1, 10, 13, 18, 19, 2, 2017, 3, 4, 5, 6, 7, 8, 9

## File: web/js/IVSFaceSearch.js
**Ports**: 1, 100, 12, 1969, 2, 2049, 23, 31, 3600, 40, 59, 60, 8

## File: bin/free
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/data/Data/FontSmallEn.bin
**Ports**: 2, 4, 8

## File: bin/chmod
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/libdl.so.0
**Ports**: 1, 2, 3, 4, 40, 44, 5, 6, 7, 8, 80, 81
### Encryption/Encoding: TLS

## File: bin/vlock
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/ash
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/touch
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/AD1641M.lua
**Ports**: 1, 10, 11, 12, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: web/js/alarmcenter.js
**Ports**: 1, 12, 2, 24, 255, 3, 4, 5, 6, 65535, 7, 8

## File: bin/tar
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/css/Intellent.css
**Ports**: 1, 100, 2, 2014, 210, 29, 3, 444, 50, 6, 60, 8, 999

## File: web/html/usermanage.htm
**Ports**: 1, 11, 2, 3, 63

## File: bin/hush
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/msh
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/qrcode.js
**Ports**: 1, 10, 100, 101, 102, 104, 106, 107, 108, 109, 11, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 12, 120, 121, 122, 123, 126, 128, 13, 130, 132, 133, 1335, 134, 135, 136, 138, 139, 14, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 15, 150, 151, 152, 153, 154, 158, 16, 162, 166, 17, 170, 18, 19, 2, 20, 21, 21522, 22, 23, 236, 24, 25, 255, 256, 26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 4095, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 7, 70, 71, 72, 73, 74, 75, 76, 78, 7973, 8, 80, 81, 82, 84, 86, 87, 88, 9, 90, 92, 93, 94, 97, 98, 99

## File: bin/netstat
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/system.js
**Ports**: 1, 2, 6, 9

## File: web/js/faceplayback.js
**Ports**: 1, 10, 100, 12, 120, 150, 16, 2, 20, 200, 210, 23, 230, 3, 35, 350, 4, 5, 50, 500, 59, 6, 655, 7, 8, 83, 9

## File: web/js/broadcast.js
**Ports**: 1, 1025, 2, 224, 239, 3, 36666

## File: web/html/recordcontrol.htm
**Ports**: 1

## File: web/js/3gnetcfg.js
**Ports**: 1, 12, 16, 2, 31, 32, 5, 65535, 777, 98, 99

## File: tmp/daemon1
**Ports**: 1, 168, 192, 2, 22, 25, 3

## File: usr/data/Data/cursors/wait.cur
**Ports**: 8

## File: web/html/alarmcenter.htm
**Ports**: 1, 65535

## File: web/html/remotestorage.htm
**Ports**: 1, 2, 31, 32, 65535

## File: bin/login
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/autoregister.htm
**Ports**: 1, 31, 65535

## File: usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_vicap.sh
**Ports**: 1, 10, 32

## File: bin/[
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: bin/cttyhack
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/useronvif.js
**Ports**: 1, 17, 2, 30

## File: bin/top
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/PelcoP1.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: usr/bin/lua/ptz/ADMatrix.lua
**Ports**: 1, 10, 13, 16, 1610, 2, 2006, 256, 3, 4, 5, 6, 66, 7

## File: lib/libpthread-0.9.33.2.so
**Ports**: 1, 2, 20, 2006, 22, 3, 30, 33, 4, 40, 404, 414, 42, 44, 47, 5, 6, 7, 8, 80, 81, 9
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: web/pluginVersion.js
**Ports**: 1, 3

## File: lib/ld-uClibc-0.9.33.2.so
**Ports**: 1, 12, 13, 2, 21, 3, 4, 40, 44, 5, 6, 7, 8, 80, 800, 81, 88, 9
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: TLS

## File: web/jsBase/lib/more.js
**Ports**: 1, 100, 16, 2, 20, 25, 250, 255, 3, 360, 4, 4096, 5, 50, 6, 60
### Encryption/Encoding: Hex

## File: linuxrc
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/CP-CVI.lua
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: sbin/dvrhelper
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/sbin/3gpp
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/html/setindex.htm
**Ports**: 1, 1999, 2, 6, 7, 8
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: web/js/onlineuser.js
**Ports**: 1, 2

## File: web/html/emailconfig.htm
**Ports**: 1, 1440, 2, 3, 30, 3600, 65535
### Encryption/Encoding: SSL, TLS

## File: sbin/route
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/GroupControl.js
**Ports**: 1, 15, 16, 2, 3, 4, 5, 6, 7, 8, 9

## File: web/js/emailconfig.js
**Ports**: 1, 100, 120, 1440, 16, 18, 2, 20, 3, 30, 31, 360, 3600, 4, 40, 5, 60, 63, 65535

## File: web/html/wificfg.htm
**Ports**: 1, 128, 2, 3, 4

## File: usr/bin/lua/ptz/CATU.lua
**Ports**: 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: usr/bin/lua/ptz/EPTZ.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 80, 9

## File: sbin/pppd
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/version.js
**Ports**: 1, 100, 2, 3, 4, 5, 500, 6, 7, 9

## File: web/html/videomatrix.htm
**Ports**: 1, 10, 100, 11, 12, 120, 13, 14, 15, 16, 2, 3, 4, 5, 6, 7, 8, 9

## File: web/html/faceplayback.htm
**Ports**: 1, 10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1999, 2, 20, 2012, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 4, 6, 7, 8, 9

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_aio.ko
**Ports**: 1, 10, 16, 2, 20, 3, 38, 4, 41, 42, 44, 46, 47, 48, 5, 6, 61, 7, 8, 83, 84, 85, 87, 88, 9

## File: usr/bin/DahuaExec
**Ports**: 1, 15, 2, 3, 4, 5, 6, 8, 80
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.

## File: usr/bin/lua/ptz/Videon_P.lua
**Ports**: 1, 2, 200, 256, 4, 5, 6, 7, 8

## File: web/css/playbackindex.css
**Ports**: 10, 100, 1000, 10000, 11, 2000, 444, 555, 900, 998, 999, 9995, 9999

## File: sbin/net3g
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: usr/bin/lua/ptz/QT-2XXD.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7

## File: web/js/videomatrix.js
**Ports**: 1, 100, 1024, 12, 120, 150, 16, 2, 20, 200, 25, 3, 300, 32, 350, 36, 4, 5, 6, 8, 9

## File: web/js/tcpip_ipc.js
**Ports**: 1, 110, 119, 120, 127, 1280, 15, 1500, 2, 20, 255, 256, 3, 33, 4, 5, 500, 7200

## File: web/js/ptzCtrl.js
**Ports**: 1, 10

## File: lib/libdl-0.9.33.2.so
**Ports**: 1, 2, 3, 4, 40, 44, 5, 6, 7, 8, 80, 81
### Encryption/Encoding: TLS

## File: usr/bin/lua/ptz/PelcoP-HK.lua
**Ports**: 1, 128, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 8192

## File: web/js/ipAccess.js
**Ports**: 1, 190, 2, 200, 64

## File: web/js/loginEx.js
**Ports**: 1, 120, 128, 192, 200, 255, 3, 300, 3600, 4, 60, 63, 8

## File: usr/bin/lua/ptz/PelcoASCII.lua
**Ports**: 1, 10, 2, 200, 256, 3, 4, 5, 6, 63, 64, 99, 9999

## File: usr/lib/lib.7z.extracted/0/lib/i2c_common.ko
**Ports**: 1, 10, 12696, 2, 2016, 3, 4, 5, 52, 62, 7, 8, 9
### Vulnerabilities:
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.

## File: usr/bin/lua/ptz/Yaan.lua
**Ports**: 1, 10, 11, 12, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: bin/chat
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/audioset.js
**Ports**: 1, 1024, 1440, 2, 3, 30, 3600, 4, 500, 6, 60

## File: usr/bin/lua/ptz/SIERA-D.lua
**Ports**: 1, 16, 1610, 2, 200, 256, 3, 4, 5, 6, 7, 8, 9

## File: bin/vi
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/adddevice.js
**Ports**: 1, 10, 108, 110, 127, 15, 16, 168, 17, 192, 2, 20, 210, 25001, 255, 256, 275, 3, 31, 32, 37777, 4, 40001, 442, 5, 554, 6, 65535, 7, 8, 80, 9, 9999

## File: bin/awk
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: web/js/findPwd.js
**Ports**: 1, 10, 12, 168, 17, 192, 2, 3, 4, 442, 63, 8

## File: web/html/ptzconfig.htm
**Ports**: 1, 1200, 19200, 2, 2400, 38400, 4800, 5, 57600, 6, 7, 8, 9600

## File: etc/udev/rules.d/device-mapper.rules
**Ports**: 600, 9

## File: web/html/defaultcfg.htm
**Ports**: 1, 2, 3, 4, 5
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.

## File: usr/lib/lib.7z.extracted/0/lib/hi3521a_jpege.ko
**Ports**: 1, 10, 13, 16, 18, 19, 2, 2017, 22, 255, 29, 3, 31, 32, 38, 4, 40, 42, 420, 422, 44, 47, 49, 5, 52, 56, 56789, 6, 64, 7, 78, 8, 80, 81, 84, 86, 8888, 89, 9, 92, 9387
### Encryption/Encoding: DES

## File: web/css/index.css
**Ports**: 100, 1000, 10000, 45, 50, 55, 60, 8, 80

## File: usr/bin/lua/ptz/Mercer.lua
**Ports**: 1, 10, 100, 1000, 16, 1610, 2, 200, 3, 4, 5, 6, 8

## File: usr/data/hardware.lua
**Ports**: 1, 2

## File: bin/dnsdomainname
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: lib/ld-uClibc.so.0
**Ports**: 1, 12, 13, 2, 21, 3, 4, 40, 44, 5, 6, 7, 8, 80, 800, 81, 88, 9
### Vulnerabilities:
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: TLS

## File: web/html/alarmindex.htm
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 1999, 2, 25, 3, 4, 5, 6, 7, 8, 9

## File: usr/data/Data/Font.bin
**Ports**: 1, 10, 11, 113, 2, 3, 30, 33, 4, 5, 6, 7, 8, 80, 83, 88, 9, 90

## File: web/cap.js
**Ports**: 1, 10, 11, 12, 13, 14, 15, 16, 19, 2, 3, 37777, 4, 5, 554, 6, 7, 8, 9

## File: lib/Data_Signature
**Ports**: 60

## File: usr/bin/lua/ptz/SHARP.lua
**Ports**: 10, 200, 4, 5, 6

## File: web/css/alarmindex.css
**Ports**: 100, 30, 65

## File: usr/lib/lib.7z.extracted/0/lib/pinmux_hi3521a_i2s.sh
**Ports**: 1, 10, 32

## File: usr/bin/lua/ATMCtrl.lua
**Ports**: 1, 14, 16, 1992, 2007, 2416, 43, 5

## File: sbin/lsusb
**Ports**: 1, 10, 100, 101, 1024, 106, 107, 108, 109, 11, 1101, 111, 1112, 112, 1190, 12, 120, 12258, 123, 127, 128, 13, 14, 140, 1414, 1492, 15, 1500, 156, 157, 16, 168, 17, 176, 18, 180, 182, 184, 187, 19, 192, 1998, 2, 20, 2000, 2002, 2009, 2010, 2017, 208, 21, 21518, 22, 220, 23, 24, 25, 2500, 2516, 255, 25834, 27, 280, 2822, 3, 30, 3020, 31, 3100, 3133, 32, 32774, 333, 34, 36, 37, 38, 4, 40, 400, 40008, 401, 402, 404, 405, 407, 408, 4080, 409, 41, 410, 411, 414, 42, 43, 434, 44, 440, 45, 450, 451, 46, 47, 48, 480, 490, 5, 50, 500, 5000, 505, 506, 51, 512, 52, 521, 53, 54, 540, 542, 545, 55, 56, 58, 580, 59, 6, 60, 6000, 6020, 62, 64, 6412, 646, 647, 648, 649, 67, 681, 691, 7, 70, 7001, 704, 709, 7095, 71, 72, 73, 74, 76, 77, 777, 78, 8, 80, 800, 801, 802, 803, 804, 808, 81, 810, 818, 82, 820, 821, 822, 828, 829, 83, 838, 84, 840, 85, 86, 87, 88, 89, 9, 90, 91, 93, 936, 94, 940, 95, 960, 97, 98, 99, 999
### Vulnerabilities:
- **system**: Command Injection: Allows attackers to inject arbitrary commands into the system for execution.
- **strcpy**: Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.
- **scanf**: Buffer Overflow: If used improperly, can cause memory corruption or allow code execution.
- **gets**: Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.
- **exec**: Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.
### Encryption/Encoding: Hex, RSA

## File: etc/init.d/S99dh
**Ports**: 1, 10, 168, 192, 200, 240, 255, 5, 5120, 52, 6, 777
