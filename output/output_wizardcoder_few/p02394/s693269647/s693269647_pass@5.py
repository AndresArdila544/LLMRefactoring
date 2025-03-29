```python
def inRect(W, H, x, y, r):
    return all([0 <= x-r, x+r <= W, 0 <= y-r, y+r <= H])

print('Yes' if inRect(*map(int, input().split())) else 'No')
```