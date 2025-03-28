import math
a, b, Cdegree = map(float, input().split())
c = math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(math.radians(Cdegree)))
L = a + b + c
S = a * h / 2
print(f"{S:.2f}")
print(f"{L:.2f}")