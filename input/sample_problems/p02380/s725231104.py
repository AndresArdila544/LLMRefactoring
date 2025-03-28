import math

a,b,C=map(float,input().split())

print("%f"%(1/2*a*b*math.sin(math.radians(C))))
print("%f"%(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C)))))
print("%f"%((1/2*a*b*math.sin(math.radians(C)))/a*2))

