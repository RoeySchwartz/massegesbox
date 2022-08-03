import socket
import threading

addresses_list = []

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))


def receive_messages():
    while True:
        server.listen()
        client_socket, address = server.accept()
        # client_socket.send(f"the code is: {code}".encode("utf-8"))
        print(f"connected to: {address}")
        addresses_list.append(address)
        my_message = client_socket.recv(1024).decode("utf-8")
        history_msg = open("history_messages.txt", "r+")
        history_msg.write(f"{my_message}")
        history_msg.close()
        client_socket.send(f"{my_message}".encode("utf-8"))
        client_socket.close()


receive_messages()
