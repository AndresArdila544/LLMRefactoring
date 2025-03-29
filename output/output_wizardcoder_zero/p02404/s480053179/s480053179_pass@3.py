```python
import sys

def sa(Type= int):
    return list(map(Type, input().split()))

while True:
    h, w = sa()
    if not all(h and w):
        break
    row = ['#'*(w+2)]
    frame = ['#'.join(row[:1]+['.']*w+row[-1:] for _ in range(h+2)]
    print('\n'.join(frame))
```