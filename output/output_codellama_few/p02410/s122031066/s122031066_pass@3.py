import math
n,m=(int(x) for x in input().split())
lst1=[]
lst2=[]
for s in range(n):
    aij=input().split()
    lst1.append(aij)
for t in range(m):
    bi=int(input())
    lst2.append(bi)

GOMI_list = []
for u in range(n):
    for v in range(m):
        number1=int(lst1[u][v])
        number2=lst2[v]
        GOMI = 0
        for k in range(m):
            GOMI += FUCK[k][j]*YEAH[i][k]
        GOMI_list.append(GOMI)
print(*GOMI_list,sep=' ')