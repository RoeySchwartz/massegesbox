from multiprocessing.connection import Client
import socket

Client1 = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.gethostbyname('localhost'), 9090, "Tomer")

