from __future__ import division, print_function
from sys import stdin
while True:
    n, x = (int(s) for s in stdin.readline().split())
    if n == 0 and x == 0:
        break
    n += 1
    cnt = sum(a + b >= x for a in range(1, n) for b in range(a+1, n))
    print(cnt)