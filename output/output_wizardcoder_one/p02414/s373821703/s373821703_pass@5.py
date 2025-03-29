n, m, l = map(int, input().split())
YEAH = [list(map(int,input().split())) for i in range(n)]
FUCK = [list(map(int,input().split()) for i in range(m)
for j in range(l):
    GOMI = 0
    for k in range(m):
        GOMI += FUCK[k][j]*YEAH[i][k]
    if j != l:
        print(GOMI, end=" ")
    else:
        print(GOMI)
print()