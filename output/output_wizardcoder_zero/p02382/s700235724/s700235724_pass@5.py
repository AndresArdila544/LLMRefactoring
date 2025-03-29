```python
import math

dim = int(input().strip())
vec_x = list(map(int, input().split()))
vec_y = list(map(int, input().split()))

dist_1 = 0
tmp_dist_2 = 0
tmp_dist_3 = 0
max_xy = float('-inf')
for i in range(dim):
    abs_xy = abs(vec_x[i] - vec_y[i])
    dist_1 += abs_xy
    tmp_dist_2 += abs_xy ** 2
    tmp_dist_3 += abs_xy ** 3
    max_xy = max(max_xy, abs_xy)

dist_2 = math.sqrt(tmp_dist_2)
dist_3 = (tmp_dist_3)**(1/3)
print("{:.5f}\n{:.5f}\n{:.5f}\n{:.5f}".format(dist_1, dist_2, dist_3, max_xy))
```