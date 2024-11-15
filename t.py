import paramiko
from scp import SCPClient

# Set the variables for SSH connection
hostname = '82.112.227.1'  # Replace with the IP address of the remote machine
port = 22  # Default SSH port
username = 'root'  # Replace with your remote machine's username
password = 'Cappriciosec@2024'  # Replace with your remote machine's password (or use key-based authentication)

# Set the file paths
local_file = '/home/ec2-user/assessmentsystem/backup1.zip'  # Path to the file on the local machine
remote_path = '/root/psvec/backup.zip'  # Path on the remote machine where the file will be copied

# Create an SSH client
ssh = paramiko.SSHClient()

# Automatically add the remote host key (to avoid "host key verification failed" errors)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote machine using SSH
    ssh.connect(hostname, port=port, username=username, password=password)

    # Create an SCP client connected to the SSH session
    with SCPClient(ssh.get_transport()) as scp:
        # Transfer the file
        scp.put(local_file, remote_path)

    print(f"Successfully transferred {local_file} to {hostname}:{remote_path}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the SSH connection
    ssh.close()
