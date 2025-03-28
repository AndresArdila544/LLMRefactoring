class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.n_list = [0, a, b, c, d, e, f]
    
    def is_right_surface(self, top, front):
        swapped = False
        if self.n_list.index(top) > self.n_list.index(front):
            tmp = front
            front = top
            top = tmp
            swapped = True
        
        return {
            12: (self.c, self.d, swapped),
            13: (self.e, self.b, swapped),
            14: (self.b, self.e, swapped),
            15: (self.d, self.c, swapped),
            23: (self.a, self.f, swapped),
            24: (self.f, self.a, swapped),
            26: (self.c, self.d, swapped),
            35: (self.a, self.f, swapped),
            36: (self.e, self.b, swapped),
            45: (self.f, self.a, swapped),
            46: (self.b, self.e, swapped),
            56: (self.d, self.c, swapped)
        }[top * 10 + front]
    
    def move(self, moves):
        for m in moves:
            if m == "N":
                self.move_N()
            elif m == "E":
                self.move_E()
            elif m == "W":
                self.move_W()
            elif m == "S":
                self.move_S()

    def move_N(self):
        tmp1, tmp2 = self.n_list[1], self.n_list[4]
        self.n_list[1] = self.n_list[5]
        self.n_list[4] = tmp1
        self.n_list[5] = tmp2
    
    def move_E(self):
        tmp1, tmp2 = self.n_list[0], self.n_list[3]
        self.n_list[0] = self.n_list[2]
        self.n_list[3] = tmp1
        self.n_list[2] = tmp2
    
    def move_W(self):
        tmp1, tmp2 = self.n_list[0], self.n_list[4]
        self.n_list[0] = self.n_list[3]
        self.n_list[3] = tmp1
        self.n_list[4] = tmp2
    
    def move_S(self):
        tmp1, tmp2 = self.n_list[1], self.n_list[5]
        self.n_list[1] = self.n_list[3]
        self.n_list[5] = tmp1
        self.n_list[3] = tmp2

a, b, c, d, e, f = map(int, input().split())
dice = Dice(a, b, c, d, e)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    right_surface, _, swapped = dice.is_right_surface(*sorted([x, y]))
    if swapped:
        print(right_surface)
    else:
        print(dice.n_list[y])