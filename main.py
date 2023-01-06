# -----------Bolierplate Code Start -----
import socket
from distutils import command
from threading import Thread
from tkinter import *
from tkinter import ttk

PORT = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
textarea = None
labelchat = None
text_message = None

def connectServer():
    global SERVER
    global name
    client_name = name.get()
    SERVER.send(client_name.encode())


def openChatWindow():
    print("\n\t\t\t\tIP MESSENGER")

    # Client GUI starts here
    window = Tk()

    window.title('Messenger')
    window.geometry("500x400")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    name_1 = Label(window, text = "Enter Name:- ",font = ("Monospace", 15))
    name_1.place(x=15, y=15)

    name = Entry(window, font=("Monospace",12))
    name.place(x=150, y=18)
    name.focus()

    connect_1 = Button(window, text="Connect to server", font=("Monospace",12), command=connectServer)
    connect_1.place(x=350, y=15)

    seperator = ttk.Separator(window, orient="horizontal")
    seperator.place(x=0, y = 50, relwidth=1, height=1)

    active_labels = Label(window,text="Active Users", font=("Monospace",15))
    active_labels.place(x= 5, y= 52)

    active_list = Listbox(window, height=5, width=65, font=("Monospace",10))
    active_list.place(x=15, y= 76)

    bar_1 = Scrollbar(active_list)
    bar_1.place(relheight=1, relx = 0.97)
    bar_1.config(command= active_list.yview)

    connect_2 = Button(window, text="Connect", font=("Monospace",10))
    connect_2.place(x= 250, y = 170)

    disconnect_1 = Button(window, text="Disconnect", font=("Monospace",10))
    disconnect_1.place(x= 320, y =170)

    refresh_1 = Button(window, text="Refresh", font=("Monospace",10))
    refresh_1.place(x= 410, y=170)

    seperator2 = ttk.Separator(window, orient="horizontal")
    seperator2.place(x=0, y = 200, relwidth=1, height=1)

    chat_label = Label(window, text="Chat Window", font=("Monospace",15))
    chat_label.place(x= 5, y= 205)

    chat_list = Listbox(window, height=5, width=65, font=("Monospace",10))
    chat_list.place(x=15, y=230)

    bar_2 = Scrollbar(chat_list)
    bar_2.place(relheight=1, relx = 0.97)
    bar_2.config(command= chat_list.yview)


    attact_button = Button(window,text="Attach & Send", font=("Monospace",10))
    attact_button.place(x=15, y=330)

    attach_entry = Entry(window, font=("Monospace",12),width=30,bd =1)
    attach_entry.place(x=120, y=335)

    send_button = Button(window,text="Send", font=("Monospace",10))
    send_button.place(x=410, y=330)


    window.mainloop()



def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    openChatWindow()


setup()