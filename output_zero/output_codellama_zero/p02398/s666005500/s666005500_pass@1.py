a,b,c=map(int,input().split())
x=sum(1 for _ in range(a+1,b+1) if c%_==0)
print(x)