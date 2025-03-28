```python
import math
a, b, c = map(float, input().split())
s = 0.5 * a * b * math.sin(math.radians(c))
l = a + math.sqrt((a**2) + (b**2 - 2*a*b*math.cos(math.radians(c)))
h = 2 * s / a 
print(s, l, sep='\n')
```