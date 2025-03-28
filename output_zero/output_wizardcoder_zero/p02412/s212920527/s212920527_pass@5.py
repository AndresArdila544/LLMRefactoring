```python
while True:
    n, x = map(int, input().split(' '))
    if not (n and x):
        break
    count = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            c = x - a - b
            if c > 0:
                count += (c <= n and c > b)
    print(count)
```