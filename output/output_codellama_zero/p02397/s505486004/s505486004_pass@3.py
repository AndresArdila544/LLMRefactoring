import sys
for line in sys.stdin:
    x, y = map(int, line.split())
    if x == 0 and y == 0:
        break
    print(x, y)