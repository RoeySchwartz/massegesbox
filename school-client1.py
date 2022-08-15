import socket
import threading
import tkinter
import tkinter.scrolledtext


class Client:
    def __init__(self, server_socket, HOST, PORT, name):
        self.data = None
        self.encryption_key = None
        self.name = name
        self.win = None
        self.overview = None
        self.message_box = None
        self.server_socket = server_socket
        self.HOST = HOST
        self.PORT = PORT

    def encryption(self, message_to_encrypt):
        encrypted_message = ''
        for char_to_encrypt in message_to_encrypt:
            encrypted_message += chr(ord(char_to_encrypt) + int(self.encryption_key))
        self.server_socket.send(encrypted_message.encode("utf-8"))

    def decryption(self, message_to_decrypt):
        decrypted_message = ""
        for char_to_decrypt in message_to_decrypt:
            decrypted_message += chr(ord(char_to_decrypt) - int(self.encryption_key))
        self.overview.config(state="normal")
        self.overview.insert("end", decrypted_message)
        self.overview.config(state="disabled")

    def client_receive_message(self, server_socket):
        while True:
            data = server_socket.recv(1024).decode("utf-8")
            self.decryption(data)
            if not data:
                break
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
        message_for_encryption = f'{self.name}: {message_from_message_box}'
        self.encryption(message_for_encryption)

    def client_program(self):
        self.server_socket.connect((self.HOST, self.PORT))
        self.encryption_key = self.server_socket.recv(1024).decode("utf-8")
        self.print_in_gui()


if __name__ == '__main__':
    play = Client(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.gethostbyname('localhost'), 9090, "moshe")
    play.client_program()
