```python
import math

a, b = map(float, input().split())
c_rad = math.radians(float(input()))
L = a + b + (math.sqrt((a**2) + (b**2 - 2*a*b*math.cos(c_rad)))
S = (a * b * math.sin(c_rad)) / 2
H = (2*S)/a
print(f"{S}\n{L}\n{H}")
```