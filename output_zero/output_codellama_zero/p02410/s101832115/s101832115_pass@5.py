import sys
n, m = map(int, input().split())
a = [[0 for i in range(m)] for j in range(n)]
b = [0 for i in range(m)]
c = [0 for i in range(n)]
for s in range(0, n):
    a[s] = list(map(int, input().split()))
for s in range(0, m):
    b[s] = int(input())
for s in range(0, n):
    for t in range(0, m):
        c[s] += a[s][t] * b[t]
print(*c, sep='\n')