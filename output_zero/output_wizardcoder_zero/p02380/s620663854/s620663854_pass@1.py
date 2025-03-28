a, b, C = [int(n) for n in input().split()]
c = (a**2+b**2-2*a*b*math.cos(C/180.*math.pi))**0.5
A = (360.-C)/2.
print("{:.6f}".format(0.5*a*b*math.sin(C/180.*math.pi))
print("{:.6f}".format(a+b+c)
print("{:.6f}".format(b*math.sin(C/180.*math.pi))