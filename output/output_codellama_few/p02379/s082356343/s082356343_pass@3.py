Here is a refactored version of the original program:

import math
x1, y1, x2, y2 = map(float, input().split())
print(math.hypot((x1-x2), (y1-y2)))