Here is a refactored version of the code with fewer lines:

import math
while True:
    n = int(input())
    if n == 0:
        break
    average = sum([float(i) for i in input().split()]) / n
    print((sum([(i - average) ** 2 for i in [float(i) for i in input().split()]]) / n) ** 0.5)