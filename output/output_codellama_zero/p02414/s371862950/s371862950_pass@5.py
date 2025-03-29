N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(M)]
C = [[0] * L for i in range(N)]
for n in range(N):
    for m in range(M):
        for l in range(L):
            C[n][l] += A[n][m] * B[m][l]
print(*row)