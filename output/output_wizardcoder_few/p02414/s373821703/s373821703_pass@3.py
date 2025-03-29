n,m,l = map(int,input().split())
for i in range(1,n+1):
    GOMI_list = [0]*l
    for j in range(l):
        for k in range(m):
            GOMI_list[j] += FUCK[k][i-1]*YEAH[j]
    print(*GOMI_list, sep=' ')