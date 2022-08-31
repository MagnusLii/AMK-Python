import random

# Var
xcoord = []                 # Lists for storing all X/Y coordinates.
ycoord = []
ind = 0                     # Var for keeping track of which item were reading on the list.
number_of_entries = 0       # Variable for storing the number of numbers asked to be generated.
inside_of_circle = 0        # These two are variables used to keep track of the...
outside_of_circle = 0       # ratio of numbers within and outside the circle.

# Code
# Number of coordinates generated.
while number_of_entries == 0:
    try:
        number_of_entries = int(input("Montakohan pistettä generoidaan?: "))
    except ValueError:
        print("Syötä kokonaisnumero.")

# Generating coordinates.
for i in range(number_of_entries):
    xcoord.append(round(random.uniform(-1.003, 1.001), 1))
    ycoord.append(round(random.uniform(-1.003, 1.001), 1))

# Evaluating positions.
for i in range(number_of_entries):
    if (xcoord[ind] ** 2) + (ycoord[ind] ** 2) < 1:
        inside_of_circle += 1
        ind += 1
    else:
        outside_of_circle += 1
        ind += 1

# Calculating pi
try:
    print(inside_of_circle / outside_of_circle)
except ZeroDivisionError:
    print("Kaikki pisteet osuivat ympyrän sisälle.")