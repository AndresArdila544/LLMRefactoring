while True:
    N = int(input())
    if not N:
        break
    
    lst = [int(x) for x in input().split()]
    avr = sum(lst)/len(lst)
    cal = 0
    for x in lst:
        cal += (x-avr)**2
    print(math.sqrt(cal/N))