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
    print((a[i]>=b[i])*(b[i],a[i]),(a[i]<b[i])*(a[i],b[i]))