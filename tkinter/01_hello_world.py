try:
    import tkinter as tk    # Python 3
except:
    import Tkinter as tk    # Python 2

root = tk.Tk()

w = tk.Label(root, text="Hello, world!")
w.pack()

root.mainloop()