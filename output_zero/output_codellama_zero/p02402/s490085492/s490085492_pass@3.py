Here is the refactored version of the original Python program:

import sys

n = list(map(int, sys.stdin.readlines()[1].split(" ")))

print("{0} {1} {2}".format(min(n), max(n), sum(n)))