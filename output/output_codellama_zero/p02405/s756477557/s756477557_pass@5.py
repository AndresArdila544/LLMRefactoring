import sys
blk_wh = '#.' * 151
while True:
    h, w = map(int, sys.stdin.readline().split())
    if not (h and w): break

    for row in range(h):
        print(blk_wh[:w] if row % 2 == 0 else blk_wh[1:w+1])
    print()