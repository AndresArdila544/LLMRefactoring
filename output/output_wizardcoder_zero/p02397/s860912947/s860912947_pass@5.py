```python
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    else:
        if a[-1] >= b[-1]:
            print(b[-1], a[-1])
        elif a[-1] < b[-1]:
            print(a[-1], b[-1])
```