```python
from sys import stdin
w = input().lower()
counter = sum(1 for i in map(str.lower, stdin.readline().split()) if w == i)
print(counter)
```