Here's a refactored version of the code:

import math

dim = int(input().strip())
vec_x = list(map(int, input().strip().split(" ")))
vec_y = list(map(int, input().strip().split(" ")))
abs_xy = [abs(i - j) for i, j in zip(vec_x, vec_y)]
dist_1 = sum(abs_xy)
tmp_dist_2 = sum([pow(i, 2) for i in abs_xy])
dist_2 = math.sqrt(tmp_dist_2)
dist_3 = pow(max(abs_xy), 1/3)
dist_infinite = max(abs_xy)
print("{:.5f}\n{:.5f}\n{:.5f}\n{:.5f}".format(dist_1, dist_2, dist_3, dist_infinite))