import base64
import os
import re
import sys
import subprocess
import hashlib
from math import log2
from collections import Counter
from collections import defaultdict
import string

firmware_bin_path = ""
CRYPTO_FUNCTIONS = [
    "AES_encrypt", "AES_decrypt", "AES_set_encrypt_key",
    "RSA_public_encrypt", "RSA_private_decrypt",
    "SHA1_Init", "SHA256_Init", "MD5_Init", "Blowfish_set_key",
    "EVP_EncryptInit", "EVP_DecryptInit", "RAND_bytes"
]

# Define weak cryptographic algorithms (Top 5 priority)
WEAK_ALGORITHMS = ["MD5", "SHA1", "DES", "RC4", "3DES"]

# Define Base64 key pattern (40+ characters)
BASE64_PATTERN = re.compile(r"[A-Za-z0-9+/=]{40,}")

# Define RSA key patterns
RSA_PATTERNS = [
    "-----BEGIN RSA PRIVATE KEY-----",
    "-----BEGIN PRIVATE KEY-----"
]

def scan_strings_for_patterns(rootfs, patterns):
    """Scan files in rootfs for specific string patterns."""
    found_patterns = set()
    
    for root, _, files in os.walk(rootfs):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                result = subprocess.run(["strings", file_path], capture_output=True, text=True)
                if result.returncode == 0:
                    for line in result.stdout.split("\n"):
                        if any(pat in line for pat in patterns):
                            found_patterns.add(line.strip())
            except:
                continue

    return list(found_patterns)

def find_hardcoded_base64_keys(rootfs):
    """Detect and validate Base64-encoded keys."""
    valid_base64_keys = set()
    
    for root, _, files in os.walk(rootfs):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", errors="ignore") as f:
                    for line in f:
                        match = BASE64_PATTERN.match(line.strip())
                        if match:
                            try:
                                decoded = base64.b64decode(match.group(), validate=True)
                                if len(decoded) >= 8:  # Only consider valid key-length data
                                    valid_base64_keys.add(match.group())
                            except:
                                pass
            except:
                continue

    return list(valid_base64_keys)

def find_rsa_keys(rootfs):
    rsa_keys = set()

    for root, _, files in os.walk(rootfs):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", errors="ignore") as f:
                    content = f.read()
                    if any(pattern in content for pattern in RSA_PATTERNS):
                        # Compute the relative path
                        relative_path = os.path.relpath(file_path, rootfs)
                        rsa_keys.add(f"Potential RSA Key in: {relative_path}")
            except:
                continue

    return list(rsa_keys)

def extract_cryptographic_analysis(rootfs):
    """Perform cryptographic analysis on the extracted filesystem."""
    print("[*] Running cryptographic analysis...")
    
    crypto_functions = scan_strings_for_patterns(rootfs, CRYPTO_FUNCTIONS)
    weak_crypto = scan_strings_for_patterns(rootfs, WEAK_ALGORITHMS)[:5]  # Limit to Top 5
    base64_keys = find_hardcoded_base64_keys(rootfs)
    rsa_keys = find_rsa_keys(rootfs)

    report_data = {
        "Cryptographic Functions Found": crypto_functions[:5] if len(crypto_functions) > 5 else crypto_functions,
        "Weak Encryption Detected": weak_crypto,
        "Hardcoded Base64 Keys": base64_keys[:1] if len(base64_keys) > 1 else base64_keys,
        "Potential RSA Private Keys": rsa_keys[:1] if len(rsa_keys) > 1 else rsa_keys,
    }

    return report_data
# Constants
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
        if "squashfs-root" in dirs:
            squashfs_root = os.path.join(root, "squashfs-root")
            etc_path = os.path.join(squashfs_root, "etc")
            
            # Check if /etc directory exists inside squashfs-root
            if os.path.isdir(etc_path):
                return squashfs_root
            
            # Check if squashfs-root is empty
            if not os.listdir(squashfs_root):
                return root
    
    print("Error: Could not locate root directory of extracted filesystem.")
    sys.exit(1)
    


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


# Function to calculate MD5 hash
def calculate_hash(file_path):
    try:
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return f"Error calculating hash: {str(e)}"

