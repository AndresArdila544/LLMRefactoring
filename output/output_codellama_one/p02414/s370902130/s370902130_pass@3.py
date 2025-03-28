import math
n, m, l = list(map(int, input().split()))
A = [[0 for _ in range(m)] for _ in range(n)]
B = [[0 for _ in range(l)] for _ in range(m)]
C = [[0 for _ in range(l)] for _ in range(n)]
for row in range(n):
    arow = list(map(int, input().split()))
    for j in range(m):
        A[row][j] = arow[j]
for row in range(m):
    brow = list(map(int, input().split()))
    for j in range(l):
        B[row][j] = brow[j]
for row in range(n):
    for col in range(l):
        sum_v = 0
        for k in range(m):
            sum_v += A[row][k]*B[k][col]
        C[row][col] = sum_v
for row in range(n):
    for col in range(l):
        if col < l - 1:
            print(C[row][col], end=" ")
        else:
            print(C[row][col], end="")
print()