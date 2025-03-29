Refactored Code:
```python
import sys

n = int(sys.stdin.readline())  # Take input as integer
nstr = list(map(int, sys.stdin.readline().split()))
print("{} {} {} {}".format(min(nstr), max(nstr), sum(nstr)))
```