# Function to calculate entropy
def calculate_entropy(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        if not data:
            return 0
        byte_frequencies = [data.count(byte) / len(data) for byte in set(data)]
        entropy = -sum(freq * log2(freq) for freq in byte_frequencies)
        return round(entropy, 2)
    except Exception as e:
        return f"Error calculating entropy: {str(e)}"
    
# Function to get file type
def get_file_type(file_path):
    try:
        result = subprocess.check_output(["file", "-b", file_path]).decode("utf-8").strip()
        return result
    except Exception as e:
        return f"Error determining file type: {str(e)}"

# Function to extract strings from binary files
def extract_strings(file_path):
    try:
        result = subprocess.check_output(["strings", file_path]).decode("utf-8").splitlines()
        return result
    except Exception as e:
        return [f"Error extracting strings: {str(e)}"]

# Function to find cryptographic algorithms
# def find_cryptographic_algorithms(file_path):
#     crypto_patterns = [
#         r"AES", r"RSA", r"MD5", r"SHA-1", r"SHA-256", 
#         r"HMAC", r"Blowfish", r"Twofish", r"ChaCha20"
#     ]
#     detected_algorithms = set()
    
#     try:
#         content = "\n".join(extract_strings(file_path))  # Ensure this is returning what you expect
        
#         for pattern in crypto_patterns:
#             if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
#                 detected_algorithms.add(pattern)
#             else:
#                 ...
#     except Exception as e:
#         ...
#     return list(detected_algorithms)
    
    

# Function to find UI resources


def find_ui_resources(base_path):
    """
    Find UI-related files (e.g., .html, .js, .css, images) in the extracted filesystem
    and return a Markdown-formatted string.
    """
    ui_files = defaultdict(lambda: defaultdict(list))
    extensions = [".html", ".js", ".css", ".png", ".jpg", ".svg"]

    try:
        for root, _, files in os.walk(base_path):
            for file in files:
                for ext in extensions:
                    if file.endswith(ext):
                        relative_path = os.path.relpath(os.path.join(root, file), base_path)
                        folder = os.path.dirname(relative_path) or "root"
                        ui_files[ext][folder].append(file)
    except Exception as e:
        return f"Error finding UI resources: {str(e)}"

    return format_ui_resources(ui_files)
def format_ui_resources(ui_files):
    """Convert the UI resource dictionary into a properly formatted Markdown string."""
    md_output = ["# UI Resources\n"]  # Header for Markdown

    for ext, folders in sorted(ui_files.items()):
        md_output.append(f"## {ext}")  # Subheading for each file type
        for folder, files in sorted(folders.items()):
            md_output.append(f"- **{folder}/**")  # Bold folder names
            for file in sorted(files):
                md_output.append(f"  - {file}")  # Proper bullet points
        md_output.append("")  # Blank line for spacing

    return "\n".join(md_output)  # Return as a properly formatted Markdown string


# Function to find potential passwords in a binary file
def find_potential_passwords(directory):
    regex_pattern = r'(?i)(?:passwd|pwd|password|Password)\s*=\s*"?([^"\s]+)"?\s*(?:,|$)'
    passwords_with_paths = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = re.findall(regex_pattern, content)
                    
                    for pwd in matches:
                        relative_path = os.path.relpath(file_path, directory)
                        passwords_with_paths.append((pwd, relative_path))
            
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    # Regex to filter out common placeholders or junk
    valid_pwd_pattern = r'^(?!.*[%\*\{\}\(\)\[\]])([a-zA-Z0-9]{4,12})$'
    
    # Filter out non-sensitive passwords
    sensitive_passwords = [
        (pwd, path) for pwd, path in passwords_with_paths
        if re.match(valid_pwd_pattern, str(pwd)) and pwd not in ['******', '%s', '%d']
    ]
    if os.path.exists(firmware_bin_path):
        try:
            process = subprocess.Popen(["strings", firmware_bin_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                firmware_passwords = re.findall(regex_pattern, stdout)
                
                for pwd in firmware_passwords:
                    passwords_with_paths.append((pwd, firmware_bin_path))
            else:
                print(f"Error running strings on {firmware_bin_path}: {stderr}")

        except Exception as e:
            print(f"Error processing firmware binary: {e}")

    # Regex to filter out common placeholders or junk
    valid_pwd_pattern = r'^(?!.*[%\*\{\}\(\)\[\]])([a-zA-Z0-9]{4,12})$'
    
    # Filter out non-sensitive passwords
    sensitive_passwords = [
        (pwd, path) for pwd, path in passwords_with_paths
        if re.match(valid_pwd_pattern, str(pwd)) and pwd not in ['******', '%s', '%d']
    ]
    
    return sensitive_passwords



# Function to extract metadata
def extract_metadata(file_path):
    metadata = {"Version": "N/A", "Build_date": "N/A", "Developer": "N/A"}
    try:
        strings = "\n".join(extract_strings(file_path))
        version_match = re.search(r"version\s*[0-9.]+|v[0-9.]+", strings, re.IGNORECASE)
        email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", strings)
        metadata["Version"] = version_match.group(0) if version_match else "N/A"
        metadata["Developer"] = email_match.group(0) if email_match else "N/A"
    except Exception as e:
        metadata["Error"] = f"Error extracting metadata: {str(e)}"
    return metadata
# Generate directory tree with file types
def generate_file_structure(base_path, depth=8):
    """Generate a Markdown list representing the directory tree with relative paths."""
    tree_structure = []

    def traverse(path, current_depth):
        if current_depth > depth:
            return
        for entry in sorted(os.listdir(path)):
            full_path = os.path.join(path, entry)
            relative_path = os.path.relpath(full_path, base_path)  # Convert to relative
            if os.path.isdir(full_path):
                tree_structure.append(f"{'  ' * (current_depth - 1)}--- **{relative_path}/**")
                traverse(full_path, current_depth + 1)
            else:
                file_type = get_file_type(full_path)
                tree_structure.append(f"{'  ' * (current_depth - 1)}--- {relative_path} ({file_type})")

    traverse(base_path, 1)
    return "\n".join(tree_structure)
def extract_urls(extracted_folder):
    
    urls_output = subprocess.run(
        ["grep", "-sRIEoh", r'(http|https)://[^/"]+[^/"]', "--exclude-dir=dev", extracted_folder],
        capture_output=True,
        text=True
    )

    # Remove duplicates and filter out invalid URLs
    unique_urls = sorted(set(url.strip() for url in urls_output.stdout.splitlines() if len(url.strip()) > len("http://")))

    return unique_urls    

import subprocess

def extract_ips(extracted_folder):
    ip_output = subprocess.run(
        ["grep", "-sRIEoh", 
         r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', 
         "--exclude-dir=dev", extracted_folder], 
        capture_output=True, text=True
    )

    # Remove duplicates by converting to a set, then back to a sorted list
    unique_ips = sorted(set(ip_output.stdout.splitlines()))

    return unique_ips

# Extract firmware details
def extract_firmware_details():
    
    try:
        # Calculate entropy once to avoid redundant calls
        entropy_value = calculate_entropy(firmware_bin_path)

        # Populate the details dictionary
        details = {
    "File Size": f"{os.path.getsize(firmware_path)} bytes",
    "MD5 Hash": calculate_hash(firmware_path),
    "File Format": get_file_type(firmware_path),
    "Detected URLs": extract_urls(extracted_folder),
    "Detected IP Addresses": extract_ips(extracted_folder),
    "Entropy": entropy_value,
    "Entropy Analysis": "High" if entropy_value > 7.5 else "Low",
    "Metadata": extract_metadata(firmware_path),

    # UI Resources as a proper Markdown dropdown
    "UI Resources": (
        "\n<details>\n"
        "<summary><strong>Click here for list of UI Resources</strong></summary>\n\n"
        f"{find_ui_resources(extracted_folder)}\n\n"
        "\n</details>\n"
    ),

    # "Cryptographic Algorithms": find_cryptographic_algorithms(firmware_path),
}

    except Exception as e:
        # Handle errors gracefully and provide fallback values
        details = {
            "File Size": f"{os.path.getsize(firmware_path)} bytes",
            "MD5 Hash": calculate_hash(firmware_path),
            "File Format": get_file_type(firmware_path),
            "Detected URLs": extract_urls(extracted_folder),
            "Detected IP Addresses": extract_ips(extracted_folder),
            "Entropy": None,
            "Entropy Analysis": f"Error: {str(e)}",
            "Metadata": extract_metadata(firmware_path),
            
            "UI Resources": f"\n<details>\n<summary>UI Resources</summary>\n\n{find_ui_resources(extracted_folder)}\n</details>",
            
            # "Cryptographic Algorithms": find_cryptographic_algorithms(firmware_path),
        }

    try:
        binwalk_output = subprocess.check_output(["binwalk", firmware_path]).decode("utf-8").splitlines()
        for line in binwalk_output:
            if "gzip" in line or "archive" in line:
                details["Packing"] = "Archive Detected"
            if "ARM" in line or "MIPS" in line:
                details["Architecture"] = line.strip()
            if "uImage header" in line:
                match = re.search(r"created: (.+?),", line)
                if match:
                    details["Metadata"]["Build_date"] = match.group(1)
                match = re.search(r"image name: \"(.+?)\"", line)
                if match:
                    details["Metadata"]["Version"] = match.group(1)
    except subprocess.CalledProcessError as e:
        details["Packing"] = f"Error analyzing packing: {str(e)}"
        details["Architecture"] = "Unknown"
    return details

# Function to read and return file content
def read_file(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as f:
            return f.read()
    except Exception:
        return None

# Function to find files with specific extensions
def find_files_by_extension(path, extensions, root_folder):
    """
    Find files with specific extensions and return their paths relative to the root folder.
    """
    files = []
    for root, _, file_names in os.walk(path):
        for file in file_names:
            if file.endswith(extensions):  # Accepting tuple as extensions
                relative_path = os.path.relpath(os.path.join(root, file), root_folder)
                files.append(relative_path)
    return files


# Function to find specific keywords in files
def find_keywords(path, keywords, root_folder):
    """
    Search for specific keywords in files and return their paths relative to the root folder.
    """
    found_keywords = {keyword: [] for keyword in keywords}
    for root, _, file_names in os.walk(path):
        for file in file_names:
            file_path = os.path.join(root, file)
            content = read_file(file_path)
            if content:
                for keyword in keywords:
                    if re.search(r'\b' + re.escape(keyword) + r'\b', content):
                        relative_path = os.path.relpath(file_path, root_folder)
                        found_keywords[keyword].append(relative_path)
    return found_keywords




# Function to search for common web servers in the extracted folder
def find_common_web_servers(extracted_folder, root_folder):
    """
    Search for common web servers and return their paths relative to the root folder.
    """
    web_servers_found = set()
    webserver_keywords = ["nginx", "apache", "lighttpd", "httpd", "uhttpd", "busybox-httpd", "alphapd"]

    for root, _, file_names in os.walk(extracted_folder):
        for file in file_names:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    content = f.read()
                    for keyword in webserver_keywords:
                        if keyword.lower() in content.lower():
                            relative_path = os.path.relpath(file_path, root_folder)
                            web_servers_found.add(relative_path)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue

    return sorted(list(web_servers_found))

    
# Function to find common binaries
def find_common_binaries(path, root_folder):
    """
    Find common binaries and return their paths relative to the root folder.
    """
    common_binaries = ["busybox", "wget", "curl", "telnet", "nc", "openssl", "httpd", "nginx", "ssh", "lighttpd"]
    found_binaries = []
    for root, _, files in os.walk(path):
        for file in files:
            if any(binary in file for binary in common_binaries):
                relative_path = os.path.relpath(os.path.join(root, file), root_folder)
                found_binaries.append(relative_path)
    return found_binaries
    
    
def find_etc_ssl_files(extracted_folder):
    ssl_directory = os.path.join(extracted_folder, "etc", "ssl")
    ssl_files = []
    if os.path.exists(ssl_directory):
        for root, dirs, files in os.walk(ssl_directory):
            for file in files:
                ssl_files.append(os.path.relpath(os.path.join(root, file), extracted_folder))
    return ssl_files
    
    
# Extract security-related information
def extract_security_details(extracted_folder):
    """
    Extract security-related details from the extracted filesystem.
    """
    security_report = {
        "etc/shadow and etc/passwd files": [],
        "etc/ssl directory files": [],
        "SSL related files": [],
        "Configuration files": [],
        "Script files": [],
        "Other .bin files": [],
        "Keywords found": {},
        "Common web servers used on IoT devices": [],
        "Common binaries": [],
        "URLs, email addresses, and IP addresses found": {
            "URLs": [],
            "Emails": [],
            "IP Addresses": []
        },
    }

    # Sensitive files
    sensitive_files = ["etc/shadow", "etc/passwd", "etc/shadow-", "etc/passwd-"]
    for sensitive_file in sensitive_files:
        file_path = os.path.join(extracted_folder, sensitive_file)
        if os.path.exists(file_path):
            relative_path = os.path.relpath(file_path, extracted_folder)
            
            # Append the file path to the report
            security_report["etc/shadow and etc/passwd files"].append(relative_path)

            # Read the content of the file and append it below the file path
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    file_content = f.read()
                    # Append the content of the file to the report
                    security_report["etc/shadow and etc/passwd files"].append(f"Content of {relative_path}:\n{file_content}")
            except Exception as e:
                # Handle error in case the file cannot be read
                security_report["etc/shadow and etc/passwd files"].append(f"Error reading {relative_path}: {str(e)}")

            
    # Add handling of empty `etc/ssl` directory files to the security report
    ssl_directory_files = find_etc_ssl_files(extracted_folder)
    if ssl_directory_files:
        security_report["etc/ssl directory files"].extend(ssl_directory_files)
    else:
        security_report["etc/ssl directory files"] = ["No files found in /etc/ssl directory"]

    
    
        

    # SSL-related files
    ssl_files = find_files_by_extension(extracted_folder, (".pem", ".crt", ".key"), extracted_folder)
    security_report["SSL related files"].extend(ssl_files)

    # Configuration files
    config_files = find_files_by_extension(extracted_folder, (".conf", ".cfg", ".xml", ".json", ".ini", ".yml", ".yaml"), extracted_folder)
    security_report["Configuration files"].extend(config_files)

    # Script files
    script_files = find_files_by_extension(extracted_folder, (".sh", ".py", ".bash"), extracted_folder)
    security_report["Script files"].extend(script_files)

    # Other .bin files
    bin_files = find_files_by_extension(extracted_folder, (".bin", ".img", ".fw"), extracted_folder)
    security_report["Other .bin files"].extend(bin_files)

    # Keywords
    keywords = ["password", "admin", "root", "123456"]
    security_report["Keywords found"] = find_keywords(extracted_folder, keywords, extracted_folder)

    # Web servers
    web_servers_found = find_common_web_servers(extracted_folder, extracted_folder)
    security_report["Common web servers used on IoT devices"].extend(web_servers_found)

    # Common binaries
    common_binaries = find_common_binaries(extracted_folder, extracted_folder)
    security_report["Common binaries"].extend(common_binaries)

    # URLs, emails, and IPs
    urls_output = subprocess.run(
    ["grep", "-sRIEoh", r'(http|https)://[^/"]+[^/"]', "--exclude-dir=dev", extracted_folder],
    capture_output=True,
    text=True
    )

    # Remove duplicates and filter out invalid URLs
    unique_urls = sorted(set(url.strip() for url in urls_output.stdout.splitlines() if len(url.strip()) > len("http://")))

    security_report["URLs, email addresses, and IP addresses found"]["URLs"] = unique_urls

    
    
    email_output = subprocess.run(["grep", "-sRIEoh", r'([[:alnum:]_.-]+@[[:alnum:]_.-]+?\.[[:alpha:].]{2,6})', "--exclude-dir=dev", extracted_folder], capture_output=True, text=True)
    unique_emails = sorted(set(email_output.stdout.splitlines()))
    security_report["URLs, email addresses, and IP addresses found"]["Emails"] = unique_emails  

    ip_output = subprocess.run(
    ["grep", "-sRIEoh", 
     r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', 
     "--exclude-dir=dev", extracted_folder], 
    capture_output=True, text=True
    )
    # Remove duplicates by converting to a set, then back to a sorted list
    unique_ips = sorted(set(ip_output.stdout.splitlines()))

    security_report["URLs, email addresses, and IP addresses found"]["IP Addresses"] = unique_ips
    return security_report
# Main function to generate the report
def generate_report():
     
    


    # Open the report file to write
    with open(report_file, "w") as report:
        # A. File Structure
        report.write("# Directory Tree Structure\n\n")
        report.write("<details>\n")
        report.write("<summary><strong>📁 Click to expand directory structure</strong></summary>\n\n")
        print("ANALYSING FILE STRUCTURE")
        
        report.write("```")
        report.write(generate_file_structure(extracted_folder))
        report.write("\n```\n\n")  # End code block
        report.write("</details>\n\n<br>\n")
        print("ANALYSING FILE STRUCTURE COMPLETED")
        
        # B. Firmware Details
        print("ANALYSING FIRMWARE DETAILS")
        report.write("\n# Firmware Details\n\n")
        firmware_details = extract_firmware_details()
        for key, value in firmware_details.items():
            if isinstance(value, dict):
                report.write(f"## {key}\n")
                for sub_key, sub_value in value.items():
                    report.write(f"- **{sub_key}**: {sub_value}\n")
                report.write("\n")
            else:
                report.write(f"- **{key}**: {value}\n")
                
        print("RUNNING CRYPTOGRAPHIC ANALYSIS")
        report.write("## Cryptographic Analysis\n\n")
        crypto_results = extract_cryptographic_analysis(extracted_folder)
        
        report.write("\n- Found Cryptographic Functions:\n")
        if crypto_results["Cryptographic Functions Found"]:
            report.write(f"  * {', '.join(crypto_results['Cryptographic Functions Found'])}\n")
        else:
            report.write("  * None detected\n")

        report.write("\n- Weak Encryption Detected:\n")
        if crypto_results["Weak Encryption Detected"]:
            report.write(f"  * {', '.join(crypto_results['Weak Encryption Detected'])}\n")
        else:
            report.write("  * None detected\n")

        report.write("\n- Found Hardcoded Base64 Keys:\n")
        if crypto_results["Hardcoded Base64 Keys"]:
            report.write(f"  * {crypto_results['Hardcoded Base64 Keys'][0]}\n")
        else:
            report.write("  * None detected\n")

        report.write("\n- Potential RSA Private Keys Found:\n")
        if crypto_results["Potential RSA Private Keys"]:
            report.write(f"  * {crypto_results['Potential RSA Private Keys'][0]}\n")
        else:
            report.write("  * None detected\n")
    
    
        report.write("\n## Potential Passwords Found\n")
        passwords_found = find_potential_passwords(extracted_folder)
        if passwords_found:
            for pwd, path in passwords_found:
                report.write(f"- **Password**: {pwd} | **Found in**: {path}\n")
        else:
            report.write("- No potential passwords found.\n")
        report.write("\n")
        print("ANALYSING FIRMWARE DETAILS COMPLETED")

        # C. Security Details
        print("ANALYSING SECURITY DETAILS")
        report.write("# Security Details\n\n")
        security_details = extract_security_details(extracted_folder)
        for key, value in security_details.items():
            if isinstance(value, list):
                report.write(f"## {key}\n")
                for item in value:
                    report.write(f"- {item}\n")
                report.write("\n")  # Adds a space between lists
            elif isinstance(value, dict):
                report.write(f"## {key}\n")
                for sub_key, sub_value in value.items():
                    formatted_values = ", ".join(sub_value) if isinstance(sub_value, list) else sub_value
                    report.write(f"- **{sub_key}**: {formatted_values}\n")
                report.write("\n")
            else:
                report.write(f"- **{key}**: {value}\n")
        report.write("\n")
        print("ANALYSING SECURITY STRUCTURE COMPLETED")
        




# ...existing code...

if __name__ == "__main__":
    print(r"""
     _        _   _                              _           _     
    | |      | | (_)                            | |         (_)    
 ___| |_ __ _| |_ _  ___ ______ __ _ _ __   __ _| |_   _ ___ _ ___ 
/ __| __/ _` | __| |/ __|______/ _` | '_ \ / _` | | | | / __| / __|
\__ \ || (_| | |_| | (__      | (_| | | | | (_| | | |_| \__ \ \__ \
|___/\__\__,_|\__|_|\___|      \__,_|_| |_|\__,_|_|\__, |___/_|___/
                                                    __/ |          
                                                   |___/           
          """)
    if len(sys.argv) < 3:
        print("Usage: python static_analysis.py <firmware_binary> <report_file>")
        sys.exit(1)

    firmware_path = sys.argv[1]
    firmware_bin_path = firmware_path
    report_file = sys.argv[2]
    extract_dir = "extracted_firmware"
    print("Checking and installing all dependencies...")
    ensure_and_install_dependencies()
    print("All dependencies are installed successfully.")
    # Extract firmware
    test_extract_dir = extract_firmware(firmware_path, extract_dir)
    # Dynamically find the extracted folder
    extracted_folder = find_root_directory(extract_dir)

    # Continue using 'extracted_folder' and 'report_file' as needed...
    # ...existing code...
    generate_report()  # or other logic as appropriate
