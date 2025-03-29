The original code is already quite concise and readable, but here's a refactored version with fewer lines:

```python
import math
while True:
    n = int(input())
    if n == 0:
        break
    
    b = list(map(int, input().split()))
    ave = sum(b) / n
    p = math.sqrt(sum((ave - x) ** 2 for x in b)) / n
    print("{:.8f}".format(p))
```