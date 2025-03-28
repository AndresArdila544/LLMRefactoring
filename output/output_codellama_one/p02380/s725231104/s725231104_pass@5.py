import math
a,b,C=map(float,input().split())
print(1/2*a*b*math.sin(math.radians(C)))
print((a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C))))/2)