
class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def kiihdyta(cls, speedchange):
        cls.current_speed += int(speedchange)
        if cls.current_speed < 0:
            cls.current_speed = 0
        elif cls.current_speed > cls.top_speed:
            cls.current_speed = cls.top_speed



car1 = Car("ABC-420", 69)


car1.kiihdyta(input("Nopeus muutos: "))
attributes = vars(car1)
print(", ".join("%s: %s" % item for item in attributes.items()))
