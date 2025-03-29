```python
from __future__ import division, print_function
n = int(input())
while True:
    x = int(input())
    if not (n or x):
        break
    cnt = 0
    for a in range(1, n):
        for b in range(a+1, n):
            ab = a + b
            for c in range(b+1, n):
                abc = ab + c
                if abc == x:
                    cnt += 1
                    break
                elif abc > x:
                    break
    print(cnt)
``` 
```python
def count_triplets(n):
    cnt = 0
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            ab = a + b
            for c in range(b+1, n+1):
                abc = ab + c
                if abc <= n:
                    cnt += 1
                else:
                    break
    return cnt

while True:
    x = int(input())
    if not (x == 0):
        print(count_triplets(x))
    elif n == 0:
        break
``` 
```python
def count_triplets(n, x=None):
    cnt = 0
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            ab = a + b
            if not x or ab < x:
                for c in range(b+1, n+1):
                    abc = ab + c
                    if abc == x:
                        cnt += 1
                        return cnt
                    elif abc > x:
                        break
    return cnt
while True:
    n = int(input())
    x = int(input())
    if not (n or x):
        break
    print(count_triplets(n, x))
```