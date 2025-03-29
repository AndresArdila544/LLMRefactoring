```python
import math

a, b, C = map(float, input().split())
print("%f"%((1/2*a*b*math.sin(math.radians(C)))*(1+2*(1-math.cos(math.radians(C))/(a**2+b**2)))**0.5))
```