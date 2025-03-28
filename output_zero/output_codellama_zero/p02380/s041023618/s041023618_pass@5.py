import math

a, b, C = map(int, input().split())
s = (a * b * math.sin(math.radians(C))) / 2
c2 = a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C))
h = s * 2 / a
print(h)