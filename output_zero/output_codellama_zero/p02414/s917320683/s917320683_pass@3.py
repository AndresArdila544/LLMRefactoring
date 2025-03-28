n, m, l = map(int, input().split())
nm = [[int(x) for x in input().split()] for _ in range(n)]
ml = [[int(x) for x in input().split()] for _ in range(m)]
matrix = [list(map(sum, zip(*[vec1*vec2 for vec1, vec2 in zip(nm[i], ml[k])]))) for i in range(n) for k in range(m)]
for row in matrix:
    print(*row)