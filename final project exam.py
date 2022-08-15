from multiprocessing.connection import Client
import socket

if __name__ == '__main__':
    play = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.gethostbyname('localhost'), 9090, "moshe")
    play.client_program()
