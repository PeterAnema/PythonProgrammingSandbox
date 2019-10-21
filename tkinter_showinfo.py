import sys

if sys.version_info > (3,0):
    import tkinter
    import tkinter.messagebox as mbox 
    import tkinter.simpledialog as sd 
else:
    import Tkinter as tkinter
    import tkMessageBox as mbox
    import tkSimpleDialog as sd

# to hide main window
window = tkinter.Tk()
window.wm_withdraw() 

tekst = sd.askstring( title="Input",prompt="Email Address?")

mbox.showinfo(title = "Greetings", message = tekst)
