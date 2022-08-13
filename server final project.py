import socket
import threading
import random

addresses_list = []

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def receive_messages_from_client(client_socket, address):
    connect = True
    encryption = random.randint(1, 50)
    client_socket.send(str(encryption).encode("utf-8"))

    while connect:
        encryption = random.randint(1, 50)
        client_socket.send(str(encryption).encode("utf-8"))
        print(f"connected to: {address}")
        addresses_list.append(address)
        message_from_client = client_socket.recv(1024).decode("utf-8")
        history_msg = open("studentsgrades.txt", "r+")
        history_msg.write(f"{message_from_client}")
        history_msg.close()
        client_socket.send(f"{message_from_client}".encode("utf-8"))
    client_socket.close()


def connection():
    server.listen()
    while True:
        client_socket, address = server.accept()
        threading.Thread(target=receive_messages_from_client, args=(client_socket, address)).start()


receive_messages_from_client()
