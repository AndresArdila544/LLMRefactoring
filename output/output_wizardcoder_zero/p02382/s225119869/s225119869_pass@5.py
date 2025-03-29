n = int(input())
xlist = list(map(int, input().split()))
ylist = list(map(int, input().split()))
d1 = sum(abs(x - y) for x, y in zip(xlist, ylist))
d2 = sum((x - y)**2 for x, y in zip(xlist, ylist) ** 0.50
d3 = sum(abs(x - y)**3 for x, y in zip(xlist, ylist)) ** (1/3)
dinf = max(max(abs(x - y) for x, y in zip(xlist, ylist)))