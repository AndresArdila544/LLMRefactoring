Here is a shorter Python program that still achieves the desired functionality:

import math
x1, y1, x2, y2 = map(float, input().split())
print(round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 5))