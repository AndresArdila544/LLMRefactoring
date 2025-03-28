Original solution by @daveb:
r,c=map(int,input().split())
a=[list(map(int,input().split())) for i in range(r)]
for i in range(r):
    a[i].append(sum(a[i]))
for i in range(len(a)+1):
   b=[0]*c+[sum([row[i] for row in a])]
for i in range(len(b)): print(*b)