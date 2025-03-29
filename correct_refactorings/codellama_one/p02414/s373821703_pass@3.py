import math
n,m,l = map(int,input().split())
YEAH = [list(map(int,input().split())) for i in range(n)]
FUCK = [list(map(int,input().split())) for i in range(m)]
for i in range(n):
    for j in range(l):
        GOMI = sum(FUCK[k][j]*YEAH[i][k] for k in range(m))
        if j!=l:
            print(GOMI)
        else:
            print(GOMI,end=" ")
    print()