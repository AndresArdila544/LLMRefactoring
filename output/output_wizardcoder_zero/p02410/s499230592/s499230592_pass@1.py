n, m = map(int, input().split())
a = [[0]*m for i in range(n)]
for _ in range(n):
    a[i] = list(map(lambda x: int(x) * k, input().split()))
print(' '.join([str(sum(row)) for row in a]))