while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    ans = sum(i+j+k == x for i in range(1, n+1) for j in range(i+1, n+1) for k in range(j+1, n+1))
    print(ans)