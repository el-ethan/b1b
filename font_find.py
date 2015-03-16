"""
font_find is a utility for displaying the fonts installed on your system
"""
from tkinter import *
import tkinter.font

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)

        self.all_fonts = tkinter.font.families()
        self.build_fontlists()
        self.build_test_area()

    def build_fontlists(self):
        font_disp1 = Text(self, width=30)
        font_disp1.pack(side=LEFT)
        for font in self.all_fonts:
            font_disp1.insert('0.0', font + '\n')

        font_disp2 = Text(self, width=30)
        font_disp2.pack(side=LEFT)

        for font in self.all_fonts:
            if any((('ti ' in font),
                   ('TC' in font),
                   ('SC' in font),
                   ('liU' in font),
                   ('gb' in font),
                   ('GB' in font),
                   (font.endswith('ti')))):
                font_disp2.insert('0.0', font + '\n')

    def build_test_area(self):
        self.test_entry = Entry(self)
        self.test_entry.pack(side=TOP)

        self.test_display = Label(self,
                             text='繁體字\n\n简体字',
                             font=('', 55),
                             padx=30,
                             pady=60)
        self.test_display.pack(side=TOP)
        change_button = Button(self,
                               command=self.change_font,
                               text='Change')
        change_button.pack(side=TOP)

    def change_font(self):
        font = self.test_entry.get()
        self.test_display.config(font=(font, 55))







root = Tk()

root.resizable(0, 0)
app = Application(master=root)
app.mainloop()