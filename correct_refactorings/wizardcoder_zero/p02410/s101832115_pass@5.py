n, m = map(int, input().split())
a = [[0 for i in range(m)] for j in range(n)]
b = [0 for i in range(m)]
c = [0 for i in range(n)]
for s in range(n):
    a[s] = list(map(int, input().split()))
for s in range(m):
    b[s] = int(input())
for s in range(n):
    c[s] = sum(a[s][t]*b[t] for t in range(m))
print(*c)