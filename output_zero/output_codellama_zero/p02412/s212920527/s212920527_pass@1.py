# Refactored code
while True:
    n, x = map(int, input().split())
    if not (n and x): break
    max_a = x // 3
    count = sum(1 for a in range(1, n-1) \
        for b in range(a + 1, n) \
            if c := x - a - b > 0 and c <= n and c > b)
    print(count)