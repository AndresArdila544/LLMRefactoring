Here is a refactoring of the original program to reduce its complexity and improve its readability:

from math import pi, sqrt

a, b, angle = map(int, input().split())

rad = (angle / 180) * pi
c = ((a ** 2 + b ** 2 - 2 * a * b * cos(rad)) ** 0.5).round(4)
s = (a + b + c) / 2
S = sqrt((s * (s - a) * (s - b) * (s - c)))
print(f"{S:.5f}")
print(f"{a + b + c:.5f}")
print(f"{(2 * S) / a:.5f}")