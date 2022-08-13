import os
import socket
import threading
import tkinter

# import tkinter.scrolledtext

client_id = os.getenv('CLIENT_ID')


class Client:
    def __init__(self, server_socket, HOST, PORT):
        self.message_box = None
        self.server_socket = server_socket
        self.HOST = HOST
        self.PORT = PORT

    def client_send_message(self, server_socket):
        message = ""
        while message.lower().strip() != 'bye':
            message = input(" -> ")  # again take input
            self.server_socket.send(f'{client_id}: {message}'.encode())  # send message

    def client_receive_message(self, server_socket):
        while True:
            data = server_socket.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print(data)

    def print_in_gui(self):
        win = tkinter.Tk()
        win.geometry("500x500")
        top_title = tkinter.Label(win, text="chat: ")
        top_title.place(x=230, y=1)

        self.message_box = tkinter.Text(win, height=2, width=55)
        self.message_box.place(relx=0.05, y=400)

        my_btn = tkinter.Button(win, text="send message:", command=self.button)
        my_btn.place(x=200, y=450)

        win.mainloop()

    def button(self):
        message_from_message_box = self.message_box.get("1.0", "end")
        self.server_socket.send(message_from_message_box.encode())
        threading.Thread(target=self.client_receive_message)

    def client_program(self):
        self.server_socket.connect((self.HOST, self.PORT))  # connect to the server
        threading.Thread(target=self.client_send_message, args=(self.server_socket,)).start()
        threading.Thread(target=self.client_receive_message, args=(self.server_socket,)).start()
        threading.Thread(target=self.print_in_gui).start()


if __name__ == '__main__':
    play = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.gethostbyname('localhost'), 5005)
    play.client_program()