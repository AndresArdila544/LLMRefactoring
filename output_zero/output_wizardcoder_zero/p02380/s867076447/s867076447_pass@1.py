a, b, Cdegree = map(float, input().split())
Cradian = math.radians(Cdegree)
h = b * math.sin(Cradian)
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(Cradian))
L = a + b + c
S = a * h / 2
print(S)
print(L)