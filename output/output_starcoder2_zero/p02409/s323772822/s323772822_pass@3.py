"""

n=int(input())
a=[[[0 for l in range(10)] for j in range(3)] for k in range(4)]
for i in range(n):
    b,f,r,v=map(int,input().split())
    a[b-1][f-1][r-1]+=v
for j in range(4):
    for k in range(3):
        print(' '.join(map(str,[a[j][k][l] for l in range(10)])))
    if(j!=3):
        print('####################')