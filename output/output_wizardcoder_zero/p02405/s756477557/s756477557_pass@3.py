```python
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    blk_wh = '#.' * 151
    for i in range(h):
        print(blk_wh[:w+1] if i % 2 == 0 else blk_wh[1:w+1])
```