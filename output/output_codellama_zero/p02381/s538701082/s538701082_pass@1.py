Here is a refactoring of the original program in fewer lines:

import math

while True:
    N = int(input())
    if N == 0:
        break
    
    avr, cal = sum(map(int, input().split())) / N, 0
    
    print(math.sqrt(cal/N))