#!/usr/bin/env python3
"""
z1z （找一找) is a utility for displaying the fonts installed on your system

When a font in the listbox is selected, pressing return will change the
character display to that the characters are displayed with the selected
font. The purpose of this tool is to find the identify the Chinese fonts
installed on your system so they can be used in the b1b app. Too add a
font to your font list, click one of the Add buttons. A message will
indicate that the font has been added to the list.

Fonts are added to text files sc_fonts.txt and tc_fonts.txt. Text files are
used so that they can be easily viewed and modified manually if necessary.

The value of the char_display widget's text option can be changed if you want
to test fonts for different languages (i.e., you can add Latin characters,
Japanese kana, etc., to see how they look with different fonts).
"""
import shelve
from tkinter import *
import tkinter.font


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
        mid_frame = LabelFrame(self)
        mid_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.fs_name_entry = Entry(mid_frame)
        self.fs_name_entry.pack(side=TOP, fill=BOTH, expand=True)

        self.char_display = Label(mid_frame,
                             text='繁體字\n简体字',
                             font=('', 80),
                             pady=50,
                             padx=50)
        self.char_display.pack(side=TOP, fill=BOTH, expand=True)

        add_fs = Button(mid_frame,
                            text="Add to Font Set",
                            command=self.add_fs)
        add_fs.pack(side=TOP, fill=BOTH, expand=True)

        remove_fs = Button(mid_frame,
                           text="Remove from Font Set",
                           command=self.remove_fs)
        remove_fs.pack(side=TOP, fill=BOTH, expand=True)

        save_fs = Button(mid_frame,
                      text="Done",
                      command=self.save_fs)
        save_fs.pack(side=TOP, fill=BOTH, expand=True)
        # Display message when font is added
        self.add_confirm = Label(mid_frame)
        self.add_confirm.pack(side=TOP, fill=BOTH, expand=True)

        self.right_frame = Frame(self)
        self.right_frame.pack(side=LEFT, fill=BOTH, expand=True)

        Label(self.right_frame,
              text='Font Set',
              font=('', 20),
              bg='cornflower blue').pack(side=TOP, fill=BOTH, expand=True)

        self.font_set = Listbox(self.right_frame,
                                  width=30,
                                  height=20)
        self.font_set.pack(side=TOP, fill=BOTH, expand=True)
        # Populate Listbox widget
        # for font in self.fonts_to_save:
        #     self.font_set.insert(END, font)
        #     self.font_set.bind('<Return>', self.change_font)

    def change_font(self, event):
        """Change font of char_display widget based on Listbox selection"""
        font = self.font_list.get(ACTIVE)
        self.char_display.config(font=(font, 80))

    def add_fs(self):
        """Add selected font to current font set"""
        font = self.font_list.get(ACTIVE)

        self.font_set.insert(END, font)
        self.font_set.bind('<Return>', self.change_font)

    def remove_fs(self):
        """remove selected font from current font set"""
        # font = self.font_list.get(ACTIVE)
        self.font_set.delete(ACTIVE)

    def save_fs(self):
        """
        Save fonts in Listbox to font_sets.db

        The name of the font set is saved as the key
        and the fonts are a set under that key.
        """
        fonts_to_save = self.font_set.get(0, END)
        fs_name = self.fs_name_entry.get()
        with shelve.open('font_sets') as db:
            db[fs_name] = set(fonts_to_save)