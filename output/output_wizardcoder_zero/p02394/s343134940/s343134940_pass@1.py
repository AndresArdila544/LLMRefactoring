```
def is_valid(w, h, x, y, r):
    if x-r >= 0 and x+r <= w and y-r >= 0 and y+r <= h:
        return "Yes"
    else:
        return "No"
```