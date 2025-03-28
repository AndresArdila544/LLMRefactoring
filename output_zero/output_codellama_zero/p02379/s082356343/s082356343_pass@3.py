Here's the refactored code:

import math

x1, y1, x2, y2 = map(float, input().split())
print(math.hypot(dx:=x1-x2, dy:=y1-y2))

This code uses assignment expressions to calculate dx and dy and then passes them as arguments to the hypot function in one line.