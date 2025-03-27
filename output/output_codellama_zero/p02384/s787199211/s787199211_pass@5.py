import sys

class Dice:
    def __init__(self, d):
        self.face = [d[0], d[1], d[2], d[3], d[4], d[5]]
        self.v = [d[5], d[1], d[2], d[3]]
        self.h = [d[4], d[0], d[1], d[2]]
        self.det = 1
    
    def top(self):
        return self.v[1]
    
    def north(self):
        newV = [self.v[1], self.v[2], self.v[3], self.v[0]]
        self.v = newV
        self.h[1] = self.v[1]
        self.h[3] = self.v[3]
    
    def south(self):
        newV = [self.v[3], self.v[0], self.v[1], self.v[2]]
        self.v = newV
        self.h[1] = self.v[1]
        self.h[3] = self.v[3]
    
    def east(self):
        newH = [self.h[3], self.h[0], self.h[1], self.h[2]]
        self.h = newH
        self.v[1] = self.h[1]
        self.v[3] = self.h[3]
    
    def west(self):
        newH = [self.h[1], self.h[2], self.h[3], self.h[0]]
        self.h = newH
        self.v[1] = self.h[1]
        self.v[3] = self.h[3]
    
    def searchFace(self, a):
        b = 0
        for i in range(6):
            if a == self.face[i]:
                b = i + 1
        return b
    
    def smallen(self, x):
        y = int(7 / 2 - abs(x - 7 / 2))
        if x != y:
            self.det *= -1
        return y
    
    def rightSide(self, top, front):
        r = 0
        if top == 1 and front == 2:
            r = 3
        elif top == 2 and front == 3:
            r = 1
        elif top == 3 and front == 1:
            r = 2
        elif top == 1 and front == 3:
            r = 5
        elif top == 3 and front == 2:
            r = 6
        elif top == 2 and front == 1:
            r = 4
        if self.det == -1:
            r = 7 - r
        return r

dice = Dice(list(map(int, sys.stdin.readline().split())))
# command = list(input().rstrip())
command = [int(i) for i in input().rstrip().split()]
questionAmount = int(input())

for _ in range(questionAmount):
    # Initialize det
    dice.det = 1
    question = [int(i) for i in input().rstrip().split()]
    a = dice.searchFace(question[0])
    b = dice.searchFace(question[1])
    # print(a, b)
    top = dice.smallen(a)
    front = dice.smallen(b)
    # print(top, front)
    position = dice.rightSide(top, front)
    answer = dice.face[position - 1]
    print(answer)