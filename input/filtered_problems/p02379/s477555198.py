import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

def d(u, v):
    return math.sqrt((u.x - v.x) ** 2 + (u.y - v.y) ** 2)


a = [float(e) for e in input().split()]
u = Point(a[0], a[1])
v = Point(a[2], a[3])
print(d(u, v))

