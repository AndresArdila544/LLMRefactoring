Here is an example of a program that works as intended, but I need you to refactor it into fewer lines and complexity:

import math

x1, y1, x2, y2 = map(float, input().split())

dx  = x1 - x2
dy  = y1 - y2

d   = math.hypot(dx, dy)
print d

Refactored version:


import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(x1-x2, y1-y2)
print(d)


Here is the Python program that works as intended, but I need you to refactor it into fewer lines and complexity:

a, b = map(int, raw_input().split())
print a / b
print a % b
print float(a) / b
Refactored version:

a, b = map(int, input().split())
print (a // b),  (a % b),  (float(a)/b)

Here is the Python program that works as intended, but I need you to refactor it into fewer lines and complexity:

import math
x1, y1, x2, y2 = map(float, input().split())
dx = x1 - x2
dy = y1 - y2
d  = math.hypot(dx, dy)
print d
Refactored version:


import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(x1-x2, y1-y2)
print (d)