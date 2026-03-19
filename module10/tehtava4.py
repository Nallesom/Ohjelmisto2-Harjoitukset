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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"Car: {car.license_plate}")
            print(f"Maximum speed: {car.maximum_speed}")
            print(f"Current speed: {car.current_speed}")
            print(f"Travelled distance: {car.travelled_distance}")

    def race_finished(self):
        numberOne = 0
        for car in self.cars:
            if car.travelled_distance > numberOne:
                numberOne = car.travelled_distance

        if numberOne >= self.distance:
            return True
        else:
            return False