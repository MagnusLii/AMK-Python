
terminal = {} # icao : name

while True:
    path = int(input("Input 1 to exit.\n"
                    "Input 2 to add new airport.\n"
                    "Input 3 to fetch existing airport.\n"
                    "Input: "))
    if path == 1:
        exit()
    elif path == 2:
        terminal.update({input("Anna lentoaseman ICAO koodi: ").upper():
                         input("Anna lentoaseman nimi: ")})
    elif path == 3:
        try:
            print(terminal[input("Anna haettavan lentoaseman ICAO koodi: ").upper()])
        except KeyError:
            print("404\n"
                  "You're searching beyond the knowledge of this dictionary.")
    else:
        print("1, 2, tai 3.")
