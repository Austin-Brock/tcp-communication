from socket import *

# Client setup
server_name, server_port = 'localhost', 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
print('Connected to Remote Server')

# Input handling
client_name = "Client of Bob Smith"
while True:
    user_input = input("Enter an integer between 1 and 100: ")
    try:
        num = int(user_input)
        if 1 <= num <= 100:
            break
        else:
            print("Number must be between 1 and 100.")
    except ValueError:
        print("Please enter a valid integer.")

# Sending data
message = f"{client_name}, {num}"
client_socket.send(message.encode())
print('Data sent... waiting for the response.')

# Receiving and displaying response
response = client_socket.recv(1024).decode()
print('From Server:', response)
client_socket.close()

