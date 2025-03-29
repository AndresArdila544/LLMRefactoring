import math

W, H, x, y, r = map(float, input().split())

if math.hypot(x - W + r, y - H + r) > r:
    print("No")
else:
    print("Yes")