import random


class elevator:
    def __init__(self, top, lowest):
        self.lowest = lowest
        self.top = top
        self.current = lowest

    def print_info(self):
        print(f"\nElevator top level: {self.top}")
        print(f"\nElevator lowest level: {self.lowest}")
        print(f"\nElevator current level: {self.current}\n")

    def go_to_floor(self, floor):
        if self.lowest > floor > self.top:
            self.current = self.current
        elif self.lowest <= floor <= self.top:
            if self.current < floor:
                x = self.lowest
                while x <= floor:
                    elevator.floor_up(self, floor)
                    x = x + 1
            elif self.current > floor:
                x = self.top
                while x >= floor:
                    elevator.floor_down(self, floor)
                    x = x - 1

    def floor_up(self, floor):
        if self.current < floor:
            self.current = self.current + 1
            print(f"Elevator is on the floor {self.current}")

    def floor_down(self, floor):
        if self.current > floor:
            self.current = self.current - 1
            print(f"Elevator is on the floor {self.current}")


class House:
    def __init__(self, top, down, amount):
        self.elevators = []
        self.amount = amount
        self.lowest = down
        self.top = top
        for i in range(amount):
            self.elevators.append(elevator(top, down))

    def print_info(self):
        print(f"House information {self.top} top level , {self.lowest} lowest level , {self.amount} elevators.")
        for i in self.elevators:
            i.print_info()

    def run_elevator(self, elevator_number, elevator_floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"Run elevator {elevator_number}")
        elevator.go_to_floor(elevator_floor)

    def fire_alarm(self):
        print("Fire alarm!!!!!!!")
        for i in self.elevators:
            i.go_to_floor(self.lowest)


if __name__ == '__main__':
    house = House(6, 1, 3)
    house.print_info()
    house.run_elevator(2, 3)
    house.print_info()
    house.run_elevator(3, 5)
    house.print_info()
    house.fire_alarm()
    house.print_info()
