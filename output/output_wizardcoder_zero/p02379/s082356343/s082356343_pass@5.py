```python
import math

x1, y1, x2, y2 = map(float, input().split())
print(math.hypot(abs(x1 - x2), abs(y1 - y2)))  # use the abs() function to get absolute values of dx and dy before passing them as arguments to hypot()
```
This code will output the distance between two points (x1, y1) and (x2, y2). It uses fewer lines than the original program while also improving readability by using Python's built-in abs() function to get absolute values of dx and dy.