import random


class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def print_info(self):
        print(f"\nHissin ylin kerros: {self.ylin}")
        print(f"Hissin alin kerros: {self.alin}")
        print(f"Hissin nykyinen kerros: {self.nykyinen}\n")

    def go_to_floor(self, kerros):

        if self.alin > kerros > self.ylin:
            self.nykyinen = self.nykyinen

        elif self.alin <= kerros <= self.ylin:

            if self.nykyinen < kerros:
                x = self.alin

                while x <= kerros:
                    Hissi.floor_up(self, kerros)
                    x = x + 1

            elif self.nykyinen > kerros:
                x = self.ylin

                while x >= kerros:
                    Hissi.floor_down(self, kerros)
                    x = x - 1

    def floor_up(self, kerros):
        if self.nykyinen < kerros:
            self.nykyinen = self.nykyinen + 1
            print(f"Hissi on kerroksessa {self.nykyinen}")

    def floor_down(self, kerros):
        if self.nykyinen > kerros:
            self.nykyinen = self.nykyinen - 1
            print(f"Hissi on kerroksessa {self.nykyinen}")
class House:
    def __init__(self, alin, ylin, amount):
        self.elevators = []
        self.amount = amount
        self.alin = alin
        self.ylin = ylin
        for i in range (amount):
            self.elevators.append(Hissi(alin, ylin))
    def print_info(self):
        print(f"Talon tiedot {self.ylin} ylinkerros, {self.alin} alinkerros , {self.amount} hissien määrä.")
        for i in self.elevators:
            i.print_info()
    def run_elevator(self, elevator_number, elevator_floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"Ajetaan {elevator_number}")
        elevator.go_to_floor(elevator_floor)






if __name__ == '__main__':
    house = House(1, 6, 3)
    house.print_info()

    house.run_elevator(2, 3)
    house.print_info()