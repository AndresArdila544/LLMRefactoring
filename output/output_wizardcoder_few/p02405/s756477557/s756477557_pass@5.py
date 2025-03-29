```python
import sys

blk_wh = '#.' * 151
while True:
    h, w = map(int, sys.stdin.readline().split())
    if not (h or w): break
    for row in range(0, h, 2):
        print(blk_wh[:w+1] if row % 2 == 0 else blk_wh[1:w])
```