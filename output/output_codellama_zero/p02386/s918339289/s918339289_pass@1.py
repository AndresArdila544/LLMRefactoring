Here is a more concise and readable version of the original code:

import random

class Dice:
    def __init__(self, num_list):
        self.sides = [num_list[0], num_list[1], num_list[2], num_list[3], num_list[4], num_list[5]]
        self.top = num_list[0]
        self.dside = num_list[1]
        self.rside = num_list[2]
        self.lside = num_list[3]
        self.uside = num_list[4]
        self.bottom = num_list[5]
    
    def move(self, direction):
        if direction == "N":
            (self.top, self.dside, self.bottom, self.uside) = (self.dside, self.bottom, self.uside, self.top)
        elif direction == "E":
            (self.top, self.lside, self.bottom, self.rside) = (self.lside, self.bottom, self.rside, self.top)
        else:
            (self.top, self.dside, self.bottom, self.uside) = (self.uside, self.top, self.dside, self.bottom)
    
    def __eq__(self, other):
        return self.sides == other.sides

n = int(input())
num = [list(map(int, input().split())) for i in range(n)]
dice = [Dice(num[i]) for i in range(n)]
for idx1, i in enumerate(dice):
    for idx2, j in enumerate(dice):
        if idx2 <= idx1 or len(set(i.sides) ^ set(j.sides)):
            continue
        elif len(set(num[0])) < 4:
            while i.top != j.top or i.rside != j.rside or i.dside != j.dside:
                mode = random.randint(0, 2)
                if mode == 0:
                    j.move("N")
                elif mode == 1:
                    j.move("E")
                else:
                    j.move("S")
        else:
            while i.top != j.top or (i.rside != j.rside and i.uside != j.uside):
                mode = random.randint(0, 2)
                if mode == 0:
                    j.move("N")
                elif mode == 1:
                    j.move("E")
                elif mode == 2:
                    j.move("S")
        if i == j:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")