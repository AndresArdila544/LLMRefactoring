a, b, Cdegree = map(float, input().split())
Cradian = math.radians(Cdegree)
print(f"{b * math.sin(Cradian) / 2:{0.3f}", end=" ") # h = b sin C
print((math.sqrt(a**2 + b**2 - 2*a*b*math.cos(Cradian))+ a + b:{0.3f}) # c^2 = a^2 + b^2 - 2 a b cos C, L = a + b + c
# S = a h / 2
print((math.sqrt(a**2 + b**2 - 2*a*b*math.cos(Cradian))+ a + b) / 2:{0.3f}) # S = a h / 2, L = a + b + c