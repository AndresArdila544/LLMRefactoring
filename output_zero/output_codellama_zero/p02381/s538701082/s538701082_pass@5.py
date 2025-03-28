import math

while True:
    N = int(input())
    if N == 0:
        break
    
    lst = [int(x) for x in input().split()]

    cal = sum((x-sum(lst)/N)**2 for x in lst)

    print(math.sqrt(cal/N))