n=int(input())
a=[[0]*10 for _ in range(4)]
for i in range(n):
    b,f,v = map(int, input().split())
    a[b-1][f-1]+=v
for r in a: print(*r)
'''