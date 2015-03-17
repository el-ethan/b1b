"""
font_find is a utility for displaying the fonts installed on your system

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
from tkinter import *
import tkinter.font


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.all_fonts = tkinter.font.families()
        self.build_widgets()

    def build_widgets(self):
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