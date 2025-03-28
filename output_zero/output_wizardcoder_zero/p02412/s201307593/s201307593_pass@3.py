n, x = map(int, input().split())
while n > 0 and x > 0:
    ans = sum((i+j+k == x for i in range(1, n+1) for j in range(1, n-i+1) for k in range(1, n-i-j+1))
print(ans)
"""