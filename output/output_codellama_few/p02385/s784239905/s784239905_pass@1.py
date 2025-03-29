class Dice(object):
    def __init__(self, numbers):
        self.numbers = {1: numbers[0], 2: numbers[1], 3: numbers[2], 4: numbers[3], 5: numbers[4], 6: numbers[5]}
        
        self.vertical = [self.numbers[1], self.numbers[2], self.numbers[6], self.numbers[5]]
        self.horizontal = [self.numbers[4], self.numbers[1], self.numbers[3], self.numbers[6]]
    
    def roll_dice(self, str):
        for s in str:
            if s == 'N':
                self.vertical = (self.vertical * 2)[3:7]
                self.horizontal[1] = self.vertical[0]
                self.horizontal[3] = self.vertical[2]
                
            elif s == 'S':
                self.vertical = (self.vertical * 2)[1:5]
                self.horizontal[1] = self.vertical[0]
                self.horizontal[3] = self.vertical[2]
            
            elif s == 'W':
                self.horizontal = (self.horizontal * 2)[3:7]
                self.vertical[0] = self.horizontal[1]
                self.vertical[2] = self.horizontal[3]
            
            elif s == 'E':
                self.horizontal = (self.horizontal * 2)[1:5]
                self.vertical[0] = self.horizontal[1]
                self.vertical[2] = self.horizontal[3]
    
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

if dice1.numbers == dice2.numbers:
    print("Yes")
else:
    flag = False
    
    for i in range(6):
        dice1.set_top(i+1)
        for j in xrange(4):
            dice1.roll_dice("SWN")
            
            if dice1.numbers == dice2.numbers:
                flag = True
    
    if not flag:
        dice1.roll_dice("S")
    
    print(flag and "Yes" or "No")