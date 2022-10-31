
import math

class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speedkmh = 0
        self.distance_traveled = 0

    def speedup(self, speedchange):
        self.current_speedkmh += int(speedchange)
        if self.current_speedkmh < 0:
            self.current_speedkmh = 0
        elif self.current_speedkmh > self.top_speed:
            self.current_speedkmh = self.top_speed

    def travel(self, timehours):
        # math.sqrt and ** so negative speeds don't reduce distance traveled.
        self.distance_traveled += int(timehours * math.sqrt(self.current_speedkmh ** 2))

class Electriccar(Car):
    def __init__(self, registration_number, top_speed, battery):
        self.batterycapacity = battery
        super().__init__(registration_number, top_speed)

class Petrolcar(Car):
    def __init__(self, registration_number, top_speed, gastank):
        self.gastank = gastank
        super().__init__(registration_number, top_speed)



eleccar = Electriccar("ABC-15", 180, 52.5)
petrocar = Petrolcar("ACD-123", 165, 32.3)

eleccar.speedup(69)
petrocar.speedup(350)

eleccar.travel(3)
petrocar.travel(3)

print(eleccar.distance_traveled)
print(petrocar.distance_traveled)