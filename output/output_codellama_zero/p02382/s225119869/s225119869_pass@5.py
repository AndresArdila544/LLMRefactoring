n = int(input())
xlist = list(map(int, input().split()))
ylist = list(map(int, input().split()))
d1 = sum([abs(x - y) for x, y in zip(xlist, ylist)])
d2 = sum([(x - y)**2 for x, y in zip(xlist, ylist)])**0.50
d3 = sum([(x - y)**3 for x, y in zip(xlist, ylist)])**(1/3)
dinf = max([abs(x - y) for x, y in zip(xlist, ylist)])
print(*[i for i in (d1, d2, d3, dinf)], sep='\n')