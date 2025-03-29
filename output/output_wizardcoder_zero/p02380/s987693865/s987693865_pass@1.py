a, b, angle = map(int, input().split())
rad = (angle / 180) * math.pi
c = (a**2 + b**2 - 2 * a * b * math.cos(rad)) ** 0.5
s = (a+b+c)/2
S = (s*(s-a)*(s-b)*(s-c))**0.5
print("{:.5f}".format(S))
print("{:.5f}".format(a+b+c))
print("{:.5f}".format((2*S)/a)