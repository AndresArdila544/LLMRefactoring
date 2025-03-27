import math

while True:
    N = int(input())
    if N==0:
        break
    
    lst = [int(x) for x in input().split()]

    avr = sum(lst)/N

    cal = 0
    for x in lst:
        cal += (x-avr)**2
    print(math.sqrt(cal/N))
