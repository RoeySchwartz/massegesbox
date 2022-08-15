import socket
import threading
import random

messages = []
connected_clients = []
MAX_CONNECTION = 3
encryption_key = random.randint(1, 50)

history_file = open("history_messages.txt", "r+")
history = history_file.readlines()


def send_encryption_key(client_connection):
    client_connection.send(str(encryption_key).encode("utf-8"))


def init_client_connection(client_connection):
    send_encryption_key(client_connection)
    send_history(client_connection)
    handle_client_messages(client_connection)


def decryption(message_to_decrypt):
    decrypted_message = ''
    for char_to_decrypt in message_to_decrypt:
        decrypted_message += chr(ord(char_to_decrypt) - int(encryption_key))
    history_file.write(decrypted_message)
    history_file.flush()


def encryption(client_connection, list_messages_to_encrypt):
    for message_to_encrypt in list_messages_to_encrypt:
        encrypted_message = ''
        for char_to_encrypt in message_to_encrypt:
            encrypted_message += chr(ord(char_to_encrypt) + int(encryption_key))
        client_connection.send(encrypted_message.encode("utf-8"))


def handle_client_messages(client_connection):
    while True:
        try:
            data = client_connection.recv(1024).decode("utf-8")
            print(data)
        except ConnectionResetError:
            break
        if not data:
            break
        send_message_to_all_clients(data)
        decryption(data)


def send_history(client_connection):
    encryption(client_connection, history)


def send_message_to_all_clients(message: str):
    for client in connected_clients:
        try:
            client.send(message.encode("utf-8"))
        except OSError:
            print("OSError")
            connected_clients.remove(client)


def start_server_program():
    host = socket.gethostbyname('localhost')
    port = 9090

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(MAX_CONNECTION)

    while True:
        new_connection, _ = server_socket.accept()
        threading.Thread(target=init_client_connection, args=(new_connection,)).start()
        connected_clients.append(new_connection)


if __name__ == '__main__':
    start_server_program()
