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
root:$1$jSqQv.uP$jgz4lwEx2pnDh4QwXkh06/:0:0:root:/:/bin/sh
 
- The root user password hash is stored in MD5 format (`$1$`), which is considered weak.
- This hash can potentially be cracked using tools like `John the Ripper`.

2. **Backup Password File (`passwd-`)**:
#
    cat /etc/passwd-
 
Output:
root:ab8nBoH3mb8.g:0:0::/root:/bin/sh
 
- This file contains another hash format for the root password.

3. **No Shadow File**:
- The absence of an `/etc/shadow` file indicates that password hashes are stored directly in `passwd`, which is less secure.

---

## **Step 4: Identifying Camera Model**
Using the `file` command, I identified details about the camera model embedded in the firmware:

### **Command Used**:
    file chakravyuh.bin
chakravyuh.bin: u-boot legacy uImage, hi3520Dromfs, Linux/ARM, OS Kernel Image (gzip), 13144064 bytes, Wed Nov 29 14:28:44 2017, Load Address: 0XA0060000, Entry Point: 0XA0DA0000, Header CRC: 0X71FF3C3D, Data CRC: 0X3F9F5075

### **Findings**:
- The firmware references `hi3520Dromfs`, indicating it is based on HiSilicon's Hi3520D chip, commonly used in IP cameras.
- This suggests that the device might be an IP camera or similar hardware.

---

## **Challenges Encountered**
1. **Corrupted SquashFS Filesystem**:
   - The manual extraction of the SquashFS filesystem using `unsquashfs` failed due to corruption, as indicated by errors during decompression.
   
2. **Resolution with Sasquatch**:
   - Successfully overcame this issue by using `sasquatch`, which is designed for non-standard or corrupted SquashFS filesystems.

---

## **Next Steps**
1. Attempt password cracking for hashes found in `/etc/passwd` and `/etc/passwd-`.
2. Analyze startup scripts in `/etc/init.d/` for potential vulnerabilities.
3. Search for SUID/SGID binaries that could allow privilege escalation:
# 
    find / -perm /4000 2>/dev/null
 

---

## **Conclusion**
The analysis so far has successfully extracted the firmware's filesystem and identified areas of interest, such as weak password storage mechanisms and potential hardware details (HiSilicon Hi3520D). Further exploration will focus on uncovering vulnerabilities within the system.
