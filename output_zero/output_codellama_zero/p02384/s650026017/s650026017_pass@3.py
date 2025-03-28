class Dice:
    def __init__(self, a, b, c, d, e, f):
        self.n_list = [0, a, b, c, d, e, f]

    def is_right_surface(self, top, front):
        if top == 1 and front == 2:
            return c, d
        elif top == 1 and front == 3:
            return e, b
        elif top == 1 and front == 4:
            return b, e
        elif top == 1 and front == 5:
            return d, c
        elif top == 2 and front == 3:
            return a, f
        elif top == 2 and front == 4:
            return f, a
        elif top == 2 and front == 6:
            return c, d
        elif top == 3 and front == 5:
            return a, f
        elif top == 3 and front == 6:
            return e, b
        elif top == 4 and front == 5:
            return f, a
        elif top == 4 and front == 6:
            return b, e
        elif top == 5 and front == 6:
            return d, c

dice = Dice(*map(int, input().split()))
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    right, left = dice.is_right_surface(x, y)
    print(left if right == x else right)