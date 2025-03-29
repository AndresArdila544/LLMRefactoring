import sys

blk_wh = '#.' * 151
while True:
    h, w = map(int, sys.stdin.readline().split())
    if not h and not w:
        break
    for row in range(h):
        if row % 2 == 0:
            print(blk_wh[:w])
        else:
            print(blk_wh[1:w+1])
    print()