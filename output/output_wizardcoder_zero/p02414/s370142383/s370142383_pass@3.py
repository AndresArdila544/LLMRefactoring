n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
for x in range(n):
    o = " ".join([str(sum(A[x][z]*B[z][y] for z in range(l)) for y in range(l)])