import socket
import threading

messages = []
connected_clients = []
MAX_CONNECTION = 3

history = []


def get_client_messages(client_connection):
    print(history)
    for message in history:
        send_client_messages(message)
    while True:
        try:
            data = client_connection.recv(1024).decode()
        except ConnectionResetError:
            break

        if not data:
            # if data is not received break
            break
        send_client_messages(data)
        history.append(data)





def send_client_messages(message: str):
    for client in connected_clients:
        try:
            client.send(message.encode())
        except OSError:
            connected_clients.remove(client)


def server_program():
    # get the hostname
    host = socket.gethostbyname('localhost')
    port = 9092  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(MAX_CONNECTION)
    while True:
        new_connection, _ = server_socket.accept()  # accept new connection
        threading.Thread(target=get_client_messages, args=(new_connection,)).start()
        connected_clients.append(new_connection)


if __name__ == '__main__':
    server_program()
