```python
import sys
n = list(map(int, sys.stdin.readline().split()))
print("{} {} {}".format(min(n), max(n), sum(n)))