n,m,l = map(int,input().split())
YEAH = [list(map(int,input().split())) for i in range(n)]
FUCK = [list(map(int,input().split())) for i in range(m)]

for i in range(n):
    GOMI = 0
    for k in range(m):
        GOMI += FUCK[k][j]*YEAH[i][k]
    if j!=l:
        print(GOMI)
    else:
        print(GOMI,end=" ")
print()