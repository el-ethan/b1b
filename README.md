# b1b 
b1b, *bǐyìbǐ* (比一笔), is a GUI application for comparing Chinese fonts using Python 3 and tkinter.

## Usage:
Run the b1b.py script from the command line or however you usually run your Python scripts, e.g.:

    $ python3 b1b.py

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
