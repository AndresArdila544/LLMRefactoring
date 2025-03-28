n, m, l = map(int, input().split())
A = [[0 for _ in range(m)] for _ in range(n)], B = [[0 for _ in range(l)] for _ in range(m)], C = [[0 for _ in range(l)] for _ in range(n)]
for row, arow in enumerate(map(lambda x: list(map(int, input().split())[:m], [n])):
    A[row] = arow
for row, brow in enumerate(map(lambda x: list(map(int, input().split())[:l], m)):
    B[row] = brow
C = [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(l)] for i in range(n)]
print(*(" ".join(map(str, C[i])) if j < l-1 else str(C[i][-1]) for i in range(n) for j in range(l)), sep='\n')