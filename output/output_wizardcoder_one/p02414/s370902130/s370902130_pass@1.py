import math
n, m, l = map(int, input().split())
A, B, C = [[0]*l for _ in range(n)], [[0]*m for _ in range(n)], [[0]*l for _ in range(n)]
for i in range(n):
    A[i] = list(map(int, input().split()))
    B[i] = list(map(int, input().split())[:m])
for i in range(n):
    for j in range(l):
        C[i][j] = sum(A[i][k]*B[k][j] for k in range(m))
for row in C:
    print(*row[:-1], end=" ")
    print(row[-1])