import math
x1, y1, x2, y2 = input().split()
print(math.hypot(float(x1) - float(x2), float(y1) - float(y2)))