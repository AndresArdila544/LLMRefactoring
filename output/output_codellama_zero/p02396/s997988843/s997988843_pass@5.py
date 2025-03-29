import sys

for n, i in enumerate(sys.stdin.readlines()):
    if int(i) != 0:
        print('Case ', n+1, ': ', i)