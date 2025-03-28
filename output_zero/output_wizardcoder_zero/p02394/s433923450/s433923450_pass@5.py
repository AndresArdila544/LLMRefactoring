```python
W,H,x,y,r = map(int, input().split())
print("Yes") if (0 <= x - r <= W and 0 <= y - r <= H) else print("No")
```

This version uses a ternary operator to simplify the conditional statement. It first maps the input values into the variables `W`, `H`, `x`, and `y` using the `map()` function, then checks if the condition `(0 <= x - r <= W)` and `(0 <= y - r <= H)` is true or false, and prints "Yes" or "No", respectively.