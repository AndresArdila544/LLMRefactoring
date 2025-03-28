```python
import math
a,b = map(float,input().split())
s = 0.5*a*b*math.sin(math.radians(c))
l = a+math.sqrt((a**2 + b**2 - 2*a*b*math.cos(math.radians(c)))
h = s/a
print(s, l, h, sep='\n')
```