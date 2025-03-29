import sys
r, c = map(int, sys.stdin.readline().split())
a= [0]*(c+1)
for _ in range(r):
    v = list(map(int, sys.stdin.readline().split()))
    a=[x + y for x,y in zip(a,v)]
print(*a)