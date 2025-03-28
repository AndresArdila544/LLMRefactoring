This is an example of refactoring; reducing its lines and complexity, while preserving its functionality. Example:

import math
x1, y1, x2, y2 = map(float, input().split())
d  = math.hypot(x1-x2, y1-y2)
print(d)

Refactored version:

import math
x1, y1, x2, y2  = map(float, input().split())
d  = math.hypot(x1-x2, y1-y2)
print(d)