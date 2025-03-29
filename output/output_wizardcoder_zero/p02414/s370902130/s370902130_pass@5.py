n, m, l = list(map(int, input().split()))
A = [[0 for _ in range(m)] for _ in range(n)]
B = [[0 for _ in range(l)] for _ in range(m)]
C = [[0 for _ in range(l)] for _ in range(n)]
for i, row in enumerate([list(map(int, input().split())) for _ in range(n)]):
    A[i] = row
for i, row in enumerate([list(map(int, input().split()) for _ in range(m)]):
    B[i] = row
for i, row in enumerate([[sum(A[r][k]*B[k][c] for k in range(l)) for c in range(l) for r in range(n)]:
    C[i%n][i//n] = row
for row in C[:n]:
    print(*row)