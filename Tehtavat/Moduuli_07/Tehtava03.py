
# TODO: redo lists.
terminal = {} # icao : name


def addterminal(name, icao):
    terminal.update({icao.upper():name})


def fetch(icao):
    print(icao)
    print(terminal[icao])


while True:
    path = int(input("Input 1 to exit.\n"
                    "Input 2 to add new airport.\n"
                    "Input 3 to fetch existing airport.\n"
                    "Input: "))
    if path == 1:
        exit()
    elif path == 2:
        terminal.update({input("Anna lentoaseman ICAO koodi: "):
                         input("Anna lentoaseman nimi: ")})
    elif path == 3:
        try:
            print(terminal[input("Anna haettavan lentoaseman ICAO koodi: ")])
        except KeyError:
            print("404\n"
                  "You're searching beyond the knowledge of this dictionary.")
    else:
        print("1, 2, tai 3.")
