n, x = map(int, input().split())
while n + x != 0:
    ans = sum([1 for i in range(1, n) for j in range(i+1, n) if j < x - i - j <= n])
    print(ans)
    n, x = map(int, input().split())