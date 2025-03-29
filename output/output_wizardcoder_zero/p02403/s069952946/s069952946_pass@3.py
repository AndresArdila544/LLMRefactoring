```python
while True:
    H, W = map(int, input().split())
    if (H, W) == (0, 0):
        break
    for i in range(1, W+1):
        print("#" * H)
```