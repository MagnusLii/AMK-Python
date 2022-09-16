
class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

car1 = Car("ABC-420", 69)

attributes = vars(car1)
print(", ".join("%s: %s" % item for item in attributes.items()))
