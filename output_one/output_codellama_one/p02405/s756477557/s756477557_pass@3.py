```
import sys

blk_wh = '#.' * 151  # Max 300 char
while True:
    h, w = map(int, sys.stdin.readline().split())
    if h == 0 and w == 0:
        break
    for row in range(h):
        if row % 2 == 0:
            print(blk_wh[:w])
        else:
            print(blk_wh[1:w+1])
```