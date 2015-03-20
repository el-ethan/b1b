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
# TODO: don't name widgets that don't need it.
import re
import math
import shelve
import os
from tkinter import *
import tkinter.font
from tkinter.messagebox import showwarning, askokcancel
from z1z import FontPicker

class Application(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)
        ###### Menu bar ######
        menu = Menu(root)
        root.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Font Picker",
                              command=self.open_font_picker)
        file_menu.add_command(label="Clear All Lists",
                              command=self.clear_lists)

        fs_menu = Menu(menu)
        menu.add_cascade(label="Font Sets", menu=fs_menu)


        db = shelve.open('font_sets')
        for k in db.keys():
            fs_menu.add_radiobutton(label=k,
                                         command=lambda k=k : self.ref_set(k))
        db.close()
        ###### Default font set ######
        fs = fs_menu.entrycget(0, 'label')
        with shelve.open('font_sets') as db:
            self.current_fs = db[fs]
        ###### Draw widgets ######
        self.draw_widgets()
        self.draw_fnt_disp(self.current_fs)

    def open_font_picker(self):
        """Open font picker and update b1b display once picker is closed"""
        w = FontPicker()
        w.wait_window(w)
        self.refresh_disp()

    def ref_set(self, fs_name):
        self.display_frame.destroy()
        with shelve.open('font_sets') as db:
            new_fonts = db[fs_name]
        self.current_fs = new_fonts
        self.draw_fnt_disp(new_fonts)


    def draw_widgets(self):
        """Draw widgets for main app"""

        top_frame = Frame(self)
        top_frame.pack(side=TOP, fill=BOTH, expand=True)

        top_right_frame = Frame(top_frame, padx=10)
        top_right_frame.pack(side=RIGHT)

        top_left_frame = Frame(top_frame, padx=10)
        self.char_entry = Entry(top_left_frame)
        self.char_entry.insert('0', '比一笔')
        self.char_entry.pack(side=TOP, fill=BOTH, expand=True)
        show_b = Button(top_left_frame,
                        text='Show',
                        command=self.refresh_disp)
        quit_b = Button(top_left_frame, text='Quit', command=self.quit)
        top_left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        show_b.pack(side=LEFT, fill=BOTH, expand=True)
        quit_b.pack(side=LEFT, fill=BOTH, expand=True)

        self.font_info = Label(self,
                               text='font info',
                               bg='cornflower blue',
                               relief=SUNKEN)
        self.font_info.pack(side=TOP, fill=BOTH, expand=True)

    def refresh_disp(self):
        self.display_frame.destroy()
        self.draw_fnt_disp(self.current_fs)

    def draw_fnt_disp(self, font_set):
        """Set font display area"""
        chars = self.char_entry.get()

        if len(chars) > 4:
            showwarning("Too many characters!",
                        "Input too long, trimmed to 4 characters",
                        default='ok')
            chars = chars[:4]
            self.char_entry.delete(4, END)
        # TODO: come up with better way to refresh display. If there is one...
        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)

        height = math.ceil(len(font_set) / 4)
        width = 4
        fonts = self.font_gen(font_set)
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

    # def select_fs(self):
    #     """Select and set correct font set"""
    #     selected_set = fs_menu.entrycget(0, 'label')
    #     with shelve.open('font_sets') as db:
    #         char_set = db[selected_set]
    #         # print(char_set)
    #     return char_set

    def font_gen(self, font_set):
        """Generate fonts for labels in display"""
        for font in font_set:
            yield font.strip()

    def show_font_info(self, event):
        """Generate text for font info display"""
        name = event.widget.cget('font')
        name = re.sub('[{}(55)]', '', name)
        self.font_info.config(text=name)

    def clear_lists(self):
        if (askokcancel("WARNING!",
                        "Are you sure you want to clear all lists?"
                        "\nThis action cannot be undone.",
                        default='cancel')):
            shelves = ['tc_fonts', 'sc_fonts']
            for shelf in shelves:
                with shelve.open(shelf) as db:
                    db.clear()
        self.refresh_disp()

root = Tk()
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()



