import math

a, b, C = map(int, input().split())
c = (a**2 + b**2 - 2*a*b*math.cos(math.radians(C))) ** 0.5
A = (360-2*C)/2
print(0.5*a*b*math.sin(math.radians(C)))
print(a+b+c)
print(b*math.sin(math.radians(C)))