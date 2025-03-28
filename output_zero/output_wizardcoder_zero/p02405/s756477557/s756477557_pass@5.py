```python
import sys

while True:
    h, w = map(int, sys.stdin.readline().split())
    if not (h or w):
        break
    blk_wh = '#.' * 151 # Max 30 char
    for i in range(h):
        print(blk_wh[:w+1] if i%2 == 0 else blk_wh[1:w+1]) 
```