n,m = map(int,input().split())
a=[[0]*m for i in range(n)]
for i in range(n): a[i] = list(map(int, input().split()))
k = int(input())
s=[0]*n
for i in range(n):
    s[i]=sum([a[i][j]*k for j in range(m)])
print(*s,sep="\n")