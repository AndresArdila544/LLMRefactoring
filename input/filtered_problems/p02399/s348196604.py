a, b = map(int, raw_input().split())

d = a // b
r = a % b
f = round(float(a)/float(b), 7)

print d,r,f