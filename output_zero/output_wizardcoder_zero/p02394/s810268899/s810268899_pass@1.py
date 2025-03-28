```python
def is_within_circle(w, h, x, y, r):
    return "Yes" if 0 <= x - r <= w and 0 <= y - r <= h else "No"
```