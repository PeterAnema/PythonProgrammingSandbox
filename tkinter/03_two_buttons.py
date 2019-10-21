import tkinter as tk

class App:

    def __init__(self, master):

        frame = tk.Frame(master)
        frame.pack()

        self.button = tk.Button(frame,
                                text="QUIT",
                                fg="red",
                                command=frame.quit)
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == '__main__':

    root = tk.Tk()
    app = App(root)
    root.mainloop()
