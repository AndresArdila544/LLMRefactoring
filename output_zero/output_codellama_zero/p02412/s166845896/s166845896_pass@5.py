Here is a refactored version of the original Python program:

while True:
    (n, x) = [int(i)for i in input().split()]
    if n == x == 0:
        break

    count = sum(1 for a in range(1, n + 1 - 2)
                   for b in range(a + 1, n + 1 - 1)
                       for c in range(b + 1, n + 1)
                           if (a + b + c) == x)
    print(count)