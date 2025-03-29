```python
import math
x, y = map(float, input().split())
w, h = map(float, input().split())
r = float(input())

if x > w - r or x < r or y < r or y > h - r:
    print("No")
else:
    print("Yes")
```