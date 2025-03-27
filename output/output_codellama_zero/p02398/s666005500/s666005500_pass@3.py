a,b,c = map(int,input().split())
for n in range(a,b+1):
    if c%n==0:
        x+=1
print(x)