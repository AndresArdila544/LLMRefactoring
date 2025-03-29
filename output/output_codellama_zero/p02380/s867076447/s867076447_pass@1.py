import math
a, b, Cdegree = map(float, input().split())
Cradian = math.radians(Cdegree)
c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(Cradian))
L = a + b + c
S = a * (b * math.sin(Cradian)) / 2
print(S)
print(L)
print(b * math.sin(Cradian))