import socket
# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to an IP address and port
address = ('127.0.0.1', 12345)
server_socket.bind(address)
# Listen for incoming connections
server_socket.listen(5)
print("Server listening on", address)
while True:
    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")
    # Send a response back to the client
    response = "Hello, Client!"
    client_socket.send(response.encode())
    # Close the client socket
    client_socket.close()
    # Close the server socket (unreachable in this particular sample program)
    server_socket.close()
    
