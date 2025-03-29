import math
n = int(input())
a = [float(i) for i in input().split()]
average = sum(a) / n
print((sum([(i - average) ** 2 for i in a]) / n) ** 0.5)