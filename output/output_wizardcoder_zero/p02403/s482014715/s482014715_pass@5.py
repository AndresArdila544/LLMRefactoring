```python
while True:
    h, w = map(int, input().split())
    if h == 0:
        break
    print('#' * w)
    for _ in range(h - 1):
        print()
```