import sys
import tkinter as tk

class DemoKeyHandler(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind_all('<Key>', self.key_listener)

    @staticmethod
    def key_listener(event):
        if event.char == event.keysym:
            msg = 'Normal Key %r' % event.char
        elif len(event.char) == 1:
            msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
        else:
            msg = 'Special Key %r' % event.keysym

        mods = {
            0x0001: 'Shift',
            0x0002: 'Caps Lock',
            0x0004: 'Control',
            0x0008: 'Meta',
            0x0016: 'Alt',
            0x0010: 'Num Lock',
            0x0080: 'Alt R',
            0x0100: 'Mouse button 1',
            0x0200: 'Mouse button 2',
            0x0400: 'Mouse button 3'
        }
        shift = (event.state & 0x0001) != 0
        ctrl = (event.state & 0x0004) != 0
        alt = (event.state & 0x0008) != 0 or (event.state & 0x0080) != 0

        print(msg, event.char, event.keysym, event.state)


# ----------------------------------------------------------

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x400+100+100')

    root.title('Demo KeyHandler')

    frame = DemoKeyHandler(root)
    frame.pack()

    root.mainloop()
