n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split()) for _ in range(m)])
C = [[0]*l] * n
for i in range(n):
    for j in range(l):
        C[i][j] = sum(A[i][k]*B[k][j] for k in range(m))
print(*C, sep='\n')