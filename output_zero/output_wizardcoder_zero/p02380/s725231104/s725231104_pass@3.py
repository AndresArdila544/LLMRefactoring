def calculate(a, b, C):
    return [1/2*a*b*math.sin(math.radians(C)), a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C)), (1/2*a*b*math.sin(math.radians(C))/a*2)]

results = calculate(*map(float, input().split())
print("%f %f %f" % tuple(results))