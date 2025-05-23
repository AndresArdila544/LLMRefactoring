class Dice(object):
    def __init__(self, numbers):
        self.numbers_inverse = {numbers[0]: 1, numbers[1]: 2, numbers[2]: 3, numbers[3]: 4, numbers[4]: 5,
                                numbers[5]: 6}
        self.numbers = {1: numbers[0], 2: numbers[1], 3: numbers[2], 4: numbers[3], 5: numbers[4], 6: numbers[5]}
        
        self.vertical = [self.numbers[1], self.numbers[2], self.numbers[6], self.numbers[5]]
        self.horizontal = [self.vertical[0], self.vertical[3]]
    
    def get_top(self):
        return self.vertical[0]
        
    def set_front(self, value):
        for i in range(4):
            if self.vertical[1] == value:
                break
            else:
                self.roll_dice("SWN")
        else:
            return False
        return True
    
    def set_top(self, value):
        for i in range(4):
            if self.vertical[0] == value:
                break
            else:
                self.roll_dice("SWN")
        else:
            return False
        return True
    
    def move_south(self):
        self.vertical = (self.vertical * 2)[3:7]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
    
    def move_north(self):
        self.vertical = (self.vertical * 2)[1:5]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
    
    def move_east(self):
        self.horizontal = (self.horizontal * 2)[3:7]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
    
    def move_west(self):
        self.horizontal = (self.horizontal * 2)[1:5]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
        
    def roll_dice(self, moves):
        for i in range(len(moves)):
            getattr(self, moves[i])()
    
    def map_values(self):
        self.numbers[1] = self.vertical[0]
        self.numbers[2] = self.vertical[1]
        self.numbers[3] = self.horizontal[2]
        self.numbers[4] = self.horizontal[0]
        self.numbers[5] = self.vertical[3]
        self.numbers[6] = self.vertical[2]
        
dice1 = Dice([int(x) for x in raw_input().split()])
dice2 = Dice([int(x) for x in raw_input().split()])

flag = False
if dice1.numbers == dice2.numbers:
    flag = True
else:
    for i in range(6):
        if dice1.set_front(i+1):
            break
        else:
            dice1.roll_dice("SWN")
        if dice1.numbers == dice2.numbers:
            flag = True
    if not flag:
        dice1.roll_dice("S")
    
if flag:
    print("Yes")
else:
    print("No")