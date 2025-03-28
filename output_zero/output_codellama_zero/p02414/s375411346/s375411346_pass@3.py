N, M, L = map(int, input().split())
A = [[int(i) for i in input().split()] for i in range(N)]
B = [[int(i) for i in input().split()] for i in range(M)]
C = [sum([A[i][j] * B[j][k] for j in range(M)]) for k in range(L-1)] + [sum([A[i][j] * B[j][L-1] for j in range(M)])]
print(*C, sep=' ')