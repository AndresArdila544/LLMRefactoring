```python
import math
while True:
    n, x = map(int, input().split())
    if n+x == 0:
        break
    ans = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            if j < x - i - j <= n:
                ans += 1
    print(ans)
```

Refactored version:

```python
import math
while True:
    try:
        n, x = map(int, input().split())
        if n + x == 0:
            break
        else:
            print(sum([1 for i in range(n) for j in range(i+1, n) if j < x - i - j <= n]))
    except EOFError: # This line can be added to avoid the error when no input is given.
        break
```