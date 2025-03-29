```python
from sys import stdin
w = input().lower()
print(sum(1 for i in map(str.lower, stdin.read().split()) if i == w)
```