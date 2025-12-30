#password-checker.py

class Checker():
    
    def __init__(self):
        pass

    def check(self):
        pass

#main loop

run = True
checker = Checker()

while run:
    user_password = input("enter password: ")
    print(checker.check(user_password))
    user_input = input("continue? y/n?")
    if user_input.lower() == "n":
        print("quitting...")
        run = False
