n, m, l = map(int, input().split())
A = [[int(s) for s in input().split()] for i in range(n)]
B = [[int(s) for s in input().split()] for i in range(m)]
[print(" ".join([str(sum(A[x][z]*B[z][y] for z in range(l)) for y in range(l)]), end=" ") for x in range(n)]