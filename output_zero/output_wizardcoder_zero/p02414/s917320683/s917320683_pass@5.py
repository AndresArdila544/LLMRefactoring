n, m, l = map(int, input().split())
nm = [[int(x) for x in input().split()] for _ in range(n)]
ml = [[int(x) for x in input().split()] for _ in range(m)]
matrix = [[sum(a[k]*b[j] for k in range(m)) for j in range(l)] for a in nm]
for row in matrix:
    print(" ".join(str(x) for x in row))