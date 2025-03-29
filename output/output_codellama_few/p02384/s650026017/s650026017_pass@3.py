import math
x1, y1, x2, y2 = map(float, input().split())
dx = x1 - x2
dy = y1 - y2
d = math.hypot(dx, dy)
print(d)

n = int(input())
for i in range(n):
    x, y = map(float, input().split())
    right, left, is_swap = dice.is_right_surface(x, y)
    if is_swap:
        print(left)
    else:
        print(right)