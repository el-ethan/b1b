# b1b

b1b (比一笔) is a tool for comparing how Chinese characters are represented using different fonts. While certain aspects of characters may change minimally based on font family, sometimes certain components are represented very differently. (A good test of this is to compare the character 寺, sì, using the app, paying attention to how the top portion changes).

This is very much a work in progress, and my first major project using Python and the tkinter module. Constructive feedback is more than welcome!

## A few notes on operation:

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
the gray bar below the text entry box.

# z1z 

z1z (找一找) is a tool to find fonts on your system to use with b1b. Fonts selected in this app can be automatically sent to files that can be used to populate font lists in b1b.


