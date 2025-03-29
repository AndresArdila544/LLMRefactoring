n, m, l = map(int, input().split())
A, B, C = [[0 for _ in range(m)] for _ in range(n)], [[0 for _ in range(l)] for _ in range(m)], [[0 for _ in range(l)] for _ in range(n)]

for row in range(n):
    A[row] = list(map(int, input().split()))

for row in range(m):
    B[row] = list(map(int, input().split()))

for row in range(n):
    for col in range(l):
        sum_v = 0
        for k in range(m):
            sum_v += A[row][k] * B[k][col]
        C[row][col] = sum_v

for row in range(n):
    print(*C[row], sep=" ")