n, m, l = map(int, input().split())
A = [[0]*m for _ in range(n)]
B = [[0]*l for _ in range(m)]
C = [[0]*l for _ in range(n)]
for i, row in enumerate(map(int, input().split())):
    A[i] = row
for i, row in enumerate(map(int, input().split()):
    B[i] = row
for i in range(n):
    C[i] = sum(A[i][j]*B[j] for j in range(l))
for r in range(n):
    print(*C[r], end=' ') if l > 1 else print(C[r])