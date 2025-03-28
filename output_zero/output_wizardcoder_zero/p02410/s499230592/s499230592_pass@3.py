n,m = map(int,input().split())
a=[[0]*m for i in range(n)]
for _ in range(n): a.append([*map(int,input().split())] * m)
k=int(input())
[print(sum(x)*k) for x in a]