```python
import math 
a, b = map(int, input().split())
count = 0
for i in range(1, b+1):
    if (b % i) == 0 and (c % i) == 0:
        count += 1
print(count)
```