import paramiko

 

# Define the SSH parameters

ip_address = "192.168.1.1"

username = "admin"

password = "password"

 

# Create an SSH client

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

 

# Connect to the switch

client.connect(ip_address, username=username, password=password)

 

# Send a command to the switch and print the output

command = "show version"

stdin, stdout, stderr = client.exec_command(command)

output = stdout.read().decode()

print(output)

 

# Close the SSH connection

client.close()
