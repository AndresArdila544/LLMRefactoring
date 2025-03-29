```python
import sys
for line in sys.stdin:
    if line == '0 0': break
    print(*sorted(map(int,line.split()))
```