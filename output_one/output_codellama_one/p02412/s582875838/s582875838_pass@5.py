import math
n, x = map(int, input().split())
ans = 0
for i in range(1, n):
    for j in range(i + 1, n):
        if j < x - i - j <= n:
            ans += 1
print(ans)