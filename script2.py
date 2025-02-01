import os
import sys
import hashlib
import subprocess
from datetime import datetime
import re
import argparse
from pathlib import Path

# Define well-known paths for startup scripts
startup_paths = [
    '/etc/init.d/',
    '/etc/rc.d/',
    '/etc/rc.local',
    '/sbin/',
    '/bin/'
]

suspicious_keywords = [
    "/bin/sh", "wget", "curl", "chmod", "base64", "bash", "openssl", "exec",
    "CreateProcessA", "InternetOpenURLA", "FindNextFileA", "FindFirstFileA",
    "CopyFileA", "Kernel32.dll", "Invoke-Command",
    "Invoke-MaliciousActivity", "admin", "password",
    "get_smtp", "smtp_login", "apache", "revssh64", "pastebin.com",
    "http://", "https://"
]

vulnerability_patterns = {
        "strcpy": "Buffer Overflow: Can overwrite memory if the source string is larger than the destination buffer.",
        "gets": "Buffer Overflow: Doesn't check input size, leading to memory corruption or code execution.",
        "system": "Command Injection: Allows attackers to inject arbitrary commands into the system for execution.",
        "exec": "Arbitrary Code Execution: Executes commands passed to it, potentially allowing remote code execution.",
        "scanf": "Buffer Overflow: If used improperly, can cause memory corruption or allow code execution."
    }


