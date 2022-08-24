import random


# Var
xcoord = []
ycoord = []
ind = 0
coord_maara = 0
ympyran_sisalla = 0
ympyran_ulkopuolella = 0



# Functions
def randcoord():
    xcoord.append(random.uniform(-1, 1))
    ycoord.append(random.uniform(-1, 1))


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
    if xcoord[ind] ** 2 + ycoord[ind] ** 2 <= 1:
        ind = ind + 1
        ympyran_sisalla = ympyran_sisalla + 1
    else:
        ind = ind + 1
        ympyran_ulkopuolella = ympyran_ulkopuolella + 1


# Calculating pi
try:
    pi_likiarvo = ympyran_sisalla / ympyran_ulkopuolella
    print(pi_likiarvo)
except ZeroDivisionError:
    print("Kaikki pisteet osuivat ympyrän sisälle.")

# Troubleshooting code.

# Testing lists.
#for x in xcoord:
#    print("X coord" + str(xcoord[ind]),end="")
#    print("Y coord" + str(ycoord[ind]))
#    ind = ind + 1