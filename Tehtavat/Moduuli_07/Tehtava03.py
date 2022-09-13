terminal_ICAO = []
terminal_names = []


def exit1():
    print("Well, here at last, dear friends, \n"
          "on the edge of our code comes the end. \n"
          "Go in peace! Do not not weep for not \n"
          "all years are an evil.")
    exit()


def addterminal():
    terminal_names.append(input("Anna lentoaseman nimi: "))
    terminal_ICAO.append(input("Anna lentoaseman ICAO koodi: "))


def fetch():
    lookup = input("Anna haettavan lentoaseman ICAO koodi: ")
    try:
        lookup = terminal_ICAO.index(lookup.upper())
        print(f"Lentokentän nimi on {terminal_names[lookup]}")
    except ValueError:
        print("ICAO koodia ei löytynyt.")


while True:
    try:
        path = int(input("Input 1 to exit.\n"
                         "Input 2 to add new airport.\n"
                         "Input 3 to fetch existing airport.\n"
                         "Input: "))
    except ValueError:
        print("1, 2, tai 3.")
        continue
    if path == 1:
        exit1()
    elif path == 2:
        addterminal()
    elif path == 3:
        fetch()
