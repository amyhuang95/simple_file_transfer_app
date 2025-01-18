import socket  # create TCP connection

# Set up connection to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8888
client_socket.connect(('localhost', port))

# Request a file
file_request = 'test.txt'
client_socket.send(file_request.encode())

# Receive data
with open('downloaded_file.txt', 'wb') as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file.write(data)
print('File successfully received!')
