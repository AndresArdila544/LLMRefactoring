class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

        self.n_list = [0, self.a, self.e, self.b, self.e, self.f]
    
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
    
    def is_right_surface(self, x, y):
        if (x == 0 and y == 1) or (x == 1 and y == 0) or (x == 2 and y == 3) or (x == 3 and y == 2) or (x == 4 and y == 5) or (x == 5 and y == 4):
            return True, False
        elif (x == 1 and y == 2) or (x == 2 and y == 1) or (x == 3 and y == 4) or (x == 4 and y == 3) or (x == 5 and y == 6) or (x == 6 and y == 5):
            return False, True
        else:
            return False, False

a, b, c, d, e, f = map(int, input().split())
dice = Dice(a, b, c, d, e, f)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    right, left, is_swap = dice.is_right_surface(x, y)
    if is_swap:
        print(left)
    else:
        print(right)