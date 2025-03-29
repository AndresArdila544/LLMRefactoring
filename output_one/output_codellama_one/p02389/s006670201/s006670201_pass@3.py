import math

tate, yoko = map(int, input().split())

d = math.hypot(tate - yoko)

print(d)