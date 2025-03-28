while True:
    n, x = map(int, input().split())
    if n + x == 0:
        break
    ans = sum(1 for i in range(1, n) for j in range(i + 1, n) if j < x - i - j <= n)
    print(ans)