a, b, C = map(float, input().split())
S = (1 / 2) * a * b * math.sin(math.radians(C))
c = math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(math.radians(C)))
L = a + b + c
h = b * math.sin(math.radians(C))
print("{:.8f}".format(S), end=' ')
print("{:.8f}".format(L), end=' ')
print("{:.8f}\n".format(h)