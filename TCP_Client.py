import socket
# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
server_address = ('127.0.0.1', 12345)
client_socket.connect(server_address)
print(f"Connected to server at {server_address}")
# Send data to the server
data = "Hello, Server!"
client_socket.send(data.encode())
# Receive data from the server
response = client_socket.recv(1024)
print(f"Received data: {response.decode()}")
# Close the client socket
client_socket.close()