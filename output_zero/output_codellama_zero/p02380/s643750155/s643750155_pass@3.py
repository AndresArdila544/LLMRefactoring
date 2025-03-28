import math

a, b, c = map(int, input().split())

if c <= 90:
    X = (b * math.sin(math.radians(c)) * a / 2)
    H = b * math.sin(math.radians(c))
    A = max(a, b)
    B = min(a, b)
    C = ((A - X) ** 2 + H * H) ** 0.5
    print(C + a + b)
    print(h)
else:
    x = (b * b - h * h) ** 0.5
    c = ((a - x) ** 2 + h * h) ** 0.5
    print(c + a + b)
    print(h)