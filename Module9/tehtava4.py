import random

class Car:
    def __init__(self, license_plate, maximum_speed, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hour):
        self.travelled_distance += hour * self.current_speed


def race(cars):
    numberone = 0
    while numberone < 10000:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.travelled_distance > numberone:
                numberone = car.travelled_distance
    return cars

cars = [Car("ABC-123", 142), Car("ABC-234", 122)]
cars = race(cars)