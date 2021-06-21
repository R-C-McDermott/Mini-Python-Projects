'''
Password generator GUI using tkinter with practise using OOP

By Ryan C. McDermott
'''

import tkinter as tk
from tkinter import simpledialog
import string
import random

charsPunc = list(string.digits + string.ascii_letters + string.punctuation)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        parent.title("Password Generator")
        parent.geometry("300x150")

        self.gen_button = tk.Button(self, text="Generate password", command=self.generatePassword)
        self.gen_button.pack(side="bottom")

        self.label = tk.Label(parent, text="Input:")
        self.label.pack(side="top")
        self.user_input_box = tk.Entry(self)
        self.user_input_box.pack(side="top")

        self.outputLab = tk.Label(parent, text="Output: ")
        self.outputLab.place(x=125, y=50)
        self.output_text = tk.Text(parent, height=1, width=25)
        self.output_text.place(x=50, y=70)

    # Password generation

    def generatePassword(self):
        password = ''
        size = int(self.user_input_box.get())
        self.output_text.delete("1.0","end")
        self.output_text.insert(1.0, password.join(random.sample(charsPunc, size)))


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
