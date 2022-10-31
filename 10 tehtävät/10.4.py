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
class Race:
    def __init__(self, lenght, name, cars):
        self.name = name
        self.race_lenght = lenght
        self.cars = cars
    def hour_spend(self):
        for car in self.cars:
            random_speed = random.randint(-50, 80)
            Car.accelerate(car, random_speed)
            car.traveling(1)
    def situation_info(self):
        for car in self.cars:
            Car.info(car)
    def race_over(self):
        for car in self.cars:
            if car.travel_distance >= self.race_lenght:
                return True
            else:
                continue

def car_making():
    cars = []
    for i in range (3):
        cars.append(Car("a-"+ str(i), 200))
    #for car in cars:
        #print(car.info())
    return cars
if __name__=='__main__':
    race = Race(8000, str("Bigcrashrace"), car_making())
    hour = 0
    while True:
        race.hour_spend()

        if race.race_over():
            print("Race over")
            race.situation_info()
            break
        else:
            hour = hour + 1
            if hour % 10 == 0:
                print(f"Hour: {hour}\n")
                race.situation_info()
            else:
                continue




