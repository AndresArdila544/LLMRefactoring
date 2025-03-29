n,m,l = map(int,input().split())
YEH = [list(map(int,input().split())) for i in range(n)]
FUK = [list(map(int,input().split()) for j in range(m))
for i in range(n):
    GOMI_list = []
    for k in range(l):
        GOMI = 0
        for j in range(m):
            GOMI += FUK[j][k]*YEH[i][k]
        print(GOMI,end=" ")
    print()