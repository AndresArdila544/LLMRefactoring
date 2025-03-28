```python
import math
from typing import Tuple

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
def distance(u: Point, v: Point) -> float:
    return math.sqrt((u.x - v.x) ** 2 + (u.y - v.y) ** 2)

try:
    u_coords = tuple(float(e) for e in input().split())
except ValueError:
    raise ValueError("Invalid input")
    
u, v = Point(*u_coords[:2]), Point(*u_coords[2:])
print(distance(u, v))
```