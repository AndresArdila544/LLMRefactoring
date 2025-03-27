import math
while True:
    n = int(input())
    if n == 0:
        break
    a = [float(i) for i in input().split()]
    average = sum(a) / n
    print(math.sqrt(sum((i - average)**2 for i in a)/n))