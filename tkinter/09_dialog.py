import tkinter as tk
import tkinter.simpledialog as tksd


class MyDialog(tksd.Dialog):

    def body(self, master):
        tk.Label(master, text="First:").grid(row=0)
        tk.Label(master, text="Second:").grid(row=1)

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1  # initial focus

    def apply(self):
        first = int(self.e1.get())
        second = int(self.e2.get())
        self.result = first, second



root = tk.Tk()

dialog = MyDialog(root)

print(dialog.result)

root.mainloop()