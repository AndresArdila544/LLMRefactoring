n = int(input())
while n != 0:
    x = int(input())
    ans = sum([i for i in range(1, n) for j in range(i+1, n) if (j < x - i - j <= n)]
print(ans)