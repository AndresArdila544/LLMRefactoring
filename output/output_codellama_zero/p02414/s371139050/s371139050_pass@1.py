n, m, l = map(int, input().split())
A = list(map(int, input().split())) for _ in range(n))
B = list(map(int, input().split())) for _ in range(m))
C = [[0]*l for _ in range(n)]
for i in range(n):
    tmp_sum = 0
    for k in range(m):
        tmp_sum += A[i][k] * B[k][j]
    C[i][j] = tmp_sum
for c in C: print(*c)