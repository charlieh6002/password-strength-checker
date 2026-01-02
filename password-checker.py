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
window.title("Password Strength Checker")

screen_width = window.winfo_width()
screen_height = window.winfo_height()
window_width = 800
window_height = 600
window_x = int(screen_width/2 - window_width/2)
window_y = int(screen_height/2 - window_height/2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

Label(window, text = "Password Strength Checker").grid(row = 2)
Label(window, text = "passwords should:").grid(row = 4)
Label(window, text = "be at least 8 characters in length").grid(row = 5)
Label(window, text = "contain at least 1 uppercase and lowercase character").grid(row = 6)
Label(window, text = "contain at least 1 number").grid(row = 7)
Label(window, text = "contain at least 1 special character").grid(row = 8)


window.mainloop()
#----MAIN-LOOP----

while run:
    user_password = input("enter password: ")
    print(checker.check(user_password))
    user_input = input("continue? y/n? ")
    if user_input.lower() == "n":
        print("quitting...")
        run = False
