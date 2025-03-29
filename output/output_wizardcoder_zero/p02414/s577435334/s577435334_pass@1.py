N, M, L = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(N)]
B = [[int(x) for x in input().split()] for i in range(M)]
C = [[0]*L for _ in range(N)]
for i, row_a in enumerate(A):
    C[i] = [sum(row_a[j]*B[j][l] for j, l in enumerate(range(L))]
print(*(" ".join(map(str, (C_row) for C_row in C)) for row_a in A)