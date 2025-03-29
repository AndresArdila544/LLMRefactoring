```python
while True:
    try:
        a, b = list(map(int, input().split()))
        if a == 0 and b == 0:
            break
        count = sum([1 for i in range(a) for j in range(a+1-i) for k in range(a-j) if i + j + k == b])
        print(count)
    except ValueError:
        continue
```