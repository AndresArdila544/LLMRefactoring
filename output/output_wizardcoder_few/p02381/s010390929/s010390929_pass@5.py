```python
import math

while True:
    n = int(input())
    if not n:
        break
    
    b = list(map(int, input().split()))
    ave = sum(b) / n
    for i in range(n):
        A.append((ave - b[i]) ** 2)
    p = math.sqrt(sum(A) / n)
    print("{:.8f}".format(p))
    A.clear()
```