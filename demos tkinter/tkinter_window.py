from tkinter import *

class MyWindowClass(Frame):
    """ A GUI class """
    
    def __init__(self, master):
        """ Initialize the frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.place(relx=0.5, rely=0.5, anchor=CENTER)

        """ Create 3 buttons """
        self.button1 = Button(self, text = "Button1: 0")
        self.button1["command"] = self.update_button1
        self.button1.grid(row=0,column=0)

        self.button2 = Button(self)
        self.button2.configure(text = "Button2: 0")
        self.button2["command"] = self.update_button2
        self.button2.grid(row=0,column=1)

        self.button3 = Button(self)
        self.button3["text"] = "Button3: 0"
        self.button3["command"] = self.update_button3
        self.button3.grid(row=0,column=2)

    def update_button1(self):
        n = int(self.button1["text"].split(":")[1].strip())
        n += 1
        self.button1["text"] = "Button1: " + str(n)

    def update_button2(self):
        n = int(self.button2["text"].split(":")[1].strip())
        n += 1
        self.button2["text"] = "Button2: " + str(n)

    def update_button3(self):
        n = int(self.button3["text"].split(":")[1].strip())
        n += 1
        self.button3["text"] = "Button3: " + str(n)

# -------------------------------------------------------
        
root = Tk()
root.title("Demo TKinter Frame")
root.geometry("300x200+100+100")

window = MyWindowClass(root)

root.mainloop()
