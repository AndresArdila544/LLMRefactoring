class Dice:
    def __init__(self):
        self.number = list(range(6))
        self.work = self.number[:]
    
    def setNumber(self, *numbers):
        self.number = numbers
        
    def roll(self, loc):
        if loc == 'E':
            self.setNumber(self.work[3], self.work[1], self.work[0], self.work[5], self.work[4], self.work[2])
        elif loc == 'N':
            self.setNumber(self.work[1], self.work[5], self.work[2], self.work[3], self.work[0], self.work[4])
        elif loc == 'S':
            self.setNumber(self.work[4], self.work[0], self.work[2], self.work[3], self.work[5], self.work[1])
        else:
            self.setNumber(self.work[2], self.work[1], self.work[5], self.work[0], self.work[4], self.work[3])
    
    def get_Top(self):
        return self.number[0]

dice = Dice()
table = list(map(int, input().split()))
dice.setNumber(*table)
loc_array = str(input())

for tmp_loc in loc_array:
    dice.roll(tmp_loc)
print(dice.get_Top())