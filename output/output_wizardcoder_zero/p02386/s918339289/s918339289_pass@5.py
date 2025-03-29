```python
import random
from collections import Counter
class Dice:
    def __init__(self, num_list):
        self.top = num_list[0]
        self.dside = num_list[1]
        self.rside = num_list[2]
        self.lside = num_list[3]
        self.uside = num_list[4]
        self.bottom = num_list[5]
    
    def north(self):
        self.top, self.dside, self.bottom, self.uside = self.dside, self.bottom, self.uside, self.top
    
    def east(self):
        self.top, self.lside, self.bottom, self.rside = self.lside, self.bottom, self.rside, self.top
    
    def south(self):
        self.top, self.dside, self.bottom, self.uside = self.uside, self.top, self.dside, self.bottom
        
def rotate_dice(dice, direction):
    if direction == 'north':
        dice.north()
    elif direction == 'east':
        dice.east()
    else:
        dice.south()

def check_same_sides(d1, d2):
    return Counter(d1) == Counter(d2)

n = int(input())
num = [list(map(int, input().split())) for i in range(n)]
for idx1, i in enumerate(dice):
    for idx2, j in enumerate(dice[idx1+1:], start=idx1+1):
        if len(set(i.dlist) ^ set(j.dlist)) == 0:
            continue
        while True:
            rotate_dice(j, random.choice(['north', 'east', 'south']))
            if check_same_sides(i, j):
                break
    else:
        print("No")
        break
else:
    print("Yes")
```