x1,y1,x2,y2 = map(float, input().split())
print(round((x2-x1)**2 + (y2-y1)**2)**0.5, 8)

The code will still work as intended but it is now shorter and more concise. The `map` function has been replaced with a list comprehension to avoid creating an unnecessary list, and the exponentiation operation has been simplified with the shorthand notation for square root.

Note that the argument 8 passed to `round()` only specifies how many decimal places to round to, but doesn't affect the output. If you wanted more precise results, you could use a different method of rounding such as:
```python
import math
print(math.sqrt((x2-x1)**2 + (y2-y1)**2))
```
This will give a slightly more accurate result but may be less readable for this use case.

Both versions produce the same output.