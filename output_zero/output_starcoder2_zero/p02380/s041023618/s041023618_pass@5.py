import math
a,b,C = map(int,input().split())
print(a*b*math.sin(math.radians(C))/2)
h=a**2+b**2-2*a*b*math.cos(math.radians(C))**(1/2)
print(a+b+h**(1/2))
print(h/(2*a))