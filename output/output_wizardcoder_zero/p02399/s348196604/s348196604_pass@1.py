a, b = map(int, input().split())
d, r = a // b, a % b
f = round(float(a) / float(b), 7)
print(d, r, f)