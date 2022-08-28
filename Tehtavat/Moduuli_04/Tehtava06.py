import random


# Var
xcoord = []                     # List for storing all X coordinates.
ycoord = []                     # ^^ Same but for Y coords.
ind = 0                         # Var for keeping track of which item were reading on the list.
coord_maara = 0                 # Variable for storing the number of numbers asked to be generated.
ympyran_sisalla = 0             # These two are variables used to keep track of the...
ympyran_ulkopuolella = 0        # ratio of numbers within and outside the circle.


# Functions
def randcoord():
    xcoord.append(round(random.uniform(-1, 1),1))
    ycoord.append(round(random.uniform(-1, 1),1))


# Code
# Number of coordinates generated.
while coord_maara == 0:
    try:
        coord_maara = int(input("Montakohan pistettä generoidaan?: "))
    except ValueError:
        print("Syötä kokonaisnumero.")


# Generating coordinates.
for i in range(coord_maara):
    randcoord()


# Evaluating positions.
for i in range(coord_maara):
    if (xcoord[ind] ** 2) + (ycoord[ind] ** 2) < 1:
        ind = ind + 1
        ympyran_sisalla = ympyran_sisalla + 1
    else:
        ympyran_ulkopuolella = ympyran_ulkopuolella + 1
        ind = ind + 1


# Calculating pi
try:
    pi_likiarvo = ympyran_sisalla / ympyran_ulkopuolella
    print(pi_likiarvo)
except ZeroDivisionError:
    print("Kaikki pisteet osuivat ympyrän sisälle.")

# Troubleshooting code.

# Screening end results
#print(ympyran_ulkopuolella)
#print(ympyran_sisalla)

# Testing lists.
#for x in xcoord:
#    print("X coord" + str(xcoord[ind]),end="")
#    print("Y coord" + str(ycoord[ind]))
#    ind = ind + 1