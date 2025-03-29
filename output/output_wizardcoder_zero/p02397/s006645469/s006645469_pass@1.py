```python
import sys
for a in sys.stdin:
    if a == '0 0': break
    print(*sorted(map(int,a.split()))
```

Refactored version:

```python
import sys
while True:
    line = input()
    if line == '0 0': 
        break
    else:
        print(*sorted(map(int,line.split()))
```