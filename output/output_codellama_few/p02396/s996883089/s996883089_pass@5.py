import sys
while True:
    x = int(sys.stdin.readline())
    if x != 0:
        print('Case {}: {}'.format(count, x))
        count += 1
    else:
        break