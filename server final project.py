import socket
import threading
import time

addresses_list = []

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
threading.Thread(target=server.listen()).start()


def receive_messages_from_client():
    while True:
        threading.Thread(target=server.listen()).start()
        client_socket, address = server.accept()
        print(f"connected to: {address}")
        addresses_list.append(address)
        message_from_server = client_socket.recv(1024).decode("utf-8")
        history_msg = open("studentsgrades.txt", "r+")
        history_msg.write(f"{message_from_server}")
        history_msg.close()
        client_socket.send(f"{message_from_server}".encode("utf-8"))
        server.shutdown(2)
        time.sleep(2.0)


receive_messages_from_client()
