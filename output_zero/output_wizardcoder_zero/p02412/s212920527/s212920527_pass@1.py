```python
while True:
    count = 0
    n, x = map(int, input().split())
    if not n and not x:
        break
    for a in range(1, n):
        for b in range(a+1, n):
            c = x - (a + b)
            if 0 < c <= n:
                count += 1
    print(count)
```