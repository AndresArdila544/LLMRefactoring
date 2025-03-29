n, m, l = map(int, input().split())
A = [[0 for _ in range(m)] for _ in range(n)], B = [[0 for _ in range(l)] for _ in range(m), C = [[0 for _ in range(l)] for _ in range(n)]
for i in range(n): A[i] = list(map(int, input().split()))
for i in range(m): B[i] = list(map(int, input().split())
for i in range(n):
    for j in range(l):
        C[i][j] = sum([A[i][k]*B[k][j] for k in range(m)]
for row in range(n):
    print(*C[row], sep=" ")