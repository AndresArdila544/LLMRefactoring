Here is the refactored version:

dim = int(input())
a, b = map(int, input().split()), map(int, input().split())
d1 = [abs(x - y) for x, y in zip(a, b)]
print(sum(d1))
d2 = [(x - y)**2 for x, y in zip(a, b)]
d3 = [(abs(x - y))**3 for x, y in zip(a, b)]
print(max(d1), pow(sum(d2), 1/2), pow(sum(d3), 1/3))