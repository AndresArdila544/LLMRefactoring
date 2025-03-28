class Dice(object):
    def __init__(self, numbers):
        self.numbers_inverse = {numbers[0]: 1, numbers[1]: 2, numbers[2]: 3, numbers[3]: 4, numbers[4]: 5}
        self.numbers = {1: numbers[0], 2: numbers[1], 3: numbers[2], 4: numbers[3], 5: numbers[4]}

        self.vertical = [self.numbers_inverse[numbers[1]], self.numbers_inverse[numbers[2], self.numbers_inverse[numbers[5]]]
        self.horizontal = [self.numbers_inverse[numbers[4]], self.numbers_inverse[numbers[1]], self.numbers_inverse[numbers[3], self.numbers_inverse[numbers[6]]
    
    def roll(self, direction):
        if direction == 'N':
            return self.move_north()
        elif direction == 'S':
            return self.move_south()
        elif direction == 'W':
            return self.move_west()
        else: #direction is 'E'
            return self.move_east()
    
    def move_north(self):
        self.vertical = [self.numbers_inverse[v] for v in (self.vertical * 2)[1:5]] + [self.horizontal[0], self.horizontal[3]]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
    
    def move_south(self):
        self.vertical = [self.numbers_inverse[v] for v in (self.vertical * 2)[3:7] + [self.horizontal[1], self.horizontal[3]]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
    
    def move_east(self):
        self.horizontal = [self.numbers_inverse[v] for v in (self.horizontal * 2)[1:5] + [self.vertical[0], self.vertical[3]]
        self.vertical[0] = self.horizontal[1]
    
    def move_west(self):
        self.horizontal = [self.numbers_inverse[v] for v in (self.horizontal * 2)[3:7] + [self.vertical[0], self.vertical[3]]
        self.vertical[0] = self.horizontal[1]
    
    def map(self):
        self.numbers[1] = self.vertical[0]
        self.numbers[2] = self.vertical[1]
        self.numbers[3] = self.horizontal[2]
        self.numbers[4] = self.horizontal[0]
        self.numbers[5] = self.vertical[3]
    
    def get_top(self):
        return self.numbers[1]

dice1 = Dice([int(x) for x in input().split()])
dice2 = Dice([int(x) for x in input().split()])

flag = True if dice1.numbers == dice2.numbers else False
for i in range(6):
    flag = dice1.roll('SWN') and flag or all(dice1.roll(s) for j in range(4))
if flag:
    print("Yes")
else:
    print("No")