Here is a refactored version of the original Python program:

import math

while True:
    N = int(input())
    if N == 0:
        break
    
    lst = list(map(int, input().split()))
    avr = sum(lst) / N
    cal = math.sqrt(sum((x - avr) ** 2 for x in lst) / N)
    print(cal)