n, m, l = map(int, input().split())
A, B = [list(map(int, input().split())) for _ in range(2)], [[0]*l for i in range(m)]
for x in range(n):
    A[x] = list(map(int, input().split()))
for y in range(l):
    o = []
    for x in range(n):
        B[y][x] = int(input())
    s = sum(A[i][j]*B[j][y] for i in range(n) for j in range(m))
    o.append(str(s))
print(" ".join(o))