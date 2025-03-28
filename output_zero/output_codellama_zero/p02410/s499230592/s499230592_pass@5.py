n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(m):
        a[i][j] *= int(input())
print(*map(sum, a))