n,m,l = map(int,input().split())
YEAH = [list(map(int,input().split())) for i in range(n)]
FUCK = [list(map(int,input().split())) for i in range(m)]
for i in range(n):
    GOMI_list = []
    for j in range(l):
        GOMI = 0
        for k in range(m):
            GOMI += FUCK[k][j]*YEAH[i][k]
        GOMI_list.append(GOMI)
    print(*GOMI_list,sep=' ')