Here is the refactored version of the code:

import math
a, b, angle = map(int, input().split())
rad = (angle / 180) * math.pi
c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)) ** 0.5
s = (a+b+c)/2
S = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"{S:.5f}")
print(f"{(a+b+c):.5f}")
print(f"{((2*S)/a):.5f}")