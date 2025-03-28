Here is a refactored version of the original Python program:
N, M, L = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(N)]
B = [[int(x) for x in input().split()] for i in range(M)]
C = [[0]*L for i in range(N)]
for i in range(N):
    for j in range(L):
        C[i][j] = sum([A[i][k]*B[k][j] for k in range(M)])
for line in C:
    print(*line)