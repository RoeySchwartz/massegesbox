import socket
from main_client import Client

host = socket.gethostbyname('localhost')
port = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client3 = Client(server, host, port, "Edan")
Client3.client_program()
