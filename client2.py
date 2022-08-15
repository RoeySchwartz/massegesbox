import socket
from main_client import Client

host = socket.gethostbyname('localhost')
port = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client2 = Client(server, host, port, "Roey")
Client2.client_program()
