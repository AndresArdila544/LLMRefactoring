```python
import math
r = float(input())
print('{:.6f} {:.6f}'.format(math.pi * r**2, 2*math.pi * r)) # Use format strings to print both values on the same line with less code.
```

This code reduces the number of lines and improves readability by using a single `print()` statement and a more concise formatting expression. The first value is calculated as pi times the square of r, while the second value is calculated as 2 times pi times r. This avoids having to use multiple format() calls or storing intermediate values for each calculation.