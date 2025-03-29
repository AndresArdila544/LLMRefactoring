import sys
for line in sys.stdin:
    if '0 0' in line: break
    print(*sorted(map(int,line.split())))