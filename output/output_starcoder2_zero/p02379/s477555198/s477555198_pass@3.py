Here is the refactored version of the code:
import math
def distance(x1,y1,x2,y2):
    return math.sqrt((u.x - v.x) ** 2 + (u.y - v.y) ** 2)


a = [float(e) for e in input().split()]
print(distance(a[0], a[1], a[2], a[3]))