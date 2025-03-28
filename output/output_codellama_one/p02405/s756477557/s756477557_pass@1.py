import sys

blk_wh = '#.' * 151  # Max 300 char
while True:
    h, w = map(int, input().split())
    if not (h and w):
        break

    for row in range(h):
        if row % 2 == 0:
            print(blk_wh[:w])
        else:
            print(blk_wh[1:w+1])
    print()