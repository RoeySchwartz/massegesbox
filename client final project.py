import socket
import threading
import tkinter
import tkinter.scrolledtext

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.win = None
        threading.Thread(target=self.gui_config).start()

        self.is_init_display = False

        self.overview = None
        self.client = None
        self.name = ""
        self.message_box = None

    def connect(self):
        while not self.is_init_display:
            pass

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        threading.Thread(target=self.receive_msg, ).start()

    def gui_config(self):
        self.name = str(input("enter your name "))
        self.win = tkinter.Tk()
        self.win.geometry("500x500")
        top_title = tkinter.Label(self.win, text='chat:')
        top_title.place(x=230, y=1)

        self.overview = tkinter.scrolledtext.ScrolledText(self.win, height=20, width=55)
        self.overview.place(relx=0.05, y=20)
        self.overview.config(state="disabled")

        message_title = tkinter.Label(self.win, text="message:")
        message_title.place(x=220, y=375)

        self.message_box = tkinter.Text(self.win, height=2, width=55)
        self.message_box.place(relx=0.05, y=400)

        my_btn = tkinter.Button(self.win, text="send message:", command=self.button1)
        my_btn.place(x=200, y=450)

        self.is_init_display = True
        self.win.mainloop()

    def button1(self):
        self.overview.config(state="normal")
        message_to_server = f"{self.name}: {self.message_box.get('1.0', 'end')}"
        self.client.send(f"{message_to_server}".encode("utf-8"))
        self.overview.insert("end", f'{self.client.recv(1024).decode("utf-8")}')
        self.overview.config(state="disabled")

    def receive_msg(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.overview.config(state="normal")
                self.overview.insert("end", "\n" + str(message))
                self.overview.config(state="disable")
                self.client.send("Accept Message".encode('utf-8'))
            except Exception as err:
                print("Error" + str(err))


a = Client("192.168.1.29", 9090)
a.connect()