import random
class Car:
    def __init__(self, license_number, top_speed):
        self.license_number = license_number
        self.top_speed = top_speed
        self.speed = 0
        self.travel_distance = 0
        self.travel_hours = 0
    def info(self):
        print("Auton rekisteri numero", self.license_number, ","
              , self.top_speed,"km/h maksiminopeus,", self.speed,"km/h nopeus,", self.travel_distance, "km kuljettu matka", self.travel_hours, "tuntia ajettu")
    def accelerate(self, amount):
        if 0 < self.speed + amount < self.top_speed:
            self.speed = self.speed + amount
        elif self.speed + amount <= 0:
            self.speed = 0
        else:
            self.speed = self.top_speed
    def traveling(self, amount):
        self.travel_distance = self.travel_distance + (self.speed * amount)
        self.travel_hours = self.travel_hours + amount

def car_making():
    cars = []
    for i in range (10):
        cars.append(Car("a-"+ str(i), 50))
    #for car in cars:
        #print(car.info())
    return cars


cars = car_making()
race_length = 10000

for car in cars:
    while car.travel_distance < race_length:
        random_speed = random.randint(-15,15)
        Car.accelerate(car,random_speed)
        Car.traveling(car,1)
        if car.travel_distance >= race_length:
            Car.info(car)



