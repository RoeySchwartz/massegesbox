import os
import socket
import threading
import tkinter
import tkinter.scrolledtext

client_id = os.getenv('CLIENT_ID')




class Client:
    def __init__(self, server_socket, HOST, PORT ):
        self.name = input('enter your name: ')
        self.win = None
        self.overview = None
        self.message_box = None
        self.server_socket = server_socket
        self.HOST = HOST
        self.PORT = PORT



    def client_receive_message(self, server_socket):
        while True:
            data = server_socket.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            self.overview.config(state='normal')
            self.overview.insert('end', str(data))
            self.overview.config(state='disabled')
            print(str(data))

    def print_in_gui(self):
        self.win = tkinter.Tk()
        self.win.geometry("500x500")
        top_title = tkinter.Label(self.win, text="chat: ")
        top_title.place(x=230, y=1)

        self.overview = tkinter.scrolledtext.ScrolledText(self.win, height=20, width=55)
        self.overview.place(relx=0.05, y=20)
        self.overview.config(state="disabled")

        self.message_box = tkinter.Text(self.win, height=2, width=55)
        self.message_box.place(relx=0.05, y=400)

        my_btn = tkinter.Button(self.win, text="send message:", command=self.button)
        my_btn.place(x=200, y=450)

        threading.Thread(target=self.client_receive_message, args=(self.server_socket,)).start()

        self.win.mainloop()

    def button(self):
        message_from_message_box = self.message_box.get("1.0", "end")
        self.message_box.delete('1.0', 'end')
        self.server_socket.send(f'{self.name}: {message_from_message_box}'.encode())


    def client_program(self):
        self.server_socket.connect((self.HOST, self.PORT))  # connect to the server
        self.print_in_gui()




if __name__ == '__main__':
    play = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.gethostbyname('localhost'), 9092)
    play.client_program()
