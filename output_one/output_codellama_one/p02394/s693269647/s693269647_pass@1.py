Here is the refactored version of the original code:

import math
def inRect(W, H, x, y, r):
    return (0 <= x-r <= W and 0 <= y-r <= H)
print('Yes' if inRect(*map(int, input().split())) else 'No')