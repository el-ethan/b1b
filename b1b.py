from tkinter import *

ALL = N+E+S+W

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        left_frame = Frame(self)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        char_entry = Entry(left_frame, text='Type characters here')
        char_entry.pack(side=TOP, fill=BOTH, expand=True)

        var = IntVar()
        r1 = Radiobutton(left_frame,
                         variable=var,
                         value=1,
                         text='Traditional')
        r2 = Radiobutton(left_frame,
                         variable=var,
                         value=2,
                         text='Simplified')
        r3 = Radiobutton(left_frame,
                         variable=var,
                         value=3,
                         text='TC & SC')
        r1.pack(side=TOP, fill=BOTH, expand=True)
        r2.pack(side=TOP, fill=BOTH, expand=True)
        r3.pack(side=TOP, fill=BOTH, expand=True)

        button_frame = Frame(left_frame)
        button_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
        show_b = Button(button_frame, text='Show')
        quit_b = Button(button_frame, text='Quit')
        show_b.pack(side=LEFT, fill=BOTH, expand=True)
        quit_b.pack(side=LEFT, fill=BOTH, expand=True)

        display_frame = LabelFrame(self)
        display_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        display_font = ('Kaiti SC', 24)
        for r in range (5):
            for c in range (3):
                Label(display_frame,
                      text='比一笔',
                      relief=RIDGE, font=display_font).grid(row=r, column=c)



root = Tk()
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()