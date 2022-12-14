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
            elif self.current > floor:
                x = self.top
                while x >= floor:
                    elevator.floor_down(self, floor)
    def floor_up(self, floor):
        if self.current < floor:
            self.current = self.current + 1
            print(f"Elevator is on the floor {self.current}")
    def floor_down(self, floor):
        if self.current > floor:
            self.current = self.current - 1
            print(f"Elevator is on the floor {self.current}")

if __name__=='__main__':
    Elevator = elevator(1, 10)
    Elevator.go_to_floor(random.randint(1,10))
    Elevator.print_info()
    Elevator.go_to_floor(1)
    Elevator.print_info()