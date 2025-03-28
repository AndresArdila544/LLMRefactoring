n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
b = [int(input()) for _ in range(m)]
print(*(sum(x*y for x, y in zip(a[k], b)) for k in range(n))