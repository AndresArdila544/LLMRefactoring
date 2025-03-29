```python
import sys
import math

while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break

    blk_wh = '#.' * 151 # Max 30 char
    for row in range(h):
        print((blk_wh[:w] if row % 2 == 0 else blk_wh[1:w+1])
```

I believe this is the refactored version of the code you're looking for. It uses ternary operator to check for even and odd rows and print appropriate string.
```python
#!/usr/bin/python3
import sys

blk_wh = '#.' * 151 # Max 30 char
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break

    for row in range(h):
        print((blk_wh[:w] if row % 2 == 0 else blk_wh[1:w+1])
```
```