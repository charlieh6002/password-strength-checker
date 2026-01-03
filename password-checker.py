#---IMPORTS----

import tkinter as tk
from tkinter import *
from tkinter import font
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

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 1200
window_height = 800
window_x = int((screen_width - window_width)/2)
window_y = int((screen_height - window_height)/2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.configure(background = "light grey")

#background and graphics
frame = tk.Frame(window, width = window_width, height = window_height)
frame.configure(background = "black")
frame.pack(padx = 10, pady = 10)

entry_frame = tk.Frame(window, width = 200, height = 45)
entry_frame.configure(background = "white")
entry_frame.pack(padx = 10, pady = 10)

large_pixeboy_font = font.Font(family = "Pixeboy", size = 50)
medium_pixeboy_font = font.Font(family = "Pixeboy", size = 40)
small_pixeboy_font = font.Font(family = "Pixeboy", size = 30)

Label(window, text = "Password Strength Checker", font = large_pixeboy_font, background = "black").place(relx = 0.5, rely = 0.05, anchor = 'n')

Label(window, text = "passwords should:", font = medium_pixeboy_font, background = "black").place(relx = 0.05, rely = 0.175, anchor = 'nw')

Label(window, text = "be at least 8 characters in length", font = small_pixeboy_font, background = "black").place(relx = 0.05, rely = 0.25, anchor = 'nw')
Label(window, text = "contain at least 1 uppercase and lowercase character", font = small_pixeboy_font, background = "black").place(relx = 0.05, rely = 0.3, anchor = 'nw')
Label(window, text = "contain at least 1 number", font = small_pixeboy_font, background = "black").place(relx = 0.05, rely = 0.35, anchor = 'nw')
Label(window, text = "contain at least 1 special character", font = small_pixeboy_font, background = "black").place(relx = 0.05, rely = 0.4, anchor = 'nw')

#text entry

Label(window, text = "Password: ", font = small_pixeboy_font, background = "black").place(relx = 0.05, rely = 0.5, anchor = "nw")
password_entry = Entry(window, show = "*", fg = "black", bg = "white", width = 100, text = "Password:").place(relx = 0.2, rely = 0.55, anchor = "nw")

window.mainloop()
#----MAIN-LOOP----

#while run:
 #   user_password = input("enter password: ")
  #  print(checker.check(user_password))
   # user_input = input("continue? y/n? ")
    #if user_input.lower() == "n":
     #   print("quitting...")
      #  run = False
