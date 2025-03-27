n=int(input())
a=[0]*4
for i in range(n):
    b,f,r,v=map(int,input().split())
    a[b-1][f-1][r-1]+=v
for j in range(4):
    for k in range(3):
        print(' '+str(a[j][k][l]), end='')
    if(j!=3):
        print('####################')