r, c = map(int, input().split())
a = [[int(x) for x in input().split()] for i in range(r)]
b = [[0] * (c + 1) for i in range(r + 1)]
for i in range(r):
    for j in range(c):
        b[i][j], b[r][j] += a[i][j]
        b[i][c] += a[i][j]
        b[r][c] += a[i][j]
for i in b: print(*i)