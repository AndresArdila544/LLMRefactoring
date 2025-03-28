while True:
    n, x = map(int, input().split())
    if not (n + x == 0): break
    for i in range(1, n):
        for j in range(i + 1, n):
            if j < x - i - j <= n:
                ans += 1
    print(ans)