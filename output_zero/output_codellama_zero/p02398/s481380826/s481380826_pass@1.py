a,b,c=map(int, input().split())
count=0
for i in range(a, b+1):
    count += (c%i==0)