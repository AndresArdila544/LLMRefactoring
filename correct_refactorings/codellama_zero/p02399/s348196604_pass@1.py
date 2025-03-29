a, b = map(int, raw_input().split())
d, r, f = a // b, a % b, round(float(a)/float(b), 7)
print d,r,f