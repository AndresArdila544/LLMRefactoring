```python
w, h, x, y, r = map(int, input().split())
if (x >= r and x <= w - r) and (y >= r and y <= h - r):
    print("Yes")
else:
    print("No")
```