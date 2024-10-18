# OpenVPN Brute Force Tool

This Python script is designed to brute force the key password for an OpenVPN client configuration using a wordlist. The script attempts different passwords from the wordlist until it successfully finds the correct one or exhausts all options.

### Note: Script should be running with sudo.

## Prerequisites

- **Python 3.x**
- **OpenVPN** installed and accessible via the command line.
- A wordlist file containing potential passwords (e.g., `rockyou.txt`).
- OpenVPN configuration file (e.g., `client.conf`).

## How It Works

1. The script reads a list of passwords from the specified wordlist file (`rockyou.txt` in this example).
2. For each password, it:
   - Writes the password to a temporary file (`keypass.txt`).
   - Runs the OpenVPN command with the `--askpass` option, which uses the temporary file for the password.
   - Logs the results of each attempt to both the console and a log file (`output.log`).
3. If a password is successful, it logs the password and stops. If no password works, it logs that no password was found.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nednik19/OpenVPN-bruteforcer.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd openvpn-bruteforcer
   ```

3. **Install necessary dependencies**:
   This script only requires the standard Python libraries (`subprocess`, `os`, and `logging`), so there is no need for external dependencies.

4. **Make sure OpenVPN is installed**:
   OpenVPN must be installed and properly configured on your system. You can install it using your package manager:
   - For Ubuntu/Debian:
     ```bash
     sudo apt install openvpn
     ```
   - For macOS (using Homebrew):
     ```bash
     brew install openvpn
     ```

## Usage

1. **Prepare your OpenVPN configuration**:
   Ensure that you have an OpenVPN config file (`client.conf`) ready.

2. **Edit the script**:
   Modify the `file_path` variable in the script to point to your wordlist file:
   ```python
   file_path = "/path/to/your/wordlist.txt"
   ```

3. **Run the script**:
   Run the Python script:
   ```bash
   python3 bruteforcer.py
   ```

4. **Monitor the output**:
   The script will log its progress to both the console and `output.log` file. If it finds the correct password, it will output the success in the logs.

## Example Output

Here’s an example of what you might see in `output.log`:
```
2024-10-18 12:00:00 - INFO - Trying password: 123456
2024-10-18 12:00:05 - ERROR - Command failed with output:
    ...
2024-10-18 12:00:10 - INFO - Trying password: password123
2024-10-18 12:00:15 - INFO - Password found: password123
```

## Notes

- This script is meant for ethical and legal use. Ensure that you have permission to test the OpenVPN server in question.
- OpenVPN limits the number of password attempts. Be cautious, as repeated failures may result in temporary or permanent bans from the server.


## Disclaimer

This tool is intended for educational and ethical hacking purposes only. Unauthorized use of this script to access systems without permission is illegal and punishable under applicable laws.

