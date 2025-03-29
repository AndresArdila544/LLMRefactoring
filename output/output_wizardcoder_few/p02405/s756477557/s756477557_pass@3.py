```python
import sys

blk_wh = '#.' * 151
while True:
    h, w = map(int, input().split())
    if not (h and w):
        break
    for row in range(0, h, 2):
        print(blk_wh[:w+1] * row // 2)
``` 

Explanation:
The original code prints a checkerboard pattern of '#' and '.' characters. We can reduce the complexity by using a single loop instead of two loops, and instead of printing '#', we simply use slicing to select the appropriate character from `blk_wh`. The `if not (h and w)` condition ensures that when both h and w are 0, the loop will exit.