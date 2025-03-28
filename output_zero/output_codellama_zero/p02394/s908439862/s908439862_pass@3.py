import math

W, H, x, y, r = map(float, input().split())
if math.hypot(x - W / 2, y - H / 2) > r:
    print("No")
else:
    print("Yes")