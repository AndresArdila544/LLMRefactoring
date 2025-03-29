class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.n_list = [a, b, c, d, e, f]

    def is_right_surface(self, top, front):
        if {top, front} == {1, 2}:
            return c, d, False
        elif {top, front} == {1, 3}:
            return e, b, False
        elif {top, front} == {1, 4}:
            return b, e, False
        elif {top, front} == {1, 5}:
            return d, c, False
        elif {top, front} == {2, 3}:
            return a, f, False
        elif {top, front} == {2, 4}:
            return f, a, False
        elif {top, front} == {2, 6}:
            return c, d, False
        elif {top, front} == {3, 5}:
            return a, f, False
        elif {top, front} == {3, 6}:
            return e, b, False
        elif {top, front} == {4, 5}:
            return f, a, False
        else:
            return d, c, True

    def move_N(self):
        self.n_list[0], self.n_list[1] = self.n_list[1], self.n_list[4]
        self.n_list[1], self.n_list[2] = self.n_list[2], self.n_list[1]
        self.n_list[2], self.n_list[3] = self.n_list[3], self.n_list[2]
        
    def move_E(self):
        self.n_list[0], self.n_list[2] = self.n_list[2], self.n_list[1]
        self.n_list[1], self.n_list[3] = self.n_list[3], self.n_list[1]
        
    def move_W(self):
        self.n_list[0], self.n_list[2] = self.n_list[2], self.n_list[0]
        self.n_list[1], self.n_list[3] = self.n_list[3], self.n_list[1]
        
    def move_S(self):
        self.n_list[0], self.n_list[2] = self.n_list[2], self.n_list[3]
        self.n_list[1], self.n_list[4] = self.n_list[4], self.n_list[3]
        
    def move(self, moves):
        for i in moves:
            if i == "N":
                self.move_N()
            elif i == "E":
                self.move_E()
            elif i == "W":
                self.move_W()
            else:
                self.move_S()
        
a, b, c, d, e = map(int, input().split())
dice = Dice(a, b, c, d, e)
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    right, left, is_swap = dice.is_right_surface(x, y)
    if not is_swap:
        print(right)
    else:
        print(left)