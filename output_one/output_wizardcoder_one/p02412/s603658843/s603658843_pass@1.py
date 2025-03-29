```python
import sys
from math import hypot
while True:
    try:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            break
        cnt = 0
        for a in range(1, n):
            for b in range(a+1, n-1):
                abc = hypot(a,b)
                if abc >= x:
                    cnt += 1
        print(cnt)
    except EOFError:
        break
``` 

Explanation:

We can use the built-in `hypot` function from the `math` module to calculate the distance between two points in a straight line. We only need to loop through the values of `a` and `b` such that `a+b <= x`. The condition `a >= x` is redundant as it is already covered by `a < x` and `b < x` because we are checking pairs of distinct numbers.

We also use a try-except block to catch the EOF error when there is no more input left. This ensures that we can stop the loop when we have processed all inputs.