from socket import *
import random

# Server setup
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', server_port))
server_socket.listen(1)
server_name = "Server of Bob Smith"
print(server_name + " is now ONLINE")

while True:
    connection_socket, addr = server_socket.accept()
    received_data = connection_socket.recv(1024).decode()
    client_name, client_num_str = received_data.split(', ')
    client_num = int(client_num_str)

    # Server's actions
    server_num = random.randint(1, 100)
    sum_numbers = client_num + server_num
    print(f"{client_name} connected. {server_name}")

    # Creating response message
    response_message = f"{server_name}, Server Number: {server_num}, Sum: {sum_numbers}"
    connection_socket.send(response_message.encode())
    print("Sent response to client.")
    connection_socket.close()

