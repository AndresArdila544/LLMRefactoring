```
while True:
    n = int(input())
    if n == 0:
        break
    a = [float(i) for i in input().split()]
    average = sum(a) / n
    print((sum([(i - average) ** 2 for i in a]) / n) ** 0.5)
```


Refactored version:

import math
while True:
    try:
        n = int(input())
        if not n:
            break
        a = [float(i) for i in input().split()]
        print(math.sqrt(sum([(i - sum(a)/n)**2 for i in a]))