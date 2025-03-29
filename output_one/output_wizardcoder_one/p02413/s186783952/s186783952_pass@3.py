```python
import math
r,c=map(int,input().split())
a = []
for i in range(r):
    a.append([sum(list(map(int, input().split()))]+[sum(a)])
print(*a[0][:-1])
print(*[sum(row) for row in zip(*a)[::-1]])
```