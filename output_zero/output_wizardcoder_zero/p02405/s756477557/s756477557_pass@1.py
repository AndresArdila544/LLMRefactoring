```python
import sys

while True:
    h, w = map(int, input().split())
    if not h and not w:
        break

    for row in range(h):
        if row % 2 == 0:
            print('.' * w)
        else:
            print('#' * (w + 1)[1:]
```