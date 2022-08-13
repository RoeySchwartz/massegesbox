import os
import socket
import threading

client_id = os.getenv('CLIENT_ID')


def client_send_message(server_socket):
    message = ""
    while message.lower().strip() != 'bye':
        message = input(" -> ")  # again take input
        server_socket.send(f'{client_id}: {message}'.encode())  # send message


def client_receive_message(server_socket):
    while True:
        data = server_socket.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print_in_gui(str(data))


def print_in_gui(message):
    print(message)


def client_program():
    host = socket.gethostbyname('localhost')
    port = 5005  # socket server port number
    server_socket = socket.socket()  # instantiate
    server_socket.connect((host, port))  # connect to the server
    threading.Thread(target=client_send_message, args=(server_socket,)).start()
    threading.Thread(target=client_receive_message, args=(server_socket,)).start()


if __name__ == '__main__':
    client_program()
