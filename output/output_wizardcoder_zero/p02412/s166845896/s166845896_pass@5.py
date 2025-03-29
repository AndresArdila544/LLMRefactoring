```python
while True:
    try:
        n, x = map(int, input().split())
        if n == 0:
            break
        count = sum((a + b + c == x) for a in range(1, n) for b in range(n - a) for c in range(n - a - b))
        print(count)
    except ValueError:
        pass
```