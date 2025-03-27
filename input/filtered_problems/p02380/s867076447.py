import math

a, b, Cdegree = map(float, input().split())
Cradian = math.radians(Cdegree)

# h = b sin C
h = b * math.sin(Cradian)
# c^2 = a^2 + b^2 - 2 a b cos C
c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(Cradian))
L = a + b + c
S = a * h / 2

print(S)
print(L)
print(h)

