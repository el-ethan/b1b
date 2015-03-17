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
        self.build_widgets()

    def build_widgets(self):
        ###### Left Frame ######
        left_frame = LabelFrame(self)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)

        Label(left_frame,
              text='Available Fonts',
              font=('Avenir Next', 20),
              bg='cornflower blue',
              bd=10).pack(side=TOP, fill=BOTH, expand=True)

        self.font_list = Listbox(left_frame,
                                  width=30,
                                  height=20,
                                  font=('Avenir Next', 12))
        self.font_list.pack(side=TOP, fill=BOTH, expand=True)

        for font in self.all_fonts:
            self.font_list.insert(END, font)
            self.font_list.bind('<Return>', self.change_font)

        ###### Right Frame ######
        right_frame = LabelFrame(self, padx=100, pady=100)
        right_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.test_display = Label(right_frame,
                             text='繁體字\n简体字',
                             font=('', 60),
                             pady=50)
        self.test_display.pack(side=TOP, fill=BOTH, expand=True)

        add_sc = Button(right_frame,
                            text="Add to SC Font List",
                            command=self.add_sc_font)
        add_sc.pack(side=TOP, fill=BOTH, expand=True)

        add_tc = Button(right_frame,
                            text="Add to TC Font List",
                            command=self.add_tc_font,
                            pady=20)
        add_tc.pack(side=TOP, fill=BOTH, expand=True)

        self.add_confirm = Label(right_frame)
        self.add_confirm.pack(side=TOP, fill=BOTH, expand=True)

    def change_font(self, event):
        font = self.font_list.get(ACTIVE)
        self.test_display.config(font=(font, 55))

    def add_sc_font(self):
        font = self.font_list.get(ACTIVE)
        with open('sc_fonts.txt', 'a') as f:
            f.write(font + '\n')
        self.add_confirm.config(text="Added '%s' to sc_fonts.txt" % font)

    def add_tc_font(self):
        font = self.font_list.get(ACTIVE)
        with open('tc_fonts.txt', 'a') as f:
            f.write(font + '\n')
        self.add_confirm.config(text="Added '%s' to tc_fonts.txt" % font)

root = Tk()
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()