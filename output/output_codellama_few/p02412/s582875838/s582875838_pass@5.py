while True:
    n,x = map(int, input().split())
    if n + x == 0:
        break
    ans = sum(i for i in range(1, n) if j < x - i - j <= n for j in range(i+1,n))
    print(ans)