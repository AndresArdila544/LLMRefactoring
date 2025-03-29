n,m,l = map(int,input().split())
YEAH = [[int(x) for x in input().split()]for i in range (n)]
FUCK = [[int(x)for x in input().split()]for i in range (m)]
for i in range (n):
    row_total=[0]*l
    for k in range (m):
        row_total[j]+=FUCK[k][j]*YEAH[i][k]
    if j!=l:
        print(row_total)
    else:
        print(*row_total,end=" ")
print()