```python
import math
while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    for i in range(H):
        print("#" * (W + 2 if i == 0 or i == H - 1 else "#" + "." * (W - 2) + "#")
print()
```

The code can be reduced to a single line using the ternary operator in Python and avoiding unnecessary iterations.
```python
import math
while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    print("#" * (W + 2 if i == 0 or i == H - 1 else "#" + "." * (W - 2) + "#")
```