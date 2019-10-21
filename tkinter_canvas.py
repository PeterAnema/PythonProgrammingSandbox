from tkinter import *

class MyCanvasClass(Canvas):
    """ A GUI class """
    
    def __init__(self, master):
        """ Initialize the frame """
        Canvas.__init__(self, master)
        self.pack()
        self.draw_canvas()

    def draw_canvas(self):
        for x in range(0,400,25):
            for y in range(0,200,25):
                self.create_rectangle(x, y, x+25, y+25, fill="lightblue")
        self.create_line(0, 0, 400, 200)
        self.create_line(0, 100, 400, 0, fill="red", dash=(4, 4))
       
## -------------------------------------------------------
        
root = Tk()
root.title("Demo TKinter Canvas")
root.geometry("300x200+100+100")

window = MyCanvasClass(root)

root.mainloop()
