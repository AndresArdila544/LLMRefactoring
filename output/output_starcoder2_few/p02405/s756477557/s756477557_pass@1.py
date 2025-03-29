Here is the refactored code:

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
blk  = '#.'*151 # Max 300 char
while True:
    h, w  = map(int, sys.stdin.readline().split())
    if h == 0 and w == 0:
        break
    for row in range(h):
        if row %2 ==0:
            print(blk[:w])
        else:
            print(blk[1:w+1])
    print()