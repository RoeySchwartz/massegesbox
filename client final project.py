import socket
import threading
import tkinter
import tkinter.scrolledtext


class Client:

    def __init__(self, HOST, PORT):

        self.HOST = HOST
        self.PORT = PORT
        self.is_init_display = False

        gui_thread = threading.Thread(target=self.gui_config, )
        gui_thread.start()



    def connect(self):

        while not self.is_init_display:
            pass


        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))

        rcv_thread = threading.Thread(target=self.recieve_msg, )
        rcv_thread.start()


    def gui_config(self):
        self.name = str(input("enter your name "))
        self.win = tkinter.Tk()
        #self.win.title(f"{name} chat")

        self.win.geometry("500x500")
        self.my_label = tkinter.Label(self.win, text = 'chat:')
        self.my_label.place(x = 230, y = 1)

        self.my_text1 = tkinter.scrolledtext.ScrolledText(self.win, height= 20, width = 55)
        self.my_text1.place(relx = 0.05, y = 20)
        self.my_text1.config(state="disable")

        self.my_label2 = tkinter.Label(self.win, text = "massege:")
        self.my_label2.place(x = 220, y = 375)

        self.my_text2 = tkinter.Text(self.win, height=2, width=55)
        self.my_text2.place(relx = 0.05, y = 400)


        self.my_btn = tkinter.Button(self.win, text = "send massege:", command = self.button1)
        self.my_btn.place(x = 200, y = 450)

        self.is_init_display = True
        self.win.mainloop()

    def button1(self):
        self.my_text1.config(state="normal")
        self.message = f"{self.name}: {self.my_text2.get('1.0', 'end')}"
        self.client.send(self.message.encode("utf-8"))
        self.recieve_msg_from_server = self.client.recv(1024).decode("utf-8")
        self.my_text1.insert("0.0",self.recieve_msg_from_server)
        self.my_text1.config(state="disable")

    def recieve_msg(self):
            index = 0
            while index < 100:
                try:
                    message = self.client.recv(1024).decode('utf-8')
                    print(message)
                    self.my_text1.config(state="normal")
                    self.my_text1.insert("end","\n" +  str(message) )
                    self.my_text1.yview("end")
                    self.my_text1.config(state="disable")
                    index += 1
                    self.client.send("Accept Message".encode('utf-8'))
                except Exception as err:
                    print("Error" + str(err))


a = Client(socket.gethostbyname(socket.gethostname()), 9090)
a.connect()