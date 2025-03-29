import sys
for line in sys.stdin:
    s = line.strip()
    if s != '0':
        print(sum(map(int, s)))