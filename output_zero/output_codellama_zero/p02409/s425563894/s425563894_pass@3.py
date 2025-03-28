n=int(input())
a=[[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

for i in range(n):
    b,f,r,v=map(int,input().split())
    a[b-1][f-1][r-1]+=v

for c in range(4):
    for d in range(3):print('{:02d}'.format(a[c][d][r]),end='')
    if c != 3:print('#' * 20)