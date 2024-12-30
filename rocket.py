import socket
import time
import random

# Set up the client (rocket)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))  # Connect to server

print("Rocket connected to ground station. Sending telemetry data...")

try:
    for _ in range(20):  # Send 20 telemetry updates
        altitude = random.uniform(1000, 5000)  # Simulated altitude in meters
        velocity = random.uniform(500, 1500)  # Simulated velocity in m/s
        telemetry = f"Altitude: {altitude:.2f} m, Velocity: {velocity:.2f} m/s"
        client_socket.sendall(telemetry.encode('utf-8'))  # Send data
        time.sleep(1)  # Wait 1 second before sending the next update
finally:
    client_socket.close()
    print("Rocket disconnected.")
