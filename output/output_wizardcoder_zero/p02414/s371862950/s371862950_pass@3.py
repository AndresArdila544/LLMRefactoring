N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split()) for _ in range(M))
C = [[0] * L for _ in range(N)]
for n, row in enumerate(C):
    for l, value in enumerate(zip(*[input() for _ in range(L)]):
        row[l] = sum(a * b for a, b in zip(A[n], value))