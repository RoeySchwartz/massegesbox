from multiprocessing.connection import Client
import socket

if __name__ == '__main__':
    Client2 = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.gethostbyname('localhost'), 9090, "Roey")
    Client2.client_program()
