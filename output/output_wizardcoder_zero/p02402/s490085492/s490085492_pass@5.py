import sys
n = list(map(int, input().split()))[1:]
print("{} {} {} {}".format(min(n), max(n), sum(n)))