import socket

# Set up the server (ground station)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))  # Localhost and port number
server_socket.listen(1)  # Listen for 1 connection

print("Ground station ready. Waiting for telemetry data...")

connection, address = server_socket.accept()  # Accept a connection
print(f"Connected to rocket at {address}")

while True:
    data = connection.recv(1024)  # Receive up to 1024 bytes
    if not data:
        break
    print(f"Telemetry received: {data.decode('utf-8')}")

connection.close()
