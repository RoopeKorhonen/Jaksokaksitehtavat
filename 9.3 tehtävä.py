class car:
    def __init__(self, license_number, top_speed):
        self.license_number = license_number
        self.top_speed = top_speed
        self.speed = 0
        self.travel_distance = 0
    def info(self):
        print("Auton rekisteri numero", self.license_number, ",", self.top_speed,"km/h maksiminopeus,", self.speed,"km/h nopeus,", self.travel_distance, "km kuljettu matka")
    def accelerate(self, amount):
        if 0 < self.speed + amount < self.top_speed:
            self.speed = self.speed + amount
        elif self.speed + amount <= 0:
            self.speed = 0
        else:
            self.speed = self.top_speed
    def traveling(self, amount):
        self.travel_distance = self.travel_distance + self.speed * amount



car_one = car("ABC-123", 142)
car_one.accelerate(30)
car_one.traveling(400)
car_one.accelerate(70)
car_one.traveling(200)
car_one.info()