from multiprocessing.connection import Client
import socket

if __name__ == '__main__':
    Client3 = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.gethostbyname('localhost'), 9090, "Edan")
    Client3.client_program()
