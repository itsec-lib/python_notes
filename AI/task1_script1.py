from netmiko import ConnectHandler

# Define the device to connect to
device = {
    'device_type': 'cisco_nxos',  # Device type for a Nexus switch
    'ip': '172.16.0.10',          # Mgmt IP address of the device
    'username': 'admin',          # Username for authentication
    'password': 'C!sco123',       # Password for authentication
}

# Connect to the device using SSH
try:
    connection = ConnectHandler(**device)
    print("Connected successfully!")
except Exception as e:
    print(f"Error: {e}")

# Sending command to the device
command = 'show ip interface brief'
print(f"Sending the following command: {command}")
output = connection.send_command(command)

# Print the output
print(output)

# Disconnect the session
connection.disconnect()

