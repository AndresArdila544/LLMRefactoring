```python
import sys

while True:
    h, w = map(int, input().split())
    if not h and not w:
        break
    blk_wh = '#.' * 151
    for row in range(h):
        if row % 2 == 0:
            print(blk_wh[:w])
        else:
            print(blk_wh[1:w+1])
```