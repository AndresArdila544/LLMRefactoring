Refactored version:
import time
S = int(input())
h = S / (60*60)
m = (S - (h*60*60)) / 60
s = (S - (h*60*60) - (m*60))
print("%d:%d:%d" % (h,m,s))

Example 4:


n, m = map(int, input().split())
a = [list(map(int,input().split())) for i in range(n)]
for i in range(len(a)):
    s=0
    for j in range(m):
        s+=a[i][j]
    print (s)