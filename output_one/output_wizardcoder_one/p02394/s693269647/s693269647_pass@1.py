```python
def inRect(W, H, x, y, r):
    if not (0 <= x-r <= W and 0 <= y-r <= H) or not (0 <= x+r <= W and 0 <= y+r <= H):
        return False
    
    return True

print('Yes' if inRect(*map(int, input().split())) else 'No')
```