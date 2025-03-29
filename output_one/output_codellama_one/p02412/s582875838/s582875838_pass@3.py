while True:
n,x = map(int,input().split())
if n+x==0:
    break
ans = sum((i*(i-1)/2) for i in range(1,x))
print(ans)