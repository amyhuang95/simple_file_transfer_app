import socket  # create TCP connection

# Set up connection to the server
internet_address_family = socket.AF_INET  # IPv4
socket_type = socket.SOCK_STREAM  # TCP
client_socket = socket.socket(internet_address_family, socket_type)
host = 'localhost'
port = 8888
client_socket.connect((host, port))  # establish the connection

# Request a file
file_request = 'test.txt'
client_socket.send(file_request.encode())

# Receive data
with open('downloaded_file.txt', 'w') as file:
    buffer_size = 1024
    data = client_socket.recv(1024)
    file.write(data.decode())
    file.close()
print('File successfully received!')
