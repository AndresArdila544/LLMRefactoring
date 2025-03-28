import math
a,b,C = map(int, input().split())

S = 0.5 * a * b * math.sin(math.radians(C))
L = a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C)))
h = b * math.sin(math.radians(C))

print(S)
print(L)
print(h)