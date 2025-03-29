```python
while True:
    H, W = map(int, input().split())
    if not H and not W:
        break
    print('#' * W)
```