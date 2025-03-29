Here is the refactored version of the original Python program:

a,b = [],[]
while True:
    x,y=map(int,input().split())
    if not (x==0 and y==0):
        a.append(x)
        b.append(y)
for i in range(len(a)):
    if a[i]>=b[i]:
        print(*reversed([b[i],a[i]]))
    elif a[i]<b[i]:
        print(*reversed([a[i],b[i]]))