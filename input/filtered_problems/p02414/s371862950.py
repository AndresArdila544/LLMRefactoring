N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(M)]
C = [[0] * L for i in range(N)]

for n in range(N):
    for l in range(L):
        for m in range(M):
            C[n][l] += A[n][m] * B[m][l]
for row in C:
    print(*row)
