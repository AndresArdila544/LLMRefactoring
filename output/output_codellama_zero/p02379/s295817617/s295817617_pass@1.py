import math
X1, Y1, X2, Y2 = map(float, input().split())
print(math.hypot(X2 - X1, Y2 - Y1))