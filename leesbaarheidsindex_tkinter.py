from tkinter import Tk, Frame, Button, Text, Scrollbar, Label, StringVar, \
    CENTER, TOP, BOTTOM, LEFT, RIGHT, X, Y, SUNKEN, FLAT, E, W, N, END

#import leesbaarheidsindex as li
from leesbaarheidsindex_class import Leesbaarheidsindex

def set_info(value):
    if value:
        if isinstance(value, float):
            return '%.2f' % value
        else:
            return str(value)
    else:
        return '-'


class MyWindowClass(Frame):
    """ A tkinter GUI class """

    BACKGROUND_COLOR = '#dfe'

    def __init__(self, master):
        """ Initialize the frame """
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """ Create the widgets """
        self.configure(bg=MyWindowClass.BACKGROUND_COLOR)

        text_frame = Frame(self, bd=1, relief=SUNKEN)
        text_frame.pack(side=TOP, fill=X, pady=5, padx=5)

        self.text = Text(text_frame, height=20, width=100)
        self.text.pack(side=LEFT, fill=Y)
        scrollbar = Scrollbar(text_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrollbar.set)

        button = Button(self, text='Bereken', command=self.calculate_info)
        button.configure(bg=MyWindowClass.BACKGROUND_COLOR,
                         highlightbackground=MyWindowClass.BACKGROUND_COLOR)
        button.pack(side=LEFT, anchor=N, padx=26)

        label_frame = Frame(self)
        label_frame.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        label_frame.pack(side=LEFT, pady=5, padx=15)

        label1 = Label(label_frame, text='Aantal woorden')
        label1.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        label1.pack(anchor=W)

        label2 = Label(label_frame, text='Aantal zinnen')
        label2.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        label2.pack(anchor=W)

        label3 = Label(label_frame, text='Gemiddelde woordlengte')
        label3.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        label3.pack(anchor=W)

        label4 = Label(label_frame, text='Gemiddeld aantal lettergrepen per woord')
        label4.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        label4.pack(anchor=W)

        label5 = Label(label_frame, text='Gemiddeld aantal woorden per zin')
        label5.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        label5.pack(anchor=W)

        label6 = Label(label_frame, text='Leesbaarheidsindex')
        label6.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        label6.pack(anchor=W)

        info_frame = Frame(self)
        info_frame.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        info_frame.pack(side=LEFT, pady=5, padx=15)

        self.info1 = StringVar()
        info_label1 = Label(info_frame, textvariable=self.info1)
        info_label1.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        info_label1.pack(anchor=W)

        self.info2 = StringVar()
        info_label2 = Label(info_frame, textvariable=self.info2)
        info_label2.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        info_label2.pack(anchor=W)

        self.info3 = StringVar()
        info_label3 = Label(info_frame, textvariable=self.info3)
        info_label3.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        info_label3.pack(anchor=W)

        self.info4 = StringVar()
        info_label4 = Label(info_frame, textvariable=self.info4)
        info_label4.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        info_label4.pack(anchor=W)

        self.info5 = StringVar()
        info_label5 = Label(info_frame, textvariable=self.info5)
        info_label5.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        info_label5.pack(anchor=W)

        self.info6 = StringVar()
        info_label6 = Label(info_frame, textvariable=self.info6)
        info_label6.configure(bg=MyWindowClass.BACKGROUND_COLOR)
        info_label6.pack(anchor=W)

        self.info1.set('0')
        self.info2.set('0')
        self.info3.set('-')
        self.info4.set('-')
        self.info5.set('-')
        self.info6.set('-')

    def calculate_info(self):
        # t = self.text.get("1.0", END)
        # self.info1.set( li.aantal_woorden(t) )
        # self.info2.set( li.aantal_zinnen(t) )
        # self.info3.set( set_info(li.gemiddelde_woordlengte(t)) )
        # self.info4.set( set_info(li.gemiddeld_aantal_lettergrepen_per_woord(t)) )
        # self.info5.set( set_info(li.gemiddeld_aantal_woorden_per_zin(t)) )
        # self.info6.set( set_info(li.leesbaarheidsindex(t)) )

        t = self.text.get("1.0", END)
        li = Leesbaarheidsindex(t)
        self.info1.set( li.get_aantal_woorden() )
        self.info2.set( li.get_aantal_zinnen() )
        self.info3.set( set_info(li.get_gemiddelde_woordlengte()) )
        self.info4.set( set_info(li.get_gemiddeld_aantal_lettergrepen_per_woord()) )
        self.info5.set( set_info(li.get_gemiddeld_aantal_woorden_per_zin()) )
        self.info6.set( set_info(li.get_leesbaarheidsindex()) )


## -------------------------------------------------------

if __name__ == '__main__':

    root = Tk()
    root.title('Leesbaarheidsindex')
    root.geometry('+100+100')
    root.configure(bg=MyWindowClass.BACKGROUND_COLOR)

    myWindow = MyWindowClass(root)

    root.mainloop()