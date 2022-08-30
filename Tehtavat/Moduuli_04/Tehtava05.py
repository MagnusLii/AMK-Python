# Var
username = "python"
password = "rules"
guesses = 0

# Functions
def logincred():
    global username_guess
    global password_guess
    username_guess = input("Syötä käyttäjätunnus: ")
    password_guess = input("Syötä Salasanasi: ")

while True:
    #print("guesses arvo" +str(guesses))    # For troubleshoot.
    if guesses == 5:
        print("Pääsy estetty")
        exit()
    elif password != password_guess:
        guesses = guesses + 1
        logincred()
    elif username != username_guess:
        guesses = guesses + 1
        logincred()
    else:
        print("Tervetuloa!")
        exit()
