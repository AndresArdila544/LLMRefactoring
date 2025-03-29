```python
import math

def dist(A_lst, B_lst):
    return [math.hypot(*zip(A_lst,B_lst)), *map(lambda x: abs(x) ** 2, zip(A_lst, B_lst)), max(abs(a-b) for a, b in zip(A_lst, B_lst))]
    
N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
print(*[round(x, 6) for x in dist(A, B)]+["{:.6f}".format(math.hypot(*zip(A,B))])
```