# _*_ coding: utf-8 _*_
# TODO: max of 4 characters can be entered, enable Chinese typing
from Tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.tk.call("tk", "useinputmethods", "0")
        self.pack(fill=BOTH, expand=True)

        self.TC_fonts = []  # 9 total on my Mac
        self.SC_fonts = []  # 15 total on my Mac
        self.TCSC_fonts = ['Yuppy SC',
                           'Yuanti SC',
                           'Xingkai SC',
                           'Weibei SC',
                           'Wawati SC',
                           'Songti SC',
                           'MingLiU_HKSCS-ExtB',
                           'MingLiU_HKSCS',
                           'Libian SC',
                           'Lantinghei SC',
                           'Kaiti SC',
                           'Heiti SC',
                           'HanziPen SC',
                           'Hannotate SC',]
        self.create_widgets()

    def create_widgets(self):
        top_frame = Frame(self)
        top_frame.pack(side=TOP, fill=BOTH, expand=True)


        top_right_frame = Frame(top_frame, padx=10)
        top_right_frame.pack(side=RIGHT)
        self.var = IntVar()
        r1 = Radiobutton(top_right_frame,
                         variable=self.var,
                         value=1,
                         text='Traditional')
        r2 = Radiobutton(top_right_frame,
                         variable=self.var,
                         value=2,
                         text='Simplified')
        r3 = Radiobutton(top_right_frame,
                         variable=self.var,
                         value=3,
                         text='TC & SC')
        self.var.set(3)
        r1.pack(side=TOP, fill=BOTH, expand=True)
        r2.pack(side=TOP, fill=BOTH, expand=True)
        r3.pack(side=TOP, fill=BOTH, expand=True)


        top_left_frame = Frame(top_frame, padx=10)
        self.char_entry = Entry(top_left_frame)
        self.char_entry.insert('0', '字')
        self.char_entry.pack(side=TOP, fill=BOTH, expand=True)
        show_b = Button(top_left_frame, text='Show', command=self.set_fonts)
        quit_b = Button(top_left_frame, text='Quit', command=self.quit)

        top_left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        show_b.pack(side=LEFT, fill=BOTH, expand=True)
        quit_b.pack(side=LEFT, fill=BOTH, expand=True)

        self.font_info = Label(self,
                               text='font info',
                               bg='grey',
                               relief=SUNKEN)
        self.font_info.pack(side=TOP, fill=BOTH, expand=True)

        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)
        # Set initial display layout
        self.set_fonts()

    def set_fonts(self):
        char_set = self.select_charset()
        chars = self.char_entry.get()
        self.display_frame.destroy()
        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)

        # height = math.ceil(len(char_set) / 4)
        # width = 4
        fonts = self.font_gen()
        try:
            for r in range(7):
                for c in range(2):

                        L = Label(self.display_frame,
                              text=chars, relief=RIDGE,
                              font=(next(fonts), 55),
                              padx=30,
                              pady=10)
                        L.bind("<Enter>", self.test_callback)
                        L.grid(row=r, column=c, sticky=N+E+S+W)

        except StopIteration:
            pass

    def select_charset(self):
        mode = self.var.get()
        char_set = []
        if mode == 1:
            char_set = self.TC_fonts
        elif mode == 2:
            char_set = self.SC_fonts
        elif mode == 3:
            char_set = self.TCSC_fonts
        return char_set


    def font_gen(self):
        char_set = self.select_charset()
        for font in char_set:
            yield font

    def test_callback(self, event):
        name = event.widget.cget('font')
        self.font_info.config(text=name)



root = Tk()

root.resizable(0, 0)
app = Application(master=root)
app.mainloop()
root.destroy()