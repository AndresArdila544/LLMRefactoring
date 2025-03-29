import math
n,c=map(int,input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    a[i]+=[sum(a[i])]
print(*a[i])
a=list(zip(*a[::-1]))

for i in range(c):print(sum(a[i]),end=' ')
print(sum(a[c]))