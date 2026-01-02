#---IMPORTS----

import tkinter as tk
from tkinter import *

#----CHECKER CLASS----

class Checker():
    
    def __init__(self):
        self.special_characters = ["!","@","£","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",":",";","","'","|",",","<",".",">","?","/","±","€","~","`"]

    def check(self, user_password):
        length = False
        upper = False
        lower = False
        number = False
        special = False
        invalid_character = ""

        if len(user_password) >= 8:
            length = True

        for c in user_password:
            if c.isupper():
                upper = True
            elif c.islower():
                lower = True
            elif c.isnumeric():
                number = True
            #use set of special characters
            else:
                if c in self.special_characters:
                    special = True
                else:
                    invalid_character = c
        if invalid_character != "":
            return ("you have entered an invalid character, " + invalid_character)
        
        elif length and upper and lower and number and special:
            return ("strong password")

        else:
            return ("weak password")


#----INITIALISING----

run = True
checker = Checker()
window = tk.Tk()

i1 = Label(window, text = "Password Strength Checker")
i2 = Label(window, text = "passwords should:")
i3 = Label(window, text = "be at least 8 characters in length")
i4 = Label(window, text = "contain at least 1 uppercase and lowercase character")
i5 = Label(window, text = "contain at least 1 number")
i6 = Label(window, text = "contain at least 1 special character")

i1.pack()
i2.pack()
i3.pack()
i4.pack()
i5.pack()
i6.pack()

window.mainloop()
#----MAIN-LOOP----

while run:
    user_password = input("enter password: ")
    print(checker.check(user_password))
    user_input = input("continue? y/n? ")
    if user_input.lower() == "n":
        print("quitting...")
        run = False
