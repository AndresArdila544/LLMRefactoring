import math
n = int(input())
s = [False]*13
h = [False]*13
c = [False]*13
d = [False]*13
for _ in range(n):
    m, a = input().split()
    if m == 'S': s[int(a)-1] = True
    elif m == 'H': h[int(a)-1] = True
    elif m == 'C': c[int(a)-1] = True
    elif m == 'D': d[int(a)-1] = True
for i in range(13):
    if not s[i]: print("S %d" % (i+1))
for i in range(13):
    if not h[i]: print("H %d" % (i+1))
for i in range(13):
    if not c[i]: print("C %d" % (i+1))
for i in range(13):
    if not d[i]: print("D %d" % (i+1))