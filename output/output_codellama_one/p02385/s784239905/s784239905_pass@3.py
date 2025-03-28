import math
class Dice:
    def __init__(self, numbers):
        self.numbers_inverse = {number: index+1 for index, number in enumerate(numbers)}
        self.numbers = {index+1: number for index, number in enumerate(numbers)}
        self.vertical = [self.numbers[1], self.numbers[2], self.numbers[6], self.numbers[5]]
        self.horizontal = [self.numbers[4], self.numbers[1], self.numbers[3], self.numbers[6]]
    def roll_dice(self, str):
        for s in str:
            if s == 'N':
                self.move_north()
            elif s == 'S':
                self.move_south()
            elif s == 'W':
                self.move_west()
            elif s == 'E':
                self.move_east()
    def set_top(self, value):
        counter = 0
        while self.vertical[0] != value:
            if counter == 4: break
            self.roll_dice("SWN")
            counter += 1
        if self.vertical[0] != value: return
        self.map_values()
    def set_front(self, value):
        counter = 0
        while self.vertical[1] != value:
            if counter == 4: break
            self.roll_dice("SWN")
            counter += 1
        if self.vertical[1] != value: return
        self.map_values()
    def move_south(self):
        self.vertical = (self.vertical * 2)[3:7]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
        self.map_values()
    def move_north(self):
        self.vertical = (self.vertical * 2)[1:5]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
        self.map_values()
    def move_east(self):
        self.horizontal = (self.horizontal * 2)[3:7]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
        self.map_values()
    def move_west(self):
        self.horizontal = (self.horizontal * 2)[1:5]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
        self.map_values()
    def map_values(self):
        self.numbers[1] = self.vertical[0]
        self.numbers[2] = self.vertical[1]
        self.numbers[3] = self.horizontal[2]
        self.numbers[4] = self.horizontal[0]
        self.numbers[5] = self.vertical[3]
        self.numbers[6] = self.vertical[2]
    def get_top(self):
        return self.vertical[0]
dice1 = Dice([int(x) for x in raw_input().split()])
dice2 = Dice([int(x) for x in raw_input().split()])
if dice1.numbers == dice2.numbers: print "Yes"
else: print "No"