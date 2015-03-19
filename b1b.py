#!/usr/bin/env python3
"""
b1b (比一笔）is a GUI application for comparing Chinese fonts.

A few notes on operation:

* For this app to work properly SC_fonts and TC_fonts lists will need
to be populated. You can modify the code to add the fonts manually or
you can first run the z1z font finder utility to add the fonts you want
to this app.

* The app does not currently support MAC OS X Chinese input methods,
so you must input text by pasting it if you are using OS X. This is a
known issue with tkinter.

* Once you have pasted new text into the entry box, click 'Show'
to refresh the display.

* Although you can enter an arbitrarily long string of characters into the
entry box, the display will grow too large to be useful with too many
characters, so it is best to limit your entry to A MAX OF 4 CHARACTERS at
a time.

* You can mix Simplified and Traditional characters in your input if you wish.
However, keep in mind that some characters may not display properly in fonts
meant specifically for SC or TC, and will default to some other font, probably
heiti.

* Use the buttons on the top right to customize the display for a particular
type of characters. Traditional and Simplified will display together by
default.

* Hover the mouse arrow over characters to display their font information in
the blue bar below the text entry box.
"""
import re
import math
from tkinter import *
import tkinter.font
from tkinter.messagebox import showwarning

class Application(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)
        self.get_fonts()
        self.draw_widgets()

        if not self.SCTC_fonts:
            self.open_font_picker()

        menu = Menu(root)
        root.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Font Picker",
                              command=self.open_font_picker)

    def open_font_picker(self):
        """Open font picker and update b1b display once picker is closed"""
        w = FontPicker()
        w.wait_window(w)
        self.get_fonts()
        self.set_fonts()

    def get_fonts(self):
        """Get fonts from text files"""
        with open('sc_fonts.txt', 'r') as f:
            self.SC_fonts = f.readlines()
        with open('tc_fonts.txt', 'r') as f:
            self.TC_fonts = f.readlines()
        self.SCTC_fonts = self.SC_fonts + self.TC_fonts


    def draw_widgets(self):
        """Draw widgets for main app"""
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
        self.char_entry.insert('0', '比一笔')
        self.char_entry.pack(side=TOP, fill=BOTH, expand=True)
        show_b = Button(top_left_frame, text='Show', command=self.set_fonts)
        quit_b = Button(top_left_frame, text='Quit', command=self.quit)
        top_left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        show_b.pack(side=LEFT, fill=BOTH, expand=True)
        quit_b.pack(side=LEFT, fill=BOTH, expand=True)

        self.font_info = Label(self,
                               text='font info',
                               bg='cornflower blue',
                               relief=SUNKEN)
        self.font_info.pack(side=TOP, fill=BOTH, expand=True)

        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)
        # Set initial display layout
        self.set_fonts()

    def set_fonts(self):
        """Set font display area"""
        char_set = self.select_charset()
        chars = self.char_entry.get()

        if len(chars) > 4:
            showwarning("Too many characters!",
                        "Input too long, trimmed to 4 characters",
                        default='ok')
            chars = chars[:4]
            self.char_entry.delete(4, END)
        # TODO: come up with better way to refresh display. If there is one...
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
                        L.bind("<Enter>", self.show_font_info)
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
            char_set = self.SCTC_fonts
        return char_set


    def font_gen(self):
        """Generate fonts for labels in display"""
        char_set = self.select_charset()
        for font in char_set:
            yield font.strip()

    def show_font_info(self, event):
        """Generate text for font info display"""
        name = event.widget.cget('font')
        name = re.sub('[{}(55)]', '', name)
        self.font_info.config(text=name)

class FontPicker(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        self.all_fonts = tkinter.font.families()
        self.draw_widgets()

    def draw_widgets(self):
        ###### Left Frame ######
        left_frame = LabelFrame(self)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)

        Label(left_frame,
              text='Available Fonts',
              font=('', 20),
              bg='cornflower blue').pack(side=TOP, fill=BOTH, expand=True)

        self.font_list = Listbox(left_frame,
                                  width=30,
                                  height=20)
        self.font_list.pack(side=TOP, fill=BOTH, expand=True)
        # Populate Listbox widget
        for font in self.all_fonts:
            self.font_list.insert(END, font)
            self.font_list.bind('<Return>', self.change_font)

        ###### Right Frame ######
        right_frame = LabelFrame(self)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.char_display = Label(right_frame,
                             text='繁體字\n简体字',
                             font=('', 80),
                             pady=50,
                             padx=50)
        self.char_display.pack(side=TOP, fill=BOTH, expand=True)

        add_sc = Button(right_frame,
                            text="Add to SC Font List",
                            command=self.add_sc_font)
        add_sc.pack(side=TOP, fill=BOTH, expand=True)

        add_tc = Button(right_frame,
                            text="Add to TC Font List",
                            command=self.add_tc_font,
                            pady=20)
        add_tc.pack(side=TOP, fill=BOTH, expand=True)
        # Display message when font is added
        self.add_confirm = Label(right_frame)
        self.add_confirm.pack(side=TOP, fill=BOTH, expand=True)

    def change_font(self, event):
        """Change font of char_display widget based on Listbox selection"""
        font = self.font_list.get(ACTIVE)
        self.char_display.config(font=(font, 80))

    def add_sc_font(self):
        """Add selected font to sc_fonts.txt and show confirmation message"""
        font = self.font_list.get(ACTIVE)
        with open('sc_fonts.txt', 'a') as f:
            f.write(font + '\n')
        self.add_confirm.config(text="Added '%s' to sc_fonts.txt" % font)

    def add_tc_font(self):
        """Add selected font to tc_fonts.txt and show confirmation message"""
        font = self.font_list.get(ACTIVE)
        with open('tc_fonts.txt', 'a') as f:
            f.write(font + '\n')
        self.add_confirm.config(text="Added '%s' to tc_fonts.txt" % font)

root = Tk()
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()



