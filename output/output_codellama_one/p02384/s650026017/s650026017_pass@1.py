import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(x1-x2, y1-y2)
print(d)


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