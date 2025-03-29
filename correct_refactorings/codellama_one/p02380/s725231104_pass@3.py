import math
a,b,C = map(float,input().split())
print("{:f}".format(1/2*a*b*math.sin(math.radians(C))))
print("{:f}".format(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C)))))
print("{:f}".format((1/2*a*b*math.sin(math.radians(C)))/a*2))