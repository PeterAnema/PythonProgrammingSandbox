import tkinter as tk
from socket_client import ClientSession

IP_ADDRESS = '127.0.0.1'
IP_PORT = 6669

class Application(tk.Frame):
    BACKGROUND_COLOR = 'lightblue'

    def __init__(self, master=None):
        super().__init__(master, bg=Application.BACKGROUND_COLOR)

        self.entry_stringvar = tk.StringVar()

        self.grid()
        self.createWidgets()

        self.session = ClientSession(host=IP_ADDRESS, port=IP_PORT)
        self.session.connect()

        self.receive()

    def createWidgets(self):
        self.chatbox = tk.Text(self,
                               state=tk.DISABLED,
                               height=10,
                               relief=tk.SUNKEN,
                               borderwidth=2)
        self.chatbox.pack(fill=tk.X,
                          padx=10,
                          pady=10)

        self.entry = tk.Entry(self,
                              textvariable=self.entry_stringvar,
                              width=50)
        self.entry.pack(fill=tk.X, padx=10)

        self.sendButton = tk.Button(self,
                                    text='Send',
                                    command=self.handleSendButton)
        self.sendButton.pack(ipadx=5, ipady=5, pady=10)

        self.quitButton = tk.Button(self,
                                    text='Leave chat room',
                                    command=self.handleQuitButton)
        self.quitButton.pack(ipadx=5, ipady=5, pady=10)

    def handleSendButton(self):
        self.send()
        self.receive()

    def send(self):
        message = self.entry_stringvar.get()
        self.entry_stringvar.set('')
        self.session.send(message)

    def receive(self):
        response = self.session.receive()
        self.chatbox.configure(state='normal')
        self.chatbox.insert(tk.END, response)
        self.chatbox.configure(state='disabled')
        self.chatbox.pack()

    def handleQuitButton(self):
        if self.session:
            self.session.disconnect()
            self.session = None
        self.quit()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Chat Room')
    app = Application(root)
    root.mainloop()
