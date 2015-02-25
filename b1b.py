# TODO: max of 4 characters can be entered, buttons on top
from tkinter import *
import tkinter.font
import math

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)

        all_fonts = tkinter.font.families()
        self.TC_fonts = []  # 9 total on my Mac
        self.SC_fonts = []  # 15 total on my Mac
        for font in all_fonts:
            if 'SC' in font:
                self.SC_fonts.append(font)
            elif ' TC' in font:
                self.TC_fonts.append(font)
        self.TCSC_fonts = self.SC_fonts + self.TC_fonts
        self.create_widgets()

    def create_widgets(self):
        top_frame = Frame(self)
        top_frame.pack(side=TOP, fill=BOTH, expand=True)


        top_right_frame = Frame(top_frame, padx=10)
        top_right_frame.pack(side=RIGHT)
        var = IntVar()
        r1 = Radiobutton(top_right_frame,
                         variable=var,
                         value=1,
                         text='Traditional')
        r2 = Radiobutton(top_right_frame,
                         variable=var,
                         value=2,
                         text='Simplified')
        r3 = Radiobutton(top_right_frame,
                         variable=var,
                         value=3,
                         text='TC & SC')
        r1.pack(side=TOP, fill=BOTH, expand=True)
        r2.pack(side=TOP, fill=BOTH, expand=True)
        r3.pack(side=TOP, fill=BOTH, expand=True)


        top_left_frame = Frame(top_frame, padx=10)
        self.char_entry = Entry(top_left_frame)
        self.char_entry.insert('0', '比一笔')
        self.char_entry.pack(side=TOP, fill=BOTH, expand=True)
        show_b = Button(top_left_frame, text='Show', command=self.set_fonts)
        quit_b = Button(top_left_frame, text='Quit', command=self.quit)

        top_left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        show_b.pack(side=LEFT, fill=BOTH, expand=True)
        quit_b.pack(side=LEFT, fill=BOTH, expand=True)

        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)
        # Set initial display layout
        self.set_fonts()
        # height = math.ceil(len(self.TCSC_fonts) / 5)
        # width = 5
        # fonts = self.font_gen()
        # for r in range (height):
        #     for c in range (width):
        #         Label(self.display_frame,
        #               text='比一笔',
        #               relief=RIDGE, font=('Kaiti SC', 50)).grid(row=r, column=c)




    def set_fonts(self):
        chars = self.char_entry.get()
        self.display_frame.destroy()
        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)

        height = math.ceil(len(self.TCSC_fonts) / 4)
        width = 4
        fonts = self.font_gen()
        try:
            for r in range(height):
                for c in range(width):

                        L = Label(self.display_frame,
                              text=chars, relief=RIDGE,
                              font=(next(fonts), 55),
                              padx=10,
                              pady=10)
                        L.grid(row=r, column=c, sticky=N+E+S+W)
        except StopIteration:
            pass

    def font_gen(self):
        for font in self.TCSC_fonts:
            yield font

root = Tk()
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()