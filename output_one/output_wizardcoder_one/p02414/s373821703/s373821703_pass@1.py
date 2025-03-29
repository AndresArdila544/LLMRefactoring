n, m, l = map(int, input().split())
YEAH = [list(map(int, input().split())) for i in range(n)]
FUCK = [list(map(int, input().split()) for j in range(m)]
for i in range(n):
    GOMI = 0
    for k in range(m):
        GOMI += FUCK[k][j]*YEAH[i][k]
    print((GOMI if j!=l else GOMI," ", end="") for j in range(l))
print()