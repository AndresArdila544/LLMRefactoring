import math
from math import sqrt
x1, y1, x2, y2 = map(float, input().split())
x, y = x2 - x1, y2 - y1
print(sqrt(x**2 + y**2))