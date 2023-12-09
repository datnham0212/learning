import socket

# Define the target and ports to scan
target = '27.3.16.152'
ports = [21, 22, 80, 443]

# Loop through the ports and attempt to connect
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # Set a timeout of 1 second for each connection attempt
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    s.close()
