class dog:
    counter = 0
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        dog.counter += 1
    def bark(self):
        if self.weight < 10:
            print(f"wuf wuf!! Olen {self.name}")
        else:
            print(f"WUF WUF!! Olen {self.name}")

dog_one = dog("Rekku", 8)
dog_two = dog("Ruffe", 12)
dog_one.bark()
dog_two.bark()
print("Koiria on yhteensä", dog.counter)


class car:
    def __init__(self, license_number, top_speed, speed, accelerate, travel_distance):
        self.license_number = license_number
        self.top_speed = top_speed
        self.speed = speed
        self.travel_distance = travel_distance
        self.accelerate = accelerate
    def info(self):
        print("Auton tiedot", self.license_number, self.top_speed,"km/h maksiminopeus", self.speed,"km/h nopeus",self.acccelerate,"kiihtyvyys", self.travel_distance,"km kuljettu matka")
    def car_accelerating(self):
        accelerating_speed_amount = self.speed + 30 + 70 + 50
        if accelerating_speed_amount > self.top_speed:
            calculation = accelerating_speed_amount - self.top_speed
            accelerating_speed_amount = accelerating_speed_amount - calculation
        return accelerating_speed_amount
car_one = car("ABC-123", 142, 0,car_accelerating(), 0)
car_one.info()