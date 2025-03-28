class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.n_list = [0, self.a, self.b, self.c, self.d, self.e, self.f]
    
    def is_right_surface(self, top, front):
        swapped = False
        if self.n_list.index(top) > self.n_list.index(front):
            tmp = front
            front = top
            top = tmp
            swapped = True
        if 1 in [self.n_list.index(top), self.n_list.index(front)] and not swapped:
            return (self.c, self.d)
        elif 2 in [self.n_list.index(top), self.n_list.index(front)] and not swapped:
            return (self.a, self.f)
        elif 3 in [self.n_list.index(top), self.n_list.index(front)] and not swapped:
            return (self.e, self.b)
        elif 4 in [self.n_list.index(top), self.n_list.index(front)] and not swapped:
            return (self.b, self.e)
        elif 5 in [self.n_list.index(top), self.n_list.index(front)] and not swapped:
            return (self.d, self.c)
        elif 6 in [self.n_list.index(top), self.n_list.index(front)] and not swapped:
            return (self.a, self.f)
    
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