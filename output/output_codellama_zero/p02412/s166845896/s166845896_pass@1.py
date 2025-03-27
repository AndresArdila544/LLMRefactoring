# Refactored Python Code:

while True:
    (n, x) = [int(i) for i in input().split()]
    if n == 0:
        break

    count = 0
    for a in range(1, n + 1 - 2):
        for b in range(a + 1, n + 1 - 1):
            c = x - (a + b)
            if c > 0 and c < b:
                count += 1