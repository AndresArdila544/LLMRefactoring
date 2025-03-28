# Answer


import math
a, b, C = map(int, input().split())
S = 1 / 2 * a * b * math.sin(math.radians(C))
c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C)))
L = a + b + c ** 0.5
h = b * math.sin(math.radians(C))
print(format(S, '.8f'))
print(format(L, '.8f'))
print(format(h, '.8f'))