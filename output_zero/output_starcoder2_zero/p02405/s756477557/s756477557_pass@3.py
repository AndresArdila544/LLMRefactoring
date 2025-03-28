Below is my solution:
# #!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys 

blk_wh = '#.' * 151 # Max 300 char
while True:
    h, w = map(int, sys.stdin.readline().split())
    if h == 0 and w == 0:
        break

    for row in range(h):
        print((blk_wh[:w] + blk_wh[1:w+1])[row % 2::2])
    print()