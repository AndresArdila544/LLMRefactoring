while True:
    count = 0
    n, x = map(int, input().split(' '))
    if n == x == 0:
        break
    max_a = x // 3
    for a in range(1, n-1):
        for b in range(a + 1, n):
            c = x - a - b
            if c > 0 and c <= n and c > b:
                count += 1
    print(count)
