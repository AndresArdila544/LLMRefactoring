class Dice(object):
    def __init__(self, numbers):
        self._numbers = {num_inverse: num for num_inverse, num in enumerate(numbers)}
        self._vertical = [None] * 4
        self._horizontal = [None] * 4
        
    def roll_dice(self, direction):
        if direction == 'N':
            self.move_north()
        elif direction == 'S':
            self.move_south()
        elif direction == 'W':
            self.move_west()
        elif direction == 'E':
            self.move_east()
    
    def set_top(self, target_value):
        for _ in range(4):
            if self._vertical[0] == target_value:
                return
            else:
                self.roll_dice("S")
                
    def set_front(self, target_value):
        for _ in range(4):
            if self._vertical[1] == target_value or self._horizontal[0] == target_value:
                return
            else:
                self.roll_dice("SWN")
                
    def move_south(self):
        self._vertical = [self._vertical[i] * 2 for i in range(1, 4)] + [None]
        self._horizontal[1], self._horizontal[3] = self._vertical[:2]
        
    def move_north(self):
        self._vertical = [self._vertical[i] * 2 for i in range(3)] + [None, self._vertical[-1]]
        self._horizontal[1], self._horizontal[3] = self._vertical[:2]
        
    def move_east(self):
        self._horizontal = [self._horizontal[i] * 2 for i in range(1, 4)] + [None]
        self._vertical[0], self._vertical[2] = self._horizontal[1:3]
        
    def move_west(self):
        self._horizontal = [self._horizontal[i] * 2 for i in range(3)] + [None]
        self._vertical[0], self._vertical[2] = self._horizontal[1:3]
    
    def map_values(self):
        self._numbers[1], self._numbers[2], self._numbers[3] = self._vertical[:3]
        self._numbers[4], self._numbers[5], self._numbers[6] = self._horizontal[:3]
        
    def get_top(self):
        return self._vertical[0]

dice1 = Dice([int(x) for x in input().split()])
dice2 = Dice([int(x) for x in input().split()])

flag = False
if dice1.numbers == dice2.numbers:
    flag = True
else:
    while not flag and len(set(dice1._vertical) != 1:
        dice1.roll_dice('SWN')
        if dice1.get_top() in dice2._horizontal[:4]:
            dice1.set_front(dice2.get_top())
    while not flag and len(set(dice1._vertical) != 1:
        dice1.roll_dice('N')
        
if flag:
    print("Yes")
else:
    print("No")