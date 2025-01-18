import socket  # Create TCP connection
import threading  # Implement concurrency


# Process client request in multithreading function
def handle_client(client_connection, client_address):
    print(f'Connected to {client_address}')
    buffer_size = 1024
    # read server's reply
    file_request = client_connection.recv(buffer_size).decode()

    try:
        with open(file_request, 'rb') as file:
            for data_chunk in file:
                # note data_chunk is in binary format
                client_connection.sendall(data_chunk)
            file.close()
    except FileNotFoundError:
        client_connection.send(b"File not found")  # byte string


# Set up server socket using TCP/IP
internet_address_family = socket.AF_INET  # IPv4
socket_type = socket.SOCK_STREAM  # TCP
server_socket = socket.socket(internet_address_family, socket_type)

# Associate the socket with a specific network
host = 'localhost'
port = 8888
server_socket.bind((host, port))

# Listening for incoming connections
server_socket.listen()
print(f'Server listening on port {port}...')

# Process request using multithreading
while True:
    # waits for incomming connection and accept it
    client_connection, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(
        client_connection, client_address))
    thread.start()
