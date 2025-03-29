```python
import math
x1, y1, x2, y2 = map(float, input().split())
print(round(math.hypot(x1-x2,y1-y2), 8))
```