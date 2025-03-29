import math
a, b, c = map(float, input().split())
s = (0.5 * a * b) * math.sin(math.radians(c))
l = a + b + math.sqrt((a**2) + (b**2) - 2 * a * b * math.cos(math.radians(c)))
h = s / a
print("\n".join([str(s), str(l), str(h)]))