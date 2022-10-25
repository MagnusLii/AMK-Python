import math
import random

# vars
hourofrace = 0

class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speedkmh = 0
        self.distance_traveled = 0

    def kiihdyta(self, speedchange):
        self.current_speedkmh += int(speedchange)
        if self.current_speedkmh < 0:
            self.current_speedkmh = 0
        elif self.current_speedkmh > self.top_speed:
            self.current_speedkmh = self.top_speed

    def travel(self, timehours):
        # math.sqrt and ** so negative speeds don't reduce distance traveled.
        self.distance_traveled += int(timehours * math.sqrt(self.current_speedkmh ** 2))

class Competition:
    def __init__(self, racename, distance, listofcarsss):
        self.name = racename
        self.distance = distance
        self.carlist = listofcarsss

    def hourpasses(self):
        global hourofrace
        for car in self.carlist:
            car.kiihdyta(random.randint(-10, 15))
            car.travel(1)
        hourofrace += 1

    def printsit(self):
        for i in cars:
            attributes = vars(i)
            print(", ".join("%s: %s" % item for item in attributes.items()))
        print("--------------------------------------------------------------------------------------")

    def raceover(self, carid):
        if carid.distance_traveled >= self.distance:
            print(f"{car.registration_number} has won the race, the race lasted {hourofrace} hours.")
            return True

cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))
comp = Competition("Suuri romuralli", 8000, cars)
someonewon = None

while not someonewon:
    for hours in range(10):
        comp.hourpasses()
        for car in comp.carlist:
            someonewon = comp.raceover(car)
            if someonewon:
                comp.printsit()
                exit()
    comp.printsit()
