```python
import math
x1, y1, x2, y2 = [float(i) for i in input().split()]
print(math.hypot(x2-x1, y2-y1))