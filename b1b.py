#!/usr/bin/env python3
"""
# b1b (比一笔）is a GUI application for comparing Chinese fonts.

## Usage:

### Font Sets

When you run the b1b.py script for the first time, the font picker app
will run, prompting you to define your first font set. This set will be
used as the default font set. Font sets are lists of font names that will
be used to display whatever characters you enter into the b1b app.

    * You can save multiple sets, and access them from the Font Sets menu.
    * The font picker can be accessed at any time from the File menu.
    * You can delete all your font sets using the 'Clear All Font Sets'
    option from the File menu.

### b1b

When you run the main app you will see the characters '比一笔' (the Chinese
name of the app) displayed using all of the fonts in the default font list
(the first list you defined from the font picker).

Once you enter new characters in the text entry region and press 'Show', the
display will update to show the new characters.

    * Currently, you can only display a max of 4 characters. All characters
    after 4 will be truncated, and the first 4 will be displayed. This is to
    preserve the readability of the display, but I intend to change this so
    that arbitrarily long strings can be displayed.
    * Because of a known issue with tkinter, the app does not work with the
    default Chinese input method on OSX, therefore characters must be pasted
    into the app if you are on a Mac. You should be able to type characters
    directly into the app on Windows (tested on Win 7) and Ubuntu (tested on
    Ubuntu 14.04).
    * You can mix Simplified and Traditional characters in your input if you
    wish. However, keep in mind that some characters may not display
    properly in fonts meant specifically for SC or TC, and will default
    to some other font, probably heiti.
    * Hover the mouse arrow over characters to display their font information
    in the blue bar below the text entry box.
"""
# TODO: don't name widgets that don't need it.
# TODO: Add command to delete only current font set
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

if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    app = Application(master=root)
    app.mainloop()