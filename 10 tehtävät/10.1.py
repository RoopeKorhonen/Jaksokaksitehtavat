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
        if self.lowest > current


