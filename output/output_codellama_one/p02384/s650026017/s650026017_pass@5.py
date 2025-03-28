class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.faces = [a, b, c, d, e, f]
        self.n_list = list(range(1, 7))

    def is_right_surface(self, top, front):
        swapped = False
        if self.n_list.index(top) > self.n_list.index(front):
            tmp = front
            front = top
            top = tmp
            swapped = True
        return (top, left, swapped)

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
        tmp1 = self.faces[0]
        tmp2 = self.faces[4]
        self.faces[0] = self.faces[3]
        self.faces[4] = self.faces[7]
        self.faces[3] = tmp1
        self.faces[7] = tmp2

    def move_E(self):
        tmp1 = self.faces[0]
        tmp2 = self.faces[3]
        self.faces[0] = self.faces[4]
        self.faces[4] = self.faces[5]
        self.faces[3] = tmp1
        self.faces[5] = tmp2

    def move_W(self):
        tmp1 = self.faces[0]
        tmp2 = self.faces[5]
        self.faces[0] = self.faces[4]
        self.faces[5] = self.faces[7]
        self.faces[4] = tmp1
        self.faces[7] = tmp2

    def move_S(self):
        tmp1 = self.faces[0]
        tmp2 = self.faces[7]
        self.faces[0] = self.faces[6]
        self.faces[6] = self.faces[3]
        self.faces[7] = tmp1
        self.faces[3] = tmp2

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