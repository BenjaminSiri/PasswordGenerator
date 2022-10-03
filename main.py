# Ben Siri 9-23-22

import random
import pyperclip
from tkinter import *


# First commit


class PasswordGenerator:
    def __init__(self, length, includeLowerCase, includeUpperCase, includeNumbers, includeSpecialChar):
        self.length = length
        self.includeLowerCase = includeLowerCase
        self.includeUpperCase = includeUpperCase
        self.includeNumbers = includeNumbers
        self.includeSpecialChar = includeSpecialChar
        self.numberSet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
        self.letterSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.upperLetterSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.specialCharSet = ['!', '@', '#', '$', '%', '^', '&', '*']

    def generate(self):
        charSet = []
        final = []
        y = self.length
        if self.includeLowerCase:
            charSet = charSet + self.letterSet
        if self.includeUpperCase:
            charSet = charSet + self.upperLetterSet
        if self.includeNumbers:
            charSet = charSet + self.numberSet
        if self.includeSpecialChar:
            charSet = charSet + self.specialCharSet

        x = 0
        while x < y:
            final = final + [random.choice(charSet)]
            x += 1
        return "".join(final)


# Gui code below

root = Tk()
root.title("Password generator")
root.geometry("400x400")


def set_text(entry, text):
    out.configure(state=NORMAL)
    entry.delete(0, END)
    entry.insert(0, text)
    out.configure(state=DISABLED)


def build():
    a = PasswordGenerator(numberSlider.get(), lower.get(), upper.get(), number.get(), special.get())
    set_text(out, a.generate())


def copy():
    pyperclip.copy(out.get())

# Check boxes
number = BooleanVar()
lower = BooleanVar()
upper = BooleanVar()
special = BooleanVar()

numberCheckBox = Checkbutton(root, text="Include Numbers", variable=number, onvalue=True, offvalue=False)
numberCheckBox.select()
lowerCheckBox = Checkbutton(root, text="Include Lower Case Letters", variable=lower, onvalue=True, offvalue=False)
lowerCheckBox.select()
upperCheckBox = Checkbutton(root, text="Include Upper Case Letters", variable=upper, onvalue=True, offvalue=False)
upperCheckBox.select()
specialCheckBox = Checkbutton(root, text="Include Special Characters", variable=special, onvalue=True, offvalue=False)
specialCheckBox.select()

numberCheckBox.grid(row=2, column=0, sticky=W)
lowerCheckBox.grid(row=3, column=0, sticky=W)
upperCheckBox.grid(row=4, column=0, sticky=W)
specialCheckBox.grid(row=5, column=0, sticky=W)

#Number Slider
numberSlider = Scale(root, from_=4, to=20, orient=HORIZONTAL)
numberSlider.grid(row=1, column=0)

#Output Entry
out = Entry(root, width=20, state=DISABLED)
out.grid(row=0, column=0)

#Generate Button
generateButton = Button(root, text="Generate!", command=build)
generateButton.grid(row=0, column=1)

#Copy Button
copyButton = Button(root, text="Copy to Clipboard", command=copy)
copyButton.grid(row=1, column=1, stick=W)

root.mainloop()
