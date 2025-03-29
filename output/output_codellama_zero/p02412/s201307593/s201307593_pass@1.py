Here is the refactored version of the original program:

while True:
    n, x = [int(i) for i in input().split()]
    if n == 0 and x == 0:
        break
    ans = sum((i + j + k == x for i in range(1, n+1) for j in range(i+1, n+1) for k in range(j+1, n+1)))
    print(ans)