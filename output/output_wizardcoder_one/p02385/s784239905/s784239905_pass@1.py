class Dice(object):
    def __init__(self, numbers):
        self.numbers = {i+1: num for i,num in enumerate(numbers)}
        self.vertical_values = [self.numbers[1], self.numbers[2], self.numbers[6], self.numbers[5]]
        self.horizontal_values = [self.numbers[4], self.numbers[1], self.numbers[3], self.numbers[6] if 6 in numbers else None, self.numbers[4] if 4 not in numbers else None]
    def move(self, direction):
        if direction == 'N':
            self.move_north()
        elif direction == 'S':
            self.move_south()
        elif direction == 'W':
            self.move_west()
        elif direction == 'E':
            self.move_east()
    def move_south(self):
        self.vertical_values = [self.vertical_values[3], *([None]*2) + self.vertical_values[:3]]
        self.horizontal_values[1] = self.vertical_values[0]
        if 4 in self.numbers:
            self.horizontal_values[3] = self.vertical_values[2]
    def move_north(self):
        self.vertical_values = [*([None]*2) + self.vertical_values[:3]]
        self.horizontal_values[1] = self.vertical_values[0]
        if 4 in self.numbers:
            self.horizontal_values[3] = self.vertical_values[2]
    def move_east(self):
        self.horizontal_values = [self.horizontal_values[3], *([None]*2) + self.horizontal_values[:2]]
        if 4 in self.numbers:
            self.vertical_values[0] = self.horizontal_values[1]
    def move_west(self):
        self.horizontal_values = [*([None]*2) + self.horizontal_values[:2]
    def update(self, dice):
        if all(val is None for val in self.vertical_values):
            return False
        for i in range(4):
            if self.vertical_values == dice.vertical_values:
                return True
            self.move('SWN')
        self.move('S')
    def get_top(self, dice):
        return self.vertical_values[0]
dice1 = Dice([int(x) for x in input().split()])
dice2 = Dice([int(x) for x in input().split()] if all(x is not None for x in dice1.vertical_values) else None)
if dice2 and any(dice1.update(Dice(list(map(lambda d: dice1.numbers[d], range(6)) * 4)): d == dice2.get_top() for d in range(1,7)):
    print("Yes")
else:
    print("No")
"""