a, b = map(int, input().split())
d = a//b
r = a%b
f = float(a)/float(b)
print(d, r, '%10.8f' % f)