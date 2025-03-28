class Dice:
    def __init__(self, lst):
        self.val = lst
    
    def rotate(self, dir):
        if dir == "N":
            tmp = self.val[0]
            self.val[0], self.val[1], self.val[5], self.val[4], tmp =  self.val[1], self.val[5], self.val[4], tmp, self.val[0]
        elif dir == "E":
            tmp = self.val[0]
            self.val[0], self.val[3], self.val[5], self.val[2], tmp =  self.val[3], self.val[5], self.val[2], tmp, self.val[0]
        elif dir == "S":
            tmp = self.val[0]
            self.val[0], self.val[4], self.val[5], self.val[1], tmp =  self.val[4], self.val[5], self.val[1], tmp, self.val[0]
        elif dir == "W":
            tmp = self.val[0]
            self.val[0], self.val[2], self.val[5], self.val[3], tmp =  self.val[2], self.val[5], self.val[3], tmp, self.val[0]

x = list(map(int,input().split()))
q = int(input())

D = Dice(x)

import random

for i in range(q):
    a,b=map(int,input().split())
    count = 0
    while True:
        D.rotate(random.choice(["N", "E", "S", "W"]))
        #count += 1
        if D.val[0] == a and D.val[1] == b:
            
            print(D.val[2])
            break