```python
import math

while True:
    n = int(input())
    if n == 0: 
        break
    else:
        b = list(map(int, input().split()))
        ave = sum(b) / n
        A = [(ave - i) ** 2 for i in b]
        p = math.sqrt(sum(A)/n)
        print("{:.8f}".format(p))
```