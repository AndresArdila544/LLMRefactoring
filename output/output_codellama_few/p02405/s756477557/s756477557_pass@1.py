import sys

blk_wh = '#.' * 151  # Max 300 char
while True:
    h, w = map(int, sys.stdin.readline().split())
    if not (h and w):
        break
    
    for row in range(h):
        print((blk_wh * w).replace('#', blk_wh[0] if row % 2 else blk_wh[1]))