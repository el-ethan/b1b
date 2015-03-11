b1b (比一笔) is a tool for comparing how Chinese characters are represented using different fonts. While certain aspects of characters may change minimally based on font family, sometimes certain components are represented very differently. (A good test of this is to compare the character 寺, sì, using the app, paying attention to how the top portion changes).

This is very much a work in progress, and my first major project using Python and the tkinter module. Constructive feedback is more than welcome!

Notes on usage:

* The app does not currently support MAC OS X Chinese input methods, so you must input text by pasting it if you are on a MAC. 
* Once you have pasted new text into the entry box, click 'Show' to refresh the display. 
* Although you can enter an arbitrarily long string of characters into the entry box, the display will grow too large to be useful with too many characters, so it is best to limit your entry to A MAX OF 4 CHARACTERS at a time.
* You can mix Simplified and Traditional characters in your input if you wish.
* Use the buttons on the top right to customize the display for a particular type of characters. Traditional and Simplified will display together by default.
* Hover the mouse arrow over characters to display their font information in the gray bar below the text entry box.
* Font information is gathered automatically. The Chinese fonts on my version of OS X have either TC (Traditional Chinese) or SC (Simplified Chinese) at the end of their names, and so font information is gathered this way. This means that in order for the app to work on other OSs, you must modify how fonts or collected - or, if you know which Chinese fonts are available on your system, you can add them manually to the TC_fonts and SC_fonts lists in the script.
* The number of fonts affects the size of the display, and you may also see some blank cells depending on the number of fonts.

