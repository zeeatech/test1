import paramiko
from scp import SCPClient
import glob
import os

# Set the variables for SSH connection
hostname = '82.112.227.1'  # Replace with the IP address of the remote machine
port = 22  # Default SSH port
username = 'root'  # Replace with your remote machine's username
password = 'Cappriciosec@2024'  # Replace with your remote machine's password (or use key-based authentication)

# Find all .sql files in the current directory
sql_files = glob.glob('./*.xlsx')  # This will find all .sql files in the current folder

# If no .sql files are found, print a message and exit
if not sql_files:
    print("No .sql files found in the current directory.")
    exit()

# Remote path where the files will be copied
remote_path = '/root/psvec/'

# Create an SSH client
ssh = paramiko.SSHClient()

# Automatically add the remote host key (to avoid "host key verification failed" errors)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote machine using SSH
    ssh.connect(hostname, port=port, username=username, password=password)

    # Create an SCP client connected to the SSH session
    with SCPClient(ssh.get_transport()) as scp:
        # Transfer all .sql files
        for sql_file in sql_files:
            # Send each .sql file to the remote directory
            scp.put(sql_file, os.path.join(remote_path, os.path.basename(sql_file)))

    print(f"Successfully transferred {len(sql_files)} .sql files to {hostname}:{remote_path}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the SSH connection
    ssh.close()
