import sys

n = sys.stdin.readlines()[1].split(" ")
print("{0} {1} {2}".format(min(map(int, n)), max(map(int, n)), sum(map(int, n))))