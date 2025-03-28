```
d = [int(i) for i in input().rstrip().split()]

class Dice:
    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.face = [a1, a2, a3, a4, a5, a6]
        self.v = [a5, a1, a2, a6] # 縦方向
        self.h = [a4, a1, a3, a6] # 横方向
        self.det = 1

    def top(self):
        return self.v[1]

    def north(self):
        newV = [self.v[1], self.v[2], self.v[3], self.v[0]]
        self.v = newV
        self.h[1] = self.v[1]
        self.h[3] = self.v[3]
        return self.v, self.h

    def south(self):
        newV = [self.v[3], self.v[0], self.v[1], self.v[2]]
        self.v = newV
        self.h[1] = self.v[1]
        self.h[3] = self.v[3]
        return self.v, self.h

    def east(self):
        newH = [self.h[3], self.h[0], self.h[1], self.h[2]]
        self.h = newH
        self.v[1] = self.h[1]
        self.v[3] = self.h[3]
        return self.v, self.h

    def west(self):
        newH = [self.h[1], self.h[2], self.h[3], self.h[0]]
        self.h = newH
        self.v[1] = self.h[1]
        self.v[3] = self.h[3]
        return self.v, self.h

    def searchFace(self, a):
        b = 0
        for i in range(6):
            if a == self.face[i]:
                # print('一致しました')
                b = i + 1
        return b

    def smallen(self, x): # a は 1 から 6 のどれか
        y = int(7 / 2 - abs(x - 7 / 2))
        if x != y:
            self.det *= -1
        return y

    def rightSide(self, top, front):
        r = 0
        if top == 1 and front == 2:
            r = 3
        elif top == 2 and front == 1:
            r = 4
        elif top == 1 and front == 3:
            r = 5
        elif top == 2 and front == 4:
            r = 6
        else:
            r = 7
        return r

questionAmount = int(input())
dice1 = Dice(*d)

for i in range(questionAmount):
    # Initialize det
    dice1.det = 1
    question = [int(i) for i in input().rstrip().split()]
    a = dice1.searchFace(question[0])
    b = dice1.searchFace(question[1])
    top = dice1.smallen(a)
    front = dice1.smallen(b)
    position = dice1.rightSide(top, front)
    answer = dice1.face[position - 1]
    print(answer)
```