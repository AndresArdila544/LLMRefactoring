import sys
for a in (line for line in sys.stdin if line != '0 0'):
    print(*sorted(map(int,a.split())))