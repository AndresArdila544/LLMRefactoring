```python
import math
from itertools import zip_longest

n = int(input())
for i in range(1, n+1):
    if i % 3 == 0 or '3' in str(i):
        print('', i, end='')
print()

A_lst = [int(x) for x in input().split()]
B_lst = [int(x) for x in input().split()]
chebyshev = max(abs(a - b) for a, b in zip_longest(A_lst, B_lst))
print("{:.6f}".format(math.hypot(*A_lst)))
print("{:.6f}".format(chebyshev**2))
print("{:.6f}".format(chebyshev**3))
```