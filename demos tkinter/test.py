import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack()

class MyLabel(tk.Label):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack()


root = tk.Tk()
MyFrame(root,
        highlightbackground="green",
        highlightcolor="green",
        highlightthickness=1,
        width=500,
        height=500)

root.mainloop()