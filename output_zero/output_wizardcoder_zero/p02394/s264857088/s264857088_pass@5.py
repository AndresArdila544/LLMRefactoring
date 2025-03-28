```python
W, H, x, y, r = map(int, input().split())
if all([x - r >= 0, x + r <= W, y - r >= 0, y + r <= H]): print("Yes") else: print("No") 
```