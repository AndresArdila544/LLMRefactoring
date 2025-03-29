point_t = point_h = 0
n = int(input())
for _ in range(n):
    card_t, card_h = input().split()
    if float(card_t) > float(card_h):
        point_t += 3
    elif float(card_t) < float(card_h):
        point_h += 3
    else:
        point_t += 1
        point_h += 1
print(point_t, point_h)

Example 4:
import math
x1,y1 = map(float, input().split())
x2,y2 = map(float, input().split())
dx = x1-x2
dy = y1-y2
d = math.sqrt(dx*dx + dy*dy)
print(int(d))