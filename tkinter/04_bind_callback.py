import tkinter as tk

root = tk.Tk()

def callback(event):
    print("clicked at", event.x, event.y)

frame = tk.Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()