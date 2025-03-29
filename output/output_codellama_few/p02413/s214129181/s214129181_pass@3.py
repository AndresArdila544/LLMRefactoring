import sys
n,m=map(int,input().split())
a=[list(map(int, input().split())) for i in range(n)]
for i in range(len(a)):
    a[i].append(sum(a[i]))
aa=[sum([a[i] for a in a]) for i in range(m+1)]
bs=[[sum([j for j in a if j!=0])for a in b]for b in a]+[aa]
for i in bs:print(" ".join(map(str,i)))