def check_sasquatch():
    try:
        # Run the 'sasquatch' command with '-v' to check if it is installed
        result = subprocess.run(['sasquatch', '-v'], 
                                capture_output=True,  # Capture stdout and stderr
                                text=True,            # Decode output as text
                                timeout=5)            # Set a timeout for the command
        return True  # If the command executes successfully, Sasquatch is installed
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False  # If an error occurs, Sasquatch is not installed
    
    
# Function to check if a tool is installed
def check_tool(tool_name):
    return subprocess.call(["which", tool_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

# Function to install a missing tool (Linux only)
def install_tool(tool_name):
    print(f"Installing {tool_name}...")
    subprocess.call(["sudo", "apt", "install", "-y", tool_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Function to install Python packages
def install_python_packages():
    python_packages = ["binwalk"]  # Add more Python dependencies if needed
    subprocess.call(["pip", "install"] + python_packages, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Python dependencies installed successfully.")

# Function to install Sasquatch
def install_sasquatch():
    if not check_sasquatch():
        print("Sasquatch is not installed. Installing it now...")
        subprocess.call(["sudo", "apt", "install", "-y", "zlib1g-dev", "liblzma-dev", "liblzo2-dev"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(["git", "clone", "https://github.com/devttys0/sasquatch"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(["bash", "-c", "cd sasquatch && ./build.sh"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(["wget", "https://raw.githubusercontent.com/devttys0/sasquatch/82da12efe97a37ddcd33dba53933bc96db4d7c69/patches/patch0.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(["bash", "-c", "mv patch0.txt sasquatch/patches/"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(["bash", "-c", "cd sasquatch && ./build.sh"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Sasquatch installed successfully.") 
    else:
        print("Sasquatch is already installed.")

# Consolidated function to check and install all dependencies
def ensure_and_install_dependencies():
    
    required_tools = ["file", "strings", "binwalk", "ent", "readelf", "grep"]
    for tool in required_tools:
        if not check_tool(tool):
            print(f"{tool} is not installed. Installing it now...")
            install_tool(tool)

    install_python_packages()
    install_sasquatch()




def extract_firmware(firmware_path, extract_dir):
    """Extract the firmware binary using binwalk."""
    try:
        print(f"Extracting firmware: {firmware_path}")
        subprocess.run(
            ["binwalk", "--extract", "--directory", extract_dir, firmware_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"Extraction completed. Filesystem extracted to: {extract_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to extract firmware. {e}")
        sys.exit(1)

def find_root_directory(extract_dir):
    """Find the root directory of the extracted filesystem."""
    for root, dirs, files in os.walk(extract_dir):
        if "etc" in dirs and "bin" in dirs:  # Check for common root filesystem structure
            return root
    print("Error: Could not locate root directory of extracted filesystem.")
    sys.exit(1)

def find_startup_scripts(root_directory):
    """Find startup scripts in well-known paths."""
    found_scripts = []
    for path in startup_paths:
        full_path = os.path.join(root_directory, path.lstrip('/'))  # Ensure proper path joining
        if os.path.exists(full_path):
            if os.path.isdir(full_path):  # If it's a directory, check its contents
                for entry in os.listdir(full_path):
                    entry_path = os.path.join(full_path, entry)
                    if os.path.isfile(entry_path) and (entry.startswith('init') or entry.startswith('rc') or entry.endswith('.sh')):
                        found_scripts.append(entry_path)
            elif os.path.isfile(full_path):  # If it's a file, add it directly
                found_scripts.append(full_path)
    return found_scripts

def get_file_info(file_path, root_directory):
    """Extract detailed information about a file."""
    file_info = {}

    # Resolve symbolic links
    if os.path.islink(file_path):
        try:
            real_path = os.path.realpath(file_path)
            file_info['Resolved_path'] = os.path.relpath(real_path, root_directory)  # Relative to root
            file_path = real_path  # Update to analyze the resolved path
        except Exception as e:
            file_info['Resolved_path'] = f"Error resolving symlink: {e}"

    # Get directory name and file name (relative to root)
    file_info['Directory_name'] = os.path.relpath(os.path.dirname(file_path), root_directory)
    file_info['file_name'] = os.path.basename(file_path)

    # Get file type using the 'file' command
    try:
        file_type_output = subprocess.check_output(['file', file_path], universal_newlines=True)
        file_info['file_type'] = file_type_output.split(':', 1)[1].strip()
    except Exception as e:
        file_info['file_type'] = f"Error determining file type: {e}"

    # Calculate MD5 hash
    try:
        with open(file_path, 'rb') as f:
            md5_hash = hashlib.md5()
            while chunk := f.read(8192):
                md5_hash.update(chunk)
            file_info['MD5_hash'] = md5_hash.hexdigest()
    except Exception as e:
        file_info['MD5_hash'] = f"Error calculating MD5 hash: {e}"

    # Get file size
    try:
        file_info['File_size'] = os.path.getsize(file_path)
    except Exception as e:
        file_info['File_size'] = f"Error getting file size: {e}"

    # Get architecture (if applicable)
    try:
        if 'ELF' in file_info['file_type']:
            arch_output = subprocess.check_output(['readelf', '-h', file_path], universal_newlines=True)
            for line in arch_output.splitlines():
                if 'Machine:' in line:
                    file_info['Architecture'] = line.split(':', 1)[1].strip()
                    break
        else:
            file_info['Architecture'] = 'Not applicable'
    except Exception as e:
        file_info['Architecture'] = f"Error determining architecture: {e}"

    return file_info

def write_file_info_to_markdown(file_info, output_file):
    """Write detailed information about a startup script to a Markdown-formatted output."""
    current_date = datetime.now().strftime("%A, %B %d, %Y, %-I %p %Z")
    
    with open(output_file, 'a') as f:
        f.write(f"### Startup Script: `/{os.path.join(file_info['Directory_name'], file_info['file_name'])}`\n\n")
        f.write(f"- **Directory Name**: `/{file_info['Directory_name']}`\n")
        f.write(f"- **File Name**: `{file_info['file_name']}`\n")
        f.write(f"- **File Type**: `{file_info['file_type']}`\n")
        f.write(f"- **MD5 Hash**: `{file_info['MD5_hash']}`\n")
        f.write(f"- **File Size**: `{file_info['File_size']} bytes`\n")
        f.write(f"- **Architecture**: `{file_info['Architecture']}`\n")
        f.write(f"- **Current Date**: `{current_date}`\n")
        f.write("\n---\n\n")








def extract_strings(file_path, min_length=4):
    """
    Extract readable strings from a binary file using the 'strings' command.
    """
    try:
        # Run the 'strings' command with a minimum string length filter
        result = subprocess.check_output(['strings', '-n', str(min_length), file_path], universal_newlines=True)
        return result.splitlines()
    except Exception as e:
        print(f"Error extracting strings from {file_path}: {e}")
        return []

def search_suspicious_strings(strings_list, keywords):
    """
    Search for suspicious keywords in the extracted strings.
    """
    matches = set()  # Use a set to ensure no duplicates
    for line in strings_list:
        for keyword in keywords:
            if keyword in line:
                matches.add(keyword)  # Add only unique keywords
    return matches

def scan_directory(root_directory, keywords, min_length=4):
    """
    Recursively scan all files in a directory for suspicious strings.
    """
    all_results = {}
    for root, _, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Extract strings from the file
            extracted_strings = extract_strings(file_path, min_length=min_length)
            # Search for suspicious keywords
            matches = search_suspicious_strings(extracted_strings, keywords)
            if matches:
                # Store results with relative paths
                relative_path = os.path.relpath(file_path, root_directory)
                all_results[relative_path] = matches
    return all_results

def display_results(scan_results):
    """
    Write the results to a Markdown file with a summary and a master dropdown.
    """
    with open(output_file, "a") as file:
        # Write the summary at the top
        if not scan_results:
            file.write("No suspicious strings detected.\n")
            return

        total_files = len(scan_results)
        total_keywords = sum(len(detections) for detections in scan_results.values())
        file.write(f"# Scan Summary\n\n")
        file.write(f"- **Total Files Scanned:** {total_files}\n")
        file.write(f"- **Total Suspicious Keywords Detected:** {total_keywords}\n\n")

        # Master dropdown for all results
        file.write("<details>\n")
        file.write("<summary>Click to view detailed results</summary>\n\n")

        # Write detailed results inside the dropdown
        for relative_path, detections in scan_results.items():
            file.write(f"### File: `{relative_path}`\n\n")
            file.write("| Keyword        |\n")
            file.write("|----------------|\n")
            for keyword in detections:
                file.write(f"| `{keyword}`     |\n")
            file.write("\n")

        file.write("</details>\n\n")





def validate_ip(ip):
    """Validate if a string is a valid IP address."""
    ip_pattern = re.compile(r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')
    return bool(ip_pattern.fullmatch(ip))

def search_ports_and_ips(root_directory):
    """Search for valid port numbers and IP addresses in the file structure."""
    findings = {}
    
    # Updated regex patterns
    ip_port_pattern = re.compile(
        r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
        r':(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|'
        r'[1-5]?[0-9]{1,4})\b'
    )
    
    keyword_port_pattern = re.compile(
        r'\b(?:port|bind|listen)\s*[:=]?\s*'
        r'(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|'
        r'[1-5]?[0-9]{1,4})\b',
        re.IGNORECASE
    )
    
    for root, _, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip non-text files
            if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.svg')):
                continue

            try:
                with open(file_path, "r", errors="ignore") as f:
                    content = f.read()
                    
                    # Extract matches
                    ip_ports = ip_port_pattern.findall(content)
                    keyword_ports = keyword_port_pattern.findall(content)

                    # Process findings
                    valid_ports = {match[-1] for match in ip_ports}  # Extract port from IP:PORT matches
                    valid_ports.update(keyword_ports)                # Add ports from keyword matches

                    if valid_ports:
                        rel_path = os.path.relpath(file_path, root_directory)
                        findings.setdefault(rel_path, {"ports": [], "ips": []})
                        findings[rel_path]["ports"] = sorted(map(int, valid_ports))  # Convert to integers

            except (UnicodeDecodeError, PermissionError):
                pass

    return findings

def search_vulnerabilities(root_directory):
    """Search for vulnerable functions or patterns in binary files."""
    findings = {}
    

    for root, _, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Skip image files
            if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.svg')): 
                continue

            try:
                result = subprocess.run(["strings", file_path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
                content = result.stdout
                rel_path = os.path.relpath(file_path, root_directory)
                for vuln, description in vulnerability_patterns.items():
                    if vuln in content:
                        if rel_path not in findings:
                            findings[rel_path] = set()
                        findings[rel_path].add(f"{vuln}: {description}")
            except Exception:
                pass

    return findings


def search_encryption(root_directory):
    """Search for encryption or encoding methods."""
    findings = {}
    encryption_keywords = ["AES", "DES", "RSA", "Base64", "SSL", "TLS", "Hex"]

    for root, _, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Skip image files
            if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.svg')):
                continue

            try:
                result = subprocess.run(["strings", file_path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
                content = result.stdout
                rel_path = os.path.relpath(file_path, root_directory)
                for keyword in encryption_keywords:
                    if keyword in content:
                        if rel_path not in findings:
                            findings[rel_path] = set()
                        findings[rel_path].add(keyword)
            except Exception:
                pass

    return findings
# Function to clean port numbers
def clean_ports(ports):
    """Clean and validate port numbers."""
    cleaned_ports = sorted(set(
        str(int(port)) for port in ports 
        if (isinstance(port, str) and port.isdigit() and 1 <= int(port) <= 65535) or 
           (isinstance(port, int) and 1 <= port <= 65535)
    ))
    return cleaned_ports

# Function to clean IP addresses and remove duplicates
def clean_ips(ips):
    # Remove IPs with non-standard characters or invalid format, and eliminate duplicates
    cleaned_ips = sorted(set(ip for ip in ips if re.match(r'^\d+\.\d+\.\d+\.\d+$', ip)))
    return cleaned_ips
    


if __name__ == "__main__":
    print(r"""
 _     _                                                _           _     
| |   (_)                                              | |         (_)    
| |__  _ _ __   __ _ _ __ _   _ ______ __ _ _ __   __ _| |_   _ ___ _ ___ 
| '_ \| | '_ \ / _` | '__| | | |______/ _` | '_ \ / _` | | | | / __| / __|
| |_) | | | | | (_| | |  | |_| |     | (_| | | | | (_| | | |_| \__ \ \__ \
|_.__/|_|_| |_|\__,_|_|   \__, |      \__,_|_| |_|\__,_|_|\__, |___/_|___/
                           __/ |                           __/ |          
                          |___/                           |___/           
          """)
    if len(sys.argv) != 3:
        print('Usage: python binary_analysis.py <firmware_binary> <output_file>')
        sys.exit(1)

    firmware_binary = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(firmware_binary):
        print(f"Error: The firmware binary '{firmware_binary}' does not exist.")
        sys.exit(1)

    extract_dir = "custom_extracted"
    print("Checking and installing all dependencies...")
    ensure_and_install_dependencies()
    print("All dependencies are installed successfully.")
    # Step 1: Extract the firmware binary
    extract_firmware(firmware_binary, extract_dir)

    # Step 2: Locate the root directory of the extracted filesystem
    root_directory = find_root_directory(extract_dir)

    # Step 3: Clear or create the output Markdown file
    with open(output_file, 'w') as f:
        f.write("# Firmware Analysis Results\n\n")

    # Step 4: Find startup scripts and analyze them
    scripts = find_startup_scripts(root_directory)

    if scripts:
        with open(output_file, 'a') as f:
            f.write("## Found Startup Scripts:\n\n")
            for script in scripts:
                relative_script = os.path.relpath(script, root_directory)
                f.write(f"- `/{relative_script}`\n")

            f.write("\n## Analysis of Startup Scripts:\n\n")

        for script in scripts:
            info = get_file_info(script, root_directory)
            write_file_info_to_markdown(info, output_file)
    
    else:
        with open(output_file, 'a') as f:
            f.write("No startup scripts found.\n")
    
    
    
    
    
    print(f"Scanning directory '{root_directory}' for suspicious strings...")

    # Perform the scan
    results = scan_directory(root_directory, suspicious_keywords)

    # Display the results
    display_results(results)

    
    
    
    port_ip_findings = search_ports_and_ips(root_directory)
    vulnerability_findings = search_vulnerabilities(root_directory)
    encryption_findings = search_encryption(root_directory)

    print("[INFO] Saving findings...")
    with open(output_file, 'a') as f:
        # Prepare a list of all files from the three findings
        all_files = set(port_ip_findings.keys()) | set(vulnerability_findings.keys()) | set(encryption_findings.keys())

        # Write the summary at the top
        f.write("# Vulnerability Report\n\n")
        f.write(f"- **Total Files Analyzed:** {len(all_files)}\n")
        f.write(f"- **Files with Port/IP Findings:** {len(port_ip_findings)}\n")
        f.write(f"- **Files with Vulnerabilities:** {len(vulnerability_findings)}\n")
        f.write(f"- **Files with Encryption/Encoding Findings:** {len(encryption_findings)}\n\n")

        # Master dropdown for all detailed findings
        f.write("<details>\n")
        f.write("<summary>Click to view detailed findings</summary>\n\n")

        # Write detailed findings inside the dropdown
        for file in all_files:
            f.write(f"## File: `{file}`\n\n")

            # Port and IP findings
            if file in port_ip_findings:
                data = port_ip_findings[file]
                # Clean ports and IPs, removing duplicates
                cleaned_ports = clean_ports(data["ports"])
                cleaned_ips = clean_ips(data["ips"])

                if cleaned_ports:
                    f.write(f"**Ports**: {', '.join(cleaned_ports)}\n\n")
                if cleaned_ips:
                    f.write(f"**IPs**: {', '.join(cleaned_ips)}\n\n")

            # Vulnerability findings
            if file in vulnerability_findings:
                vulnerabilities = vulnerability_findings[file]
                f.write(f"### Vulnerabilities:\n")
                
                for vuln in vulnerabilities:
                    # Extract just the vulnerability name (e.g., "strcpy")
                    vuln_name = vuln.split(":")[0].strip()  # Get the part before the first colon
                    
                    # Check if vuln_name exists in the vulnerability_patterns
                    if vuln_name in vulnerability_patterns:
                        # Write only the vulnerability name and its description from the dictionary
                        f.write(f"- **{vuln_name}**: {vulnerability_patterns[vuln_name]}\n")
                    else:
                        f.write(f"- **{vuln_name}**: [Description not available]\n")

            # Encryption and Encoding findings
            if file in encryption_findings:
                encryptions = encryption_findings[file]
                f.write(f"### Encryption/Encoding: {', '.join(sorted(encryptions))}\n\n")

            f.write("\n")  # Separate each file's details

        f.write("</details>\n")

        print(f"[INFO] Findings saved to {output_file}")

