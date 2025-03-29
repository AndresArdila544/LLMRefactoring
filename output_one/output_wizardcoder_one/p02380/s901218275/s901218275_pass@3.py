import math

a, b, C = map(int, input().split())
S = 0.5 * a * b * math.sin(math.radians(C))
c = math.sqrt((a**2 + b**2) - 2 * a * b * math.cos(math.radians(C)))
L = a + b + c
h = b * math.sin(math.radians(C))
print("{:.8f}".format(S), "{:.8f}".format(L), "{:.8f}".format(h) sep='\n')