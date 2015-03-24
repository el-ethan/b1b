#!/usr/bin/env python3
"""
b1b, *bǐyìbǐ* (比一笔), is a GUI application for comparing Chinese fonts using
Python 3 and tkinter
"""
# TODO: Add command to delete only current font set
# TODO: Get rid of tearoff menus
# TODO: Fix display resize issue when fewer than 3 chars are shown with
# welcome message
# TODO: Allow multiple selections in font picker
# TODO: Add warning that fonts in default set might not
# be what they appear
import re
import math
import shelve
import sys
from tkinter import *
import tkinter.font
from tkinter.messagebox import showwarning, askokcancel

# Sample font sets which can be used if no user sets defined
osx_fonts = ['Heiti SC', 'Kaiti SC', 'Songti SC']
win7_fonts = ['SimHei', 'KaiTi', 'SimSun']

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
                             command=self.open_picker)
        filemenu.add_command(label="Delete All User Font Sets",
                             command=self.clear_sets)
        fs_menu = Menu(menu)
        menu.add_cascade(label="Font Sets", menu=fs_menu)
        # Add sample font sets
        self.fs_var = StringVar()

        fs_menu.add_radiobutton(label="Sample Font Set (OS X)",
                                variable=self.fs_var,
                                value="Sample Font Set (OS X)",
                                command=self.refresh_fs)
        fs_menu.add_radiobutton(label="Sample Font Set (Windows)",
                                variable=self.fs_var,
                                value="Sample Font Set (Windows)",
                                command=self.refresh_fs)

        # Welcome message to display if not user defined font sets present
        msg = ("\n欢迎你! You have not defined your own font sets yet. "
               "To define a custom font set, \nselect Open Font Picker "
               "from the File Menu, pick some fonts, then name and "
               "save \nyour list! The first list you define will be the "
               "default list when you run b1b. Enjoy!\n")
        # Add radio button to menu for each key in font sets database
        db = shelve.open('font_sets')
        self.welcome_lbl = Label(self,
                            text=msg,
                            justify=LEFT,
                            padx=30,
                            font=('Avenir', 18))
        if not db and sys.platform == 'darwin':
            self.fs_var.set("Sample Font Set (OS X)")
            self.current_fs = osx_fonts
            self.welcome_lbl.pack(side=BOTTOM, fill=BOTH, expand=True)
        elif not db:
            # Default to Windows fonts if not on Mac
            # The Win fonts seem to work on Ubuntu as well, but don't all show
            # up in font picker...
            self.fs_var.set("Sample Font Set (Windows)")
            self.current_fs = win7_fonts
            self.welcome_lbl.pack(side=BOTTOM, fill=BOTH, expand=True)
        else:
            for fs in sorted(db.keys()):
                fs_menu.add_radiobutton(label=fs,
                                        variable=self.fs_var,
                                        value=fs,
                                        command=self.refresh_fs)
            db.close()
            # Set default font set
            with shelve.open('font_sets') as db:
                keys = [key for key in db.keys()]
                default_fs = sorted(keys)[0]
                # Set font set to first in A-Z sorted list of font sets
                self.fs_var.set(default_fs)
                self.current_fs = db[default_fs]

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
        self.default_msg = ("Hover mouse arrow over characters to "
                            "display font info")
        self.font_info = Label(self,
                               text=self.default_msg,
                               bg='cornflower blue',
                               relief=SUNKEN,
                               padx=30)
        self.font_info.pack(side=TOP, fill=BOTH, expand=True)

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
                              text=chars,
                              font=(next(fonts), fontsize),
                              padx=30,
                              pady=10)
                        L.bind('<Enter>', self.show_font_info)
                        L.grid(row=r, column=c, sticky=N+E+S+W)
        except StopIteration:
            pass

    def open_picker(self):
        """Open font picker and update b1b display once picker is closed"""
        self.welcome_lbl.destroy()
        w = FontPicker()
        w.wait_window(w)
        self.draw_menu_bar()
        # TODO: fix it without exception handling
        try:
            self.refresh_disp()
        except AttributeError:
            pass

    def refresh_fs(self):
        """Update current font set and redraw character display"""
        self.display_frame.destroy()
        fs_name = self.fs_var.get()
        if fs_name == "Sample Font Set (OS X)":
            new_fonts = osx_fonts
        elif fs_name == "Sample Font Set (Windows)":
            new_fonts = win7_fonts
        else:
            with shelve.open('font_sets') as db:
                new_fonts = db[fs_name]
        # Update current font set
        self.current_fs = new_fonts
        self.draw_char_disp(new_fonts)

    def refresh_disp(self):
        """Update character display with current font set"""
        self.display_frame.destroy()
        self.draw_char_disp(self.current_fs)

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

    def clear_sets(self):
        """Clear all user defined font sets"""
        db = shelve.open('font_sets')
        if not db:
            showwarning(None,
                        "You don't have any font sets to delete",
                        default='ok')
            return
        if (askokcancel("WARNING!",
                        "Are you sure you want to delete all sets?"
                        "\nThis action cannot be undone.",
                        default='cancel')):
            with shelve.open('font_sets') as db:
                db.clear()
            self.draw_menu_bar()
            self.refresh_disp()

class FontPicker(Toplevel):
    """A font picker application called from within b1b"""
    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        self.all_fonts = tkinter.font.families()
        self.draw_widgets()

    def draw_widgets(self):
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

        mid_frame = LabelFrame(self)
        mid_frame.pack(side=LEFT, fill=BOTH, expand=True)
        Label(mid_frame,
              text='Press Return to display selected font',
              font=('Avenir', 18),
              pady=20).pack(side=BOTTOM)

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
                      text="Save Font Set",
                      command=self.save_fs)
        save_fs.pack(side=TOP, fill=BOTH, expand=True)

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

    def quit_picker(self):
        self.distroy()

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
        # Show warning if default name hasn't changed or no name is specified
        if not fonts_to_save:
            showwarning("No Fonts Specified",
                        "Please add fonts to your set before saving",
                        default='ok')
        elif fs_name == self.name_entry_prompt or not fs_name:
            showwarning("Name of Font Set Not Specified",
                        "Please enter a name for this font set",
                        default='ok')
        else:
            with shelve.open('font_sets') as db:
                db[fs_name] = set(fonts_to_save)
                self.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title('b1b')
    root.resizable(0, 0)
    app = Application(master=root)
    app.mainloop()