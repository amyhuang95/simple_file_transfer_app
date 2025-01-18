import socket  # Create TCP connection
import threading  # Implement concurrency

# Set up server socket using TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8888
server_socket.bind(('0.0.0.0', 8888))

# Listening for incoming connections
server_socket.listen(5)  # up to 5 clients allowed in the queue
print(f'Server listening on port {port}...')


def handle_client(client_connection, client_address):
    print(f'Connected to {client_address}')
    file_request = client_connection.recv(1024).decode()

    try:
        with open(file_request, 'rb') as file:
            for data_chunk in file:
                client_connection.sendall(data_chunk)
    except FileNotFoundError:
        client_connection.send(b"File not found")  # byte string


# Process request
while True:
    client_connection, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(
        client_connection, client_address))
    thread.start()
