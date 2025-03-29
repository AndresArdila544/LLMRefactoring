```python
import sys
n = list(map(int, input().split()))
print("{} {} {} {}".format(*[min(n), max(n), sum(n)])) 
```