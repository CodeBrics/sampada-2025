# Instructions for Building and Execution

## How to Get the Code?

Users need to clone the source code from our GitLab repository to their local machine. Follow these steps to implement it:

1. Open a terminal or command prompt on your device.
2. Use the following command to clone the repository from GitLab.


    Bash:
   #
       git clone https://gitlab.com/craftbud_studios/sampada-hackathon-iot


4. Navigate to the cloned directory from your terminal.


    Bash:
    #     
        cd sampada-hackathon-iot/ 


Done! Now your code is ready to be executed.

## Executing the Script

You need to run the following command line instruction to execute the script in your terminal after cloning the source code into your local machine:

Format: ``` python3 file_name.py <firmware_binary> <report_file> ```

### Replace the instruction accordingly:
- Name of the file: `file_name.py`
- Path of the binary file (.bin): `<firmware_binary>`
- Path of the report file (.txt): `<report_file>`

### Example: ``` python analysis_tool.py firmware.bin report.txt ```


## Automation

We ensure in our script that the user does not need to perform any other tasks other than executing the command line instruction. To make the program automated, as per the requirements, we have used an `ensure_and_install_dependencies()` function which:

- Automatically checks and installs all required tools.
- Ensures that all the tools are available before execution, without the need for them to be preinstalled on the user's system.

Therefore, there is no need for manual installations, making the process automated.
