r,c=map(int,input().split())
a=[list(map(int,input().split())) for i in range(r)]
b=[[0]*(c+1) for i in range(r+1)
for i in range(r):
  b[i]=[a[i][j]+b[i][j]+b[i][-1]+b[-1][j] for j in range(c+1)]
print(*b)