import sys
from math import factorial
n = int(input())
for i in range(1, n+1):
    cnt = 0
    for a in range(1, i):
        if a >= x:
            break
        for b in range(a+1, i):
            ab = a + b
            if ab >= x:
                break
            for c in range(b+1, i):
                abc = ab + c
                if abc == x:
                    cnt += 1
                    break
                if abc > x:
                    break
    print(cnt)