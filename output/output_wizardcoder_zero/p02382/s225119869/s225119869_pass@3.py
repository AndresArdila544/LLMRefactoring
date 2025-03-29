import math
n = int(input())
xlist, ylist = list(map(int, input().split())), list(map(int, input().split()))
d1 = sum(abs(x - y) for x, y in zip(xlist, ylist))
d2 = (sum((x - y)**2 for x, y in zip(xlist, ylist)) ** 0.50)
d3 = max(abs(x - y) for x, y in zip(xlist, ylist))
print(*map(round, [d1, d2, math.ceil(d3)]))