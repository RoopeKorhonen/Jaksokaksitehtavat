class car:
    def __init__(self, license_number, top_speed, speed, travel_distance):
        self.license_number = license_number
        self.top_speed = top_speed
        self.speed = speed
        self.travel_distance = travel_distance
    def info(self):
        print(self.license_number, self.top_speed,"km/h", self.speed,"km/h", self.travel_distance,"km")

car_one = car("ABC-123", 142, 0, 0)
car_one.info()