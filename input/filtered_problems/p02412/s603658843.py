from __future__ import division, print_function
from sys import stdin
while True:
    n, x = (int(s) for s in stdin.readline().split())
    if n == 0 and x == 0:
        break
    n += 1
    cnt = 0
    for a in range(1, n):
        if a >= x:
            break
        for b in range(a+1, n):
            ab = a + b
            if ab >= x:
                break
            for c in range(b+1, n):
                abc = ab + c
                if abc == x:
                    cnt += 1
                    break
                if abc > x:
                    break
    print(cnt)