```python
import math
while True:
    try:
        n = int(input())
        if n == 0:
            break
        a = list(map(int, input().split()))
        mean = sum(a) / len(a)
        std = math.sqrt(sum((x - mean) ** 2 for x in a) / len(a))
        print(std)
    except ValueError:
        break
```
```python
import statistics
while True:
    try:
        n = int(input())
        if n == 0:
            break
        a = list(map(int, input().split()))
        print(statistics.pstdev(a))
    except ValueError:
        break
```