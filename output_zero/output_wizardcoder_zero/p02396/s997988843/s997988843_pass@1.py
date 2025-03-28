import sys

for n, i in enumerate(sys.stdin.readlines(), start=1):
    print('Case', n, ': ', i, sep='') if int(i) != 0 else break