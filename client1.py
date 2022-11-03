import socket
from main_client import Client

host = socket.gethostbyname('localhost')
port = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client1 = Client(server, host, port, "Tomer")
Client1.client_program()
