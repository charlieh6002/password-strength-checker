#password-checker.py

class Checker():
    
    def __init__(self):
        self.special_characters = ["!","@","£","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",":",";","","'","|",",","<",".",">","?","/","±","€","~","`"]

    def check(self):
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

#main loop

run = True
checker = Checker()
print("passwords should: ")
print("be at least 8 characters in length")
print("contain at least 1 uppercase and lowercase character")
print("contain at least 1 number")
print("contain at least 1 special character")

while run:
    user_password = input("enter password: ")
    print(checker.check(user_password))
    user_input = input("continue? y/n?")
    if user_input.lower() == "n":
        print("quitting...")
        run = False
