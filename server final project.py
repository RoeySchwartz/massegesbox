import socket
import threading

addresses_list = []

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


def recieve_messages():
    while True:
        client_socket, address = server.accept()
        # client_socket.send(f"the code is: {code}".encode("utf-8"))
        print(f"connected to: {address}")
        addresses_list.append(address)
        my_message = client_socket.recv(1024).decode("utf-8")
        history_msg = open("history_messages.txt", "w")
        history_msg.write(f"{my_message}\n")
        client_socket.send(f"{my_message}".encode("utf-8"))


recieve_messages()
