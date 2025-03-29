class Dice(object):
    def __init__(self, numbers):
        self.numbers_inverse = {v: k for k, v in enumerate([numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5]})}
        self.numbers = {k: v for k, v in self.numbers_inverse.items()}
        
        self.vertical = [self.numbers[v] for v in [1, 2, 6, 5]]
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
    
    def move_south(self):
        self.vertical = (self.vertical * 2)[3:7]
        self.horizontal[1], self.horizontal[0] = self.vertical[:2]
        self.horizontal[3:] = self.vertical[2:4]
    
    def move_north(self):
        self.vertical = (self.vertical * 2)[1:5]
        self.horizontal[1], self.horizontal[0] = self.vertical[:2]
        self.horizontal[3:] = self.vertical[2:4]
    
    def move_east(self):
        self.horizontal = (self.horizontal * 2)[3:7]
        self.vertical[0], self.vertical[1] = self.horizontal[:2]
        
    def move_west(self):
        self.horizontal = (self.horizontal * 2)[1:5]
        self.vertical[0], self.vertical[1] = self.horizontal[:2]
    
    def map_values(self, numbers=[1, 2, 3, 4, 5, 6]):
        for k in range(6):
            if k == 1:
                self.numbers[k + 1] = self.vertical[0]
            elif k == 2:
                self.numbers[k + 1] = self.vertical[1]
            elif k == 3:
                self.numbers[k + 1] = self.horizontal[2]
            elif k == 4:
                self.numbers[k + 1] = self.horizontal[0]
            else:
                self.numbers[k + 1] = self.vertical[3]
        
    def get_top(self):
        return self.vertical[0]

dice1 = Dice([int(x) for x in input().split()])
dice2 = Dice([int(x) for x in input().split()])

if dice1.numbers == dice2.numbers:
    print("Yes")
else:
    for _ in range(4):
        dice1.roll_dice('SWN')
        if dice1.numbers == dice2.numbers:
            break
    else:
        dice1.roll_dice('S')
        if dice1.numbers == dice2.numbers:
            print("Yes")
        else:
            print("No")