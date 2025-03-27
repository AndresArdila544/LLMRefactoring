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
        
        ab = a + b
        
        if ab >= x:
            break
        
        abc = ab + c
        
        if abc == x:
            cnt += 1
    
    print(cnt)