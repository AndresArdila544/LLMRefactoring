import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def d(u,v):
    return math.sqrt((u.x - v.x)**2 + (u.y - v.y)**2)

a = list(map(float, input().split()))
print(d(Point(a[0], a[1]), Point(a[2], a[3])))