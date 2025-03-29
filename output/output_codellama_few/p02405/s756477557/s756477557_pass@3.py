import sys

blk_wh = '#.' * 151  # Max 300 char
while True:
    h, w = map(int, sys.stdin.readline().split())
    if not h or not w:
        break
    
    for row in range(h):
        print(blk_wh[:w] if row % 2 else blk_wh[1:w+1])
    print()