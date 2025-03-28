Here is the refactored Python program:

import random

class Dice:
    def __init__(self, num_list):
        self.top = num_list[0]
        self.dside = num_list[1]
        self.rside = num_list[2]
        self.lside = num_list[3]
        self.uside = num_list[4]
        self.bottom = num_list[5]
        self.dlist = num_list
    
    def move(self):
        mode = random.randint(0, 2)
        if mode == 0:
            self.north()
        elif mode == 1:
            self.east()
        else:
            self.south()

n = int(input())
num = [list(map(int, input().split())) for i in range(n)]
dice = [Dice(num[i]) for i in range(n)]
for idx1, i in enumerate(dice):
    for idx2, j in enumerate(dice):
        if idx2 <= idx1 or len(set(i.dlist) ^ set(j.dlist)):
            continue
        elif len(set(num[0])) < 4:
            while i.top != j.top or i.rside != j.rside or i.dside != j.dside:
                i.move()
        else:
            while i.top != j.top or (i.rside != j.rside and i.uside != j.uside):
                i.move()
        if i.bottom == j.bottom and i.lside == j.lside and i.dside == j.dside:
            print("No")
            break
    else:
        continue
    break
else:
    print("Yes")