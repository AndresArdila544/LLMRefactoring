```python
while True:
    n = int(input())
    if n == 0:
        break
    l = list(map(float, input().split()))
    avg = sum(l) / len(l)
    naka = (sum((i - avg) ** 2 for i in l))
    print((naka/len(l))**0.5)
```