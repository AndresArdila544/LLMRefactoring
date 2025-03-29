```python
import math
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(float, input().split()))
    average = sum(a) / n
    print((sum([(i - average) ** 2 for i in a]) / n) ** 0.5)
```