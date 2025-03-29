N, M, L = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(N)]
B = [[int(x) for x in input().split()] for i in range(M)]
C = [[0] * L for i in range(N)]
for n, row_a in enumerate(A):
    for l, elem_a in enumerate(row_a):
        for m, elem_b in enumerate(B[m]):
            C[n][l] += elem_a*elem_b
for row in C:
    print(*row)