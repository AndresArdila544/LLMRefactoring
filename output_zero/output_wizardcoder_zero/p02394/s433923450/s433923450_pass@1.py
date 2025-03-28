```python
def is_circle_in_rectangle(w, h, x, y, r):
    return "Yes" if (0 <= x - r <= w and 0 <= y - r <= h) else "No"

W, H = map(int, input().split())
print(is_circle_in_rectangle(W,H,x,y))