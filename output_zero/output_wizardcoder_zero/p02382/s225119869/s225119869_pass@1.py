```python
import math

n = int(input())
xlist = list(map(int, input().split()))
ylist = list(map(int, input().split()))
print(sum([abs(i-j) for i, j in zip(xlist, ylist)]))
print((sum([(i-j)**2 for i, j in zip(xlist, ylist)])**0.5)
print((sum([(i-j)**3 for i, j in zip(xlist, ylist)])**(1/3))
print(max([abs(i-j) for i, j in zip(xlist, ylist)])
```