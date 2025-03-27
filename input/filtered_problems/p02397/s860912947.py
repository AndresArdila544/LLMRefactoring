a = []
b = []
while True:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    else:
        a.append(x)
        b.append(y)
        
for i in range(0,len(a)):
    if a[i] >= b[i]:
        print(b[i],a[i])
    elif a[i] < b[i]:
        print(a[i],b[i])