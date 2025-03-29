```
import sys

class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.n_list = [0, a, b, c, d, e, f]

    def is_right_surface(self, top, front):
        swapped = False
        if self.n_list.index(top) > self.n_list.index(front):
            right, left = front, top
            swapped = True
        else:
            right, left = top, front
        return right, left, swapped

    def move(self, move_str):
        for i in move_str:
            if i == "N":
                self.move_N()
            elif i == "E":
                self.move_E()
            elif i == "W":
                self.move_W()
            elif i == "S":
                self.move_S()

    def move_N(self):
        tmp1 = self.a
        tmp2 = self.e
        self.a = self.b
        self.b = self.f
        self.e = tmp1
        self.f = tmp2

    def move_E(self):
        tmp1 = self.a
        tmp2 = self.c
        self.a = self.d
        self.c = tmp1
        self.d = self.f
        self.f = tmp2

    def move_W(self):
        tmp1 = self.a
        tmp2 = self.d
        self.a = self.c
        self.c = self.f
        self.d = tmp1
        self.f = tmp2

    def move_S(self):
        tmp1 = self.a
        tmp2 = self.b
        self.a = self.e
        self.b = tmp1
        self.e = self.f
        self.f = tmp2

n = int(input())
for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
    dice = Dice(a, b, c, d, e, f)

    right, left, is_swap = dice.is_right_surface(x, y)
    if is_swap:
        print(left)
    else:
        print(right)
```