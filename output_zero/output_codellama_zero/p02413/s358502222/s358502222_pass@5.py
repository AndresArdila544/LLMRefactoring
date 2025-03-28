Here is a refactored version of the original Python program:

r, c = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(r)]
b = [[0]*(c+1) for _ in range(r+1)]
for i in range(r):
    for j in range(c):
        b[i][j], b[r][j], b[i][c], b[r][c] = a[i][j], a[i][j], a[i][j], a[i][j]  # unpack and assign to multiple variables
for i in b:
    print(*i)