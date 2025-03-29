```python
import math
n = int(input())
while n != 0:
    x = float(input().split()[1])
    cnt = sum([i for i in range(1, n) if i < x and (i+j) + k < x for j in range(n-i) for k in range(n-i-j)])
    print(cnt)
    n = int(input())
```