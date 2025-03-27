num,pat,sum=[],[],[]
i=int(0)
N=int(0)
while 1:
    num=list(map(int,input().split(' ')))
    pat.append(num[0])
    sum.append(num[1])
    if(pat[i]==0 and sum[i]==0):
        break
    i=i+1
    N=N+1
i=0
s=0
while(i<N):
    s=0
    for k in range(1,pat[i]+1):
        for l in range(k+1,pat[i]+1):
            for m in range(l+1,pat[i]+1):
                if(sum[i]==k+l+m):
                    s=s+1
    print(s)
    i=i+1
