while True:
    n, x = map(int, input().split(' '))
    if n == x == 0: break
    count = sum(1 for a in range(1, n-1) for b in range(a + 1, n) if (x - a - b) > b and (x - a - b) <= n)
    print(count)