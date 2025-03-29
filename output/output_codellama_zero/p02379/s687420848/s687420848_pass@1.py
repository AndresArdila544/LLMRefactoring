Here is a refactored version of the original program that has fewer lines and improved readability:

import math
x1,y1,x2,y2 = map(float, input().split())
dist=math.hypot((x2-x1),(y2-y1))
print("%.6f" % (dist))