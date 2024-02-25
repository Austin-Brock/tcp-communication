import socket

# Client setup
server_host = 'localhost'
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

# Accept an integer input from the user
while True:
    user_input = input("Enter an integer between 1 and 100: ")
    if user_input.isdigit():
        num = int(user_input)
        if 1 <= num <= 100:
            break
    print("Invalid input. Please try again.")

# Send a message to the server
client_name = "Client of Bob Smith"
message = f"{client_name},{num}"
client_socket.send(message.encode())

# Wait for the server's reply and print it
response = client_socket.recv(1024).decode()
server_name, server_number, sum_numbers = response.split(',')
print(f"{server_name} chose {server_number}, and the sum is {sum_numbers}")

# Close the socket
client_socket.close()
