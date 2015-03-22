#!/usr/bin/env python3
"""
This module includes a Toplevel widget that allows you to pick and save fonts

When a font in the listbox is selected, pressing return will change the
character display so that the characters are displayed with the selected
font. The purpose of this tool is to identify the Chinese fonts installed
on your system so they can be used in the b1b app. The user will be prompted
to set their first font set if the start b1b with no previously saved sets.
After that, the font picker can be accessed at anytime from the b1b File
menu.

Font sets are saved using the Python shelve module in a database where they
are stored as key-value pairs with the key being the name of the font set,
and the value being a set (in the Python sense) of the fonts in that font set.
"""
import shelve
from tkinter import *
from tkinter.messagebox import showwarning
import tkinter.font
# TODO: update documentation

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

        self.fs_name_entry = Entry(mid_frame, fg='gray')
        self.fs_name_entry.pack(side=TOP, fill=BOTH, expand=True)
        self.name_entry_prompt = "Enter a name for this font set here:"
        self.fs_name_entry.insert('0', self.name_entry_prompt)
        self.fs_name_entry.bind('<Button-1>', self.clear_entry)

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

    def change_font(self, event):
        """Change font of char_display widget based on Listbox selection"""
        font = self.font_list.get(ACTIVE)
        self.char_display.config(font=(font, 80))

    def clear_entry(self, event):
        """Clear fs_name_entry when clicked, and change font color"""
        self.fs_name_entry.delete(0, END)
        self.fs_name_entry.config(fg='black')

    def add_fs(self):
        """Add selected font to current font set"""
        font = self.font_list.get(ACTIVE)
        self.font_set.insert(END, font)
        self.font_set.bind('<Return>', self.change_font)

    def remove_fs(self):
        """remove selected font from current font set"""
        self.font_set.delete(ACTIVE)

    def save_fs(self):
        """
        Save fonts in Listbox to font_sets.db

        The name of the font set is saved as the key
        and the fonts are a set under that key.
        """
        fonts_to_save = self.font_set.get(0, END)
        fs_name = self.fs_name_entry.get()
        # Show warning if default name hasn't changed or no name is defined
        if fs_name == self.name_entry_prompt or not fs_name:
            showwarning("Name of Font Set Not Specified",
                        "Please enter a name for this font set",
                        default='ok')
        else:
            with shelve.open('font_sets') as db:
                db[fs_name] = set(fonts_to_save)
                self.destroy()