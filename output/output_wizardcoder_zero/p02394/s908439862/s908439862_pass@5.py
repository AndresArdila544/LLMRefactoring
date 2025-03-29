import math
W, H, x, y, r = map(float, input().split())
print("Yes" if (x - r) ** 2 + (y - r) ** 2 <= r ** 2 and (x + r) ** 2 + (y - r) ** 2 <= r ** 2 and (x - W + r) ** 2 + y ** 2 >= r ** 2 and x ** 2 + (y + H - r) ** 2 >= r ** 2 else "No")