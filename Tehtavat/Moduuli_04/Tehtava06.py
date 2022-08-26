import random


# Var
# potentially a better random num gen.
#numlist =   [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,
#            0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
xcoord = []
ycoord = []
ind = 0
coord_maara = 0
ympyran_sisalla = 0
ympyran_ulkopuolella = 0



# Functions random number gen.
def randcoord():
    xcoord.append(random.uniform(-1, 1))        # favours higher numbers from range.
    ycoord.append(random.uniform(-1, 1))
    #xcoord.append(random.choice(numlist))       # prefers numbers from -0.5 to 0.5
    #ycoord.append(random.choice(numlist))

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
    print("pi-n likiarvo tämän ohjelman mielestään " +str(pi_likiarvo))
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