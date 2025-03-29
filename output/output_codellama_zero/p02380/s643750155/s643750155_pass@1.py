import math

a, b, c = map(int, input().split())
if c <= 90:
    C = max(a, b)
    B = min(a, b)
    X = (B ** 2 - h * h) ** 0.5
    print((C - X) ** 2 + h ** 2) ** 0.5
else:
    A = a - b * math.cos(math.radians(c))
    x = (b ** 2 - h * h) ** 0.5
    C = ((A) ** 2 + h ** 2) ** 0.5
    print((C + a + b) ** 2 + h ** 2) ** 0.5