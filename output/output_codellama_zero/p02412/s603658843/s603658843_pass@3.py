Here is a refactored version of the original Python program:

from __future__ import division, print_function
from sys import stdin
while True:
    n, x = (int(s) for s in stdin.readline().split())
    if n == 0 and x == 0:
        break
    cnt = 0
    for a in range(1, n):
        if a >= x:
            break
        ab = a + a
        if ab >= x:
            break
        for b in range(a+1, n):
            abc = ab + b
            if abc == x:
                cnt += 1
                break
    print(cnt)