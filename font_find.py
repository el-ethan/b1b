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
        left_frame1 = LabelFrame(self)
        left_frame1.pack(side=LEFT, fill=BOTH)

        Label(left_frame1,
              text='All Fonts',
              font=('Avenir Next', 20),
              bg='cornflower blue',
              bd=10).pack(side=TOP, fill=BOTH)
        self.font_list1 = Listbox(left_frame1,
                                  width=30,
                                  height=20,
                                  font=('Avenir Next', 12))
        self.font_list1.pack(side=TOP, fill=BOTH)
        for font in self.all_fonts:
            self.font_list1.insert(END, font)
            self.font_list1.bind('<Double-Button-1>', self.change_font1)

        left_frame2 = LabelFrame(self)
        left_frame2.pack(side=LEFT, fill=BOTH)

        Label(left_frame2,
              text='Potential Chinese Fonts',
              font=('Avenir Next', 20),
              bg='cornflower blue',
              bd=10).pack(side=TOP, fill=BOTH)
        self.font_list2 = Listbox(left_frame2,
                                  width=30,
                                  height=20,
                                  font=('Avenir Next', 12))
        self.font_list2.pack(side=TOP, fill=BOTH)

        for font in self.all_fonts:
            if any((('ti ' in font),
                   ('TC' in font),
                   ('SC' in font),
                   ('liU' in font),
                   ('gb' in font),
                   ('GB' in font),
                   (font.endswith('ti')))):
                self.font_list2.insert(END, font)
                self.font_list2.bind('<Double-Button-1>', self.change_font2)

    def build_test_area(self):
        test_frame = LabelFrame(self)
        test_frame.pack(side=LEFT, fill=BOTH)

        self.test_display = Label(test_frame,
                             text='繁體字\n简体字',
                             font=('', 60),
                             padx=80)
        self.test_display.pack(side=RIGHT, fill=BOTH, expand=True)
        # change_button = Button(self,
        #                        command=self.change_font,
        #                        text='Change')
        # change_button.pack(side=TOP)

    def change_font1(self, event):
        font = self.font_list1.get(ACTIVE)
        self.test_display.config(font=(font, 55))

    def change_font2(self, event):
        font = self.font_list2.get(ACTIVE)
        self.test_display.config(font=(font, 55))







root = Tk()

root.resizable(0, 0)
app = Application(master=root)
app.mainloop()