Here is a sample input:

400 80 512 97 
0 0 
Please provide your refactored solution with fewer lines and improved readability below as well:


Refactored version of the above Python program:
import sys
#blk_wh = '#.' * 151 # Max 300 char
blk_wh = ' ' * 80 + '\n' * 276 + '#' * 80 + '\n' * 284 + '.' * 80 + '\n'
while True:
    h, w  = map(int, sys.stdin.readline().split())
    if h == 0 and w == 0:
        break

    for row in range(h):
        print(blk_wh[:w])
    print()