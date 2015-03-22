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
# TODO: Add main(), list comprehensions
# TODO: Add command to delete only current font set
# TODO: Update docstring
import re
import math
import shelve
from tkinter import *
import tkinter.font
from tkinter.messagebox import showwarning, askokcancel
from z1z import FontPicker

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)
        self.draw_menu_bar()
        self.draw_widgets()
        self.draw_char_disp(self.current_fs)

    def draw_menu_bar(self):
        """Add file menu and font set menu"""
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open Font Picker",
                             command=self.open_font_picker)
        filemenu.add_command(label="Clear All Font Sets",
                             command=self.clear_lists)
        self.fs_menu = Menu(menu)
        menu.add_cascade(label="Font Sets", menu=self.fs_menu)
        # Add radio button to menu for each key in font sets database
        db = shelve.open('font_sets')
        for k in db.keys():
            self.fs_menu.add_radiobutton(label=k,
                                    command=lambda k=k : self.refresh_fs(k))
        db.close()
        # Set default font set
        default_fs = self.fs_menu.entrycget(0, 'label')
        if not default_fs:
            self.open_font_picker()

        with shelve.open('font_sets') as db:
            keys = [key for key in db.keys()]
            default_fs = keys[0]
            self.current_fs = db[default_fs]

    def open_font_picker(self):
        """Open font picker and update b1b display once picker is closed"""
        w = FontPicker()
        w.wait_window(w)
        self.draw_menu_bar()
        # TODO: fix it without exception handling
        try:
            self.refresh_disp()
        except AttributeError:
            pass

    def refresh_fs(self, fs_name):
        """Update current font set and redraw character display"""
        self.display_frame.destroy()
        with shelve.open('font_sets') as db:
            new_fonts = db[fs_name]
        root.title(fs_name)
        self.current_fs_name = fs_name
        # Update current font set
        self.current_fs = new_fonts
        self.draw_char_disp(new_fonts)


    def draw_widgets(self):
        """Draw operation widgets (buttons, entry) in app top section"""
        # TODO: get rid of top_frame or top_left_frame
        top_frame = Frame(self)
        top_frame.pack(side=TOP, fill=BOTH, expand=True)

        top_left_frame = Frame(top_frame, padx=10)
        top_left_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.char_entry = Entry(top_left_frame)
        self.char_entry.insert('0', '比一笔')
        self.char_entry.pack(side=TOP, fill=BOTH, expand=True)

        # TODO: Get rid of buttons, figure out better way to refresh display
        show = Button(top_left_frame, text='Show',command=self.refresh_disp)
        quit = Button(top_left_frame, text='Quit', command=self.quit)
        show.pack(side=LEFT, fill=BOTH, expand=True)
        quit.pack(side=LEFT, fill=BOTH, expand=True)

        self.font_info = Label(self,
                               text='font info',
                               bg='cornflower blue',
                               relief=SUNKEN)
        self.font_info.pack(side=TOP, fill=BOTH, expand=True)

    def refresh_disp(self):
        self.display_frame.destroy()
        self.draw_char_disp(self.current_fs)
        print(self.current_fs)

    def draw_char_disp(self, font_set):
        """Set font display area"""
        chars = self.char_entry.get()
        # TODO: find better way to control window size
        if len(chars) > 4:
            showwarning("Too many characters!",
                        "Input too long, trimmed to 4 characters",
                        default='ok')
            chars = chars[:4]
            self.char_entry.delete(4, END)

        self.display_frame = LabelFrame(self)
        self.display_frame.pack(side=TOP, fill=BOTH, expand=True)


        width = 4
        height = math.ceil(len(font_set) / width)
        fonts = self.gen_font(font_set)
        fontsize = 60
        try:
            for r in range(height):
                for c in range(width):

                        L = Label(self.display_frame,
                              text=chars, relief=RIDGE,
                              font=(next(fonts), fontsize),
                              padx=30,
                              pady=10)
                        L.bind("<Enter>", self.show_font_info)
                        L.grid(row=r, column=c, sticky=N+E+S+W)
        except StopIteration:
            pass

    def gen_font(self, font_set):
        """Generate fonts for labels in display"""
        for font in font_set:
            yield font

    def show_font_info(self, event):
        """Configure font info display"""
        name = event.widget.cget('font')
        # Remove braces and size from font info
        name = re.sub('[{}\d]', '', name)
        self.font_info.config(text=name)

    def clear_lists(self):
        if (askokcancel("WARNING!",
                        "Are you sure you want to clear all lists?"
                        "\nThis action cannot be undone.",
                        default='cancel')):
            with shelve.open('font_sets') as db:
                db.clear()
            self.refresh_disp()
            self.fs_menu.delete(0, END)

root = Tk()
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()



