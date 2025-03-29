Here is a refactored version of the original program:

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
        
        # Check for each combination of top and front
        # If the top is less than or equal to the front, return the right surface
        if self.n_list.index(top) <= self.n_list.index(front):
            return self.n_list[self.n_list.index(top) + 2], \
                   self.n_list[self.n_list.index(front) - 1], swapped
        
        # If the top is greater than the front, return the left surface
        return self.n_list[self.n_list.index(top) - 1], \
               self.n_list[self.n_list.index(front) + 2], swapped

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
        tmp1 = self.n_list[0]
        tmp2 = self.n_list[6]
        self.n_list[0] = self.n_list[2]
        self.n_list[6] = self.n_list[4]
        self.n_list[2] = tmp1
        self.n_list[4] = tmp2
    
    def move_E(self):
        tmp1 = self.n_list[0]
        tmp2 = self.n_list[6]
        self.n_list[0] = self.n_list[3]
        self.n_list[6] = self.n_list[5]
        self.n_list[3] = tmp1
        self.n_list[5] = tmp2
    
    def move_W(self):
        tmp1 = self.n_list[0]
        tmp2 = self.n_list[6]
        self.n_list[0] = self.n_list[3]
        self.n_list[6] = self.n_list[5]
        self.n_list[3] = tmp1
        self.n_list[5] = tmp2
    
    def move_S(self):
        tmp1 = self.n_list[0]
        tmp2 = self.n_list[6]
        self.n_list[0] = self.n_list[4]
        self.n_list[6] = self.n_list[2]
        self.n_list[4] = tmp1
        self.n_list[2] = tmp2

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