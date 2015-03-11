"""
b1b (比一笔）is a GUI application for comparing Chinese fonts.

A few notes on operation:

* The app does not currently support MAC OS X Chinese input methods,
so you must input text by pasting it.

* Once you have pasted new text into the entry box, click 'Show'
to refresh the display.

* Although you can enter an arbitrarily long string of characters into the
entry box, the display will grow too large to be useful with too many
characters, so it is best to limit your entry to A MAX OF 4 CHARACTERS at
a time.

* You can mix Simplified and Traditional characters in your input if you wish.

* Use the buttons on the top right to customize the display for a particular
type of characters. Traditional and Simplified will display together by
default.

* Hover the mouse arrow over characters to display their font information in
the gray bar below the text entry box.

* Depending on your OS, you may have fewer/more Chinese system fonts than
the app was intended to be used with, so it is normal if some of the cells
in the character display area are blank.
"""

import re
from tkinter import *
import tkinter.font
import math

class Application(Frame):
    """Main application for b1b"""
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
        ##############################
        # Frame for operation widgets
        ##############################
        top_frame = Frame(self)
        top_frame.pack(side=TOP, fill=BOTH, expand=True)
        ##############################
        # Radio button frame and buttons
        ##############################
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
        ##############################
        # Character entry, Show/Quit buttons
        ##############################
        top_left_frame = Frame(top_frame, padx=10)
        self.char_entry = Entry(top_left_frame)
        self.char_entry.insert('0', '字')
        self.char_entry.pack(side=TOP, fill=BOTH, expand=True)
        show_b = Button(top_left_frame, text='Show', command=self.set_fonts)
        quit_b = Button(top_left_frame, text='Quit', command=self.quit)
        top_left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        show_b.pack(side=LEFT, fill=BOTH, expand=True)
        quit_b.pack(side=LEFT, fill=BOTH, expand=True)
        ##############################
        # Font info display
        ##############################
        self.font_info = Label(self,
                               text='font info',
                               bg='grey',
                               relief=SUNKEN)
        self.font_info.pack(side=TOP, fill=BOTH, expand=True)
        ##############################
        # Character display
        ##############################
        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)
        # Set initial display layout
        self.set_fonts()

    def set_fonts(self):
        """Set font display area"""
        char_set = self.select_charset()
        chars = self.char_entry.get()
        self.display_frame.destroy()
        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)

        height = math.ceil(len(char_set) / 4)
        width = 4
        fonts = self.font_gen()
        try:
            for r in range(height):
                for c in range(width):

                        L = Label(self.display_frame,
                              text=chars, relief=RIDGE,
                              font=(next(fonts), 55),
                              padx=30,
                              pady=10)
                        L.bind("<Enter>", self.callback)
                        L.grid(row=r, column=c, sticky=N+E+S+W)

        except StopIteration:
            pass

    def select_charset(self):
        """Select and set correct character set"""
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
        """Generate fonts for labels in display"""
        char_set = self.select_charset()
        for font in char_set:
            yield font

    def callback(self, event):
        """Generate text for font info display"""
        name = event.widget.cget('font')
        name = re.sub('[{}(55)]', '', name)
        self.font_info.config(text=name)



root = Tk()

root.resizable(0, 0)
app = Application(master=root)
app.mainloop()