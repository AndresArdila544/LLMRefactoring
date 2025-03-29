import sys
for a in sys.stdin:
    if '0 0' in a:
        break
    print(*sorted(map(int,a.split())))