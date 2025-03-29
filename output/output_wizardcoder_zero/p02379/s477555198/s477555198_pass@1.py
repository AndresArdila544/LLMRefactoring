import math
class Point(object):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
def distance_between_points(u: Point, v: Point) -> float:
    return math.sqrt((u.x - v.x) ** 2 + (u.y - v.y) ** 2)

a = [float(e) for e in input().split()]
u = Point(*a[:2])
v = Point(*a[2:])
print(distance_between_points(u, v))