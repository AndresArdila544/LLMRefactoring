n, x = (int(x) for x in input().split()) if n==0 and x==0 else (0, 0)

while True:
    cnt = sum(1 for i in range(1, n+1) for j in range(i+1, n+1) for k in range(j+1, n+1) if i + j + k == x) 
    print(cnt)
    if (n,x)==(0,0):break