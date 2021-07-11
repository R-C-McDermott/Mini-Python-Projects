'''
Password generator GUI using tkinter with practise using OOP

By Ryan C. McDermott
'''

import tkinter as tk
from tkinter import simpledialog
import string
import random

charsPuncNums = list(string.digits + string.ascii_letters + string.punctuation)
charsNums = list(string.digits + string.ascii_letters)
charsPunc = list(string.ascii_letters + string.punctuation)
chars = list(string.ascii_letters)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        parent.title("Password Generator")
        parent.geometry("300x180")


        # Check box to include punctuation or not in password generation
        self.punc = tk.IntVar()
        self.check_box = tk.Checkbutton(parent, text="Include punctuation?", variable=self.punc)
        self.check_box.pack(side="bottom")

        # Check box to include numbers or not in password generation
        self.nums = tk.IntVar()
        self.check_box = tk.Checkbutton(parent, text="Include numbers?", variable=self.nums)
        self.check_box.pack(side="bottom")

        # Text box for user input to give number of characters wanted
        self.label = tk.Label(parent, text="Please enter number of characters:")
        self.label.pack(side="top")
        self.user_input_box = tk.Entry(self)
        self.user_input_box.pack(side="top")

        # Output text box (copyable text) for generated password
        self.outputLab = tk.Label(parent, text="Password: ")
        self.outputLab.place(x=125, y=50)
        self.output_text = tk.Text(parent, height=1, width=25)
        self.output_text.place(x=50, y=70)

        # Button for generating password
        self.gen_button = tk.Button(parent, text="Generate password", command=self.generatePassword)
        self.gen_button.pack(side="bottom")

    # Password generation
    def passwordPuncNums(self):
        password = ''
        size = int(self.user_input_box.get())
        self.output_text.delete("1.0","end")
        self.output_text.insert(1.0, password.join(random.sample(charsPuncNums, size)))

    # Password generation without using punctuation
    def passwordNoPunc(self):
        password = ''
        size = int(self.user_input_box.get())
        self.output_text.delete("1.0","end")
        self.output_text.insert(1.0, password.join(random.sample(charsNums, size)))

    def passwordNoNums(self):
        password = ''
        size = int(self.user_input_box.get())
        self.output_text.delete("1.0","end")
        self.output_text.insert(1.0, password.join(random.sample(charsPunc, size)))

    def passwordNoNumsNoPunc(self):
        password = ''
        size = int(self.user_input_box.get())
        self.output_text.delete("1.0","end")
        self.output_text.insert(1.0, password.join(random.sample(chars, size)))

    def generatePassword(self):
        if self.punc.get() == 1 and self.nums.get() == 1:
            self.passwordPuncNums()
        if self.punc.get() == 0 and self.nums.get() == 0:
            self.passwordNoNumsNoPunc()
        if self.punc.get() == 1 and self.nums.get() == 0:
            self.passwordNoNums()
        if self.punc.get() == 0 and self.nums.get() == 1:
            self.passwordNoPunc()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
