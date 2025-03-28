```python
import math
dim = int(input().strip())
vec_x = list(map(int, input().split()))
vec_y = list(map(int, input().split()))
dist_1 = 0
dist_2 = 0
dist_3 = 0
max_xy = max([abs(a-b) for a, b in zip(vec_x, vec_y)] if len(set(vec_x)) == dim and len(set(vec_y)) == dim else float('inf')
for i in range(dim):
    dist_1 += abs(vec_x[i] - vec_y[i])
    dist_2 += (abs(vec_x[i] - vec_y[i]) ** 2)
    dist_3 += (abs(vec_x[i] - vec_y[i]) ** 3
print("{:.5f}\n{:.5f}\n{}".format(dist_1, math.sqrt(dist_2), dist_3**(1/3) if max_xy != float('inf') else max_xy)
```

Explanation: 
We can use `zip` to iterate over both vectors in parallel and calculate the distance as we go along, avoiding the need for a separate list to store distances. We also calculate `dist_infinite` using a list comprehension that checks if all elements of `vec_x` and `vec_y` are unique (i.e., they form a vector space). If not, it returns infinity instead.

The output format has been simplified to only print the required values separated by newlines.
```python
import math
dim = int(input().strip())
vec_x = list(map(int, input().split()))
vec_y = list(map(int, input().split()))
dist_1 = 0
dist_2 = 0
max_xy = max([abs(a-b) for a, b in zip(vec_x, vec_y)] if len(set(vec_x)) == dim and len(set(vec_y)) == dim else float('inf')
for i in range(dim):
    dist_1 += abs(vec_x[i] - vec_y[i])
    dist_2 += (abs(vec_x[i] - vec_y[i]) ** 2)
dist_3 = dist_2 ** (1/3) if max_xy != float('inf') else max_xy
print("{:.5f}\n{:.5f}\n{}".format(dist_1, math.sqrt(dist_2), dist_3))
```