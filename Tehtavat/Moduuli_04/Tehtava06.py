import random

# Var
xcoord = []                     # Lists for storing all X/Y coordinates.
ycoord = []
ind = 0                         # Var for keeping track of which item were reading on the list.
number_of_entries = 0                 # Variable for storing the number of numbers asked to be generated.
inside_of_circle = 0             # These two are variables used to keep track of the...
outside_of_circle = 0        # ratio of numbers within and outside the circle.

# Functions
def randcoord():
    xcoord.append(round(random.uniform(-1, 1),1))
    ycoord.append(round(random.uniform(-1, 1),1))

# Code
# Number of coordinates generated.
while number_of_entries == 0:
    try:
        number_of_entries = int(input("Montakohan pistettä generoidaan?: "))
    except ValueError:
        print("Syötä kokonaisnumero.")

# Generating coordinates.
for i in range(number_of_entries):
    randcoord()

# Evaluating positions.
for i in range(number_of_entries):
    if (xcoord[ind] ** 2) + (ycoord[ind] ** 2) < 1:
        ind = ind + 1
        inside_of_circle = inside_of_circle + 1
    else:
        outside_of_circle = outside_of_circle + 1
        ind = ind + 1

# Calculating pi
try:
    pi_approx = inside_of_circle / outside_of_circle
    print(pi_approx)
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