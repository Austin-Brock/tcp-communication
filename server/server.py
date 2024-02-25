import socket
import random

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = 'localhost'
server_port = 12345
server_socket.bind((server_host, server_port))
server_socket.listen()

print("Server of Bob Smith is listening on port", server_port)

while True:
    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Received a connection from {addr}")
    
    # Receive the message from the client
    message = client_socket.recv(1024).decode()
    client_name, client_number = message.split(',')
    client_number = int(client_number)
    print(f"Client's name: {client_name}")
    print("Server's name: Server of Bob Smith")
    
    # Server generates a random number, calculates the sum
    server_number = random.randint(1, 100)
    sum_numbers = server_number + client_number
    
    # Send the response to the client
    response = f"Server of Bob Smith,{server_number},{sum_numbers}"
    client_socket.send(response.encode())
    
    # Close the client connection
    client_socket.close()
