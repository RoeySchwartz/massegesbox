import socket
import threading
import random

addresses_list = []

HOST = '192.168.1.38'
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
messages = []


def receive_messages_from_client(client_socket, address):
    print(3)
    connect = True
    encryption = random.randint(1, 50)
    client_socket.send(str(encryption).encode("utf-8"))
    addresses_list.append(address)

    while connect:
        print(4)
        encryption = random.randint(1, 50)
        # client_socket.send(str(encryption).encode("utf-8"))
        message_from_client = client_socket.recv(1024).decode("utf-8")
        messages.append(message_from_client)
        print(messages)
        # history_msg = open("history_messages.txt", "r+")
        # history_msg.write(f"{message_from_client}")
        # history_msg.close()
        # client_socket.send(f"{message_from_client}".encode("utf-8"))
    # client_socket.close()


def connection():
    print(1)
    server.listen()
    while True:
        print(2)
        client_socket, address = server.accept()
        threading.Thread(target=receive_messages_from_client, args=(client_socket, address)).start()


connection()
