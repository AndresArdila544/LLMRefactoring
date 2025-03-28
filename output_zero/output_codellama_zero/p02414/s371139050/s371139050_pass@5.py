n, m, l = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
B = list(list(map(int, input().split())) for _ in range(m))
C = [[sum([A[i][k] * B[k][j] for k in range(m)]) for j in range(l)] for i in range(n)]
for c in C:
    print(*c)