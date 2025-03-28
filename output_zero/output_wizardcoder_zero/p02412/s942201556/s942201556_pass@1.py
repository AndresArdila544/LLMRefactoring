```python
import math
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0
    u = math.ceil(x/3)
    while u<=n and u<=x-3:
        v = (x - u)//2 + 1
        while v < x - u:
            w = (x - u) - v
            if u > v > w:
                count += 1
                # print(u, v, w)
            v+=1
    print(count)
```

```python
import math
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0
    u = math.ceil(x/3)
    for v in range((x-u)//2 + 1, (x-u):
        w = (x - u) - v
        if u > v > w:
            count += 1
            # print(u, v, w)
    print(count)
```