import sys
x = sys.stdin.readline().split()
m = map(int, x)

a, b, c = sorted(m)[0:3]
print(a,b,c)