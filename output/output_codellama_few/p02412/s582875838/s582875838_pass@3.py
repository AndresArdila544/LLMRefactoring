Here is the refactored version of the code:

n = int(input())
while n + x != 0:
    ans = sum(i for i in range(1, n) if any(j in range(x - i - j, n) for j in range(i + 1, n)))
    print(ans)