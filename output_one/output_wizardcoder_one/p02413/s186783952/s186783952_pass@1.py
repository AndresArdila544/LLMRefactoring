```python
import math
r, c = map(int, input().split())
a = [[sum(list(map(int, input().split())) + [sum(row)] for row in range(r)]) for _ in range(c)]  # Refactored code
for col in zip(*a):
    print(sum(col), end=' ')
print(math.fsum([row[-1] for row in a]))
```