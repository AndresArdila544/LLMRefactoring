import math
a, b, C = map(int, input().split())
S = (a*b*math.sin(math.radians(C))) / 2.0
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C)))
L = a+b+c
h = b * math.sin(math.radians(C))
print('%.8f' % S)
print('%.8f' % L)
print('%.8f' % h)