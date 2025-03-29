```python
import math
a, b, C = map(int, input().split())
S = 0.5 * a * b * math.sin(math.radians(C))
c = (a**2 + b**2 - 2*a*b*math.cos(math.radians(C))**0.5)
L = a + b + c
h = b * math.sin(math.radians(C))
print("{:.8f}".format(S), end=" ")
print("{:.8f}".format(L), end=" ")
print("{:.8f}\n".format(h))
```