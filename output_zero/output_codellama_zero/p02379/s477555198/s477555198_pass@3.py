import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)** 2 + (p1.y - p2.y)** 2)

a = [float(e) for e in input().split()]
u = Point(a[0], a[1])
v = Point(a[2], a[3])
print(distance(u, v))