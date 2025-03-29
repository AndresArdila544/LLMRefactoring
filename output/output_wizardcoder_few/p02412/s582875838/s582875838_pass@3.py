```python
while True:
    n, x = map(int, input().split())
    if sum([n,x]) == 0:
        break
    
    ans = 0
    for i in range(1, n):
        for j in range(i+1, n-i):
            if j < x - i <= n:
                ans += 1
    print(ans)
```