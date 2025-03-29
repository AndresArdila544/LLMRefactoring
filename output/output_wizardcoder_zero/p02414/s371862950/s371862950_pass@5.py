N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]
C = [[0] * L for _ in range(N)]
for n, row in enumerate(zip(*A)):
    C[n] = sum(a*b for a, b in zip(row, B))