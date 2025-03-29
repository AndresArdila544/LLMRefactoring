Here is the refactored version of the Python program:

import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def d(u, v):
    return math.hypot(u.x - v.x, u.y - v.y)

a = [float(e) for e in input().split()]
print(d(Point(a[0], a[1]), Point(a[2], a[3])))