Here is a refactored version of the code with fewer lines and improved readability:
```
class Dice:
    def __init__(self):
        self.number = list(range(6))
        self.work = list(range(6))
    
    def set_number(self, n0, n1, n2, n3, n4, n5):
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5
    
    def roll(self, loc):
        for i in range(6):
            self.work[i] = self.number[i]
        if loc == 'E':
            self.set_number(self.work[3], self.work[1], self.work[0], self.work[5], self.work[4], self.work[2])
        elif loc == 'N':
            self.set_number(self.work[1], self.work[5], self.work[2], self.work[3], self.work[0], self.work[4])
        elif loc == 'S':
            self.set_number(self.work[4], self.work[0], self.work[2], self.work[3], self.work[5], self.work[1])
        else:
            self.set_number(self.work[2], self.work[1], self.work[5], self.work[0], self.work[4], self.work[3])
    
    def get_top(self):
        return self.number[0]

dice = Dice()
table = list(map(int, input().split()))
dice.set_number(*table)#init
loc_array=str(input())

for tmp_loc in loc_array:
    dice.roll(tmp_loc)
print(dice.get_top())
```