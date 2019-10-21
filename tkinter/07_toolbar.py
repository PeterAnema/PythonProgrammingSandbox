import tkinter as tk

root = tk.Tk()

def callback():
    print("called the callback!")

# create a toolbar
toolbar = tk.Frame(root)

b = tk.Button(toolbar, text="new", width=6, command=callback)
b.pack(side=tk.LEFT, padx=2, pady=2)

b = tk.Button(toolbar, text="open", width=6, command=callback)
b.pack(side=tk.LEFT, padx=2, pady=2)

toolbar.pack(side=tk.TOP, fill=tk.X)

tk.mainloop()