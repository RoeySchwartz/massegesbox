from multiprocessing.connection import Client
import socket

Client2 = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.gethostbyname('localhost'), 9090, "moshe")
