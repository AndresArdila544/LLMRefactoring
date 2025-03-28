```python
import math

def std_dev(lst):
    avr = sum(lst) / len(lst)
    return math.sqrt(sum((x - avr) ** 2 for x in lst) / len(lst))

while True:
    N = int(input())
    if N == 0:
        break
    lst = [int(x) for x in input().split()]
    print(std_dev(lst))
```