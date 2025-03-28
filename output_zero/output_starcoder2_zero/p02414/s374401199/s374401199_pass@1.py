"""
def solve(n, m, l):
    A = []
    B = []
    C = [[0 for j in range(l)] for i in range(n)]
    for i in range(n):
        line  = list(map(int, input().split()))
        A.append(line)
    for i in range(m):
        line  = list(map(int, input().split()))
        B.append(line)

    for i in range(n):
        for j in range(l):
            c = 0
            for k in range(m):
                c += A[i][k] * B[k][j]
            C[i][j] = c
    return C