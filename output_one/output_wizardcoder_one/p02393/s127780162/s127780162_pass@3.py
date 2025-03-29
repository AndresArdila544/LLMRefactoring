```python
import math
x = input().split()
m = map(int, x)
a, b, c = sorted(m)
print(*sorted(m))