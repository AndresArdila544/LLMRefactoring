import math

while True:
    N = int(input())
    if N == 0:
        break
    lst = list(map(int, input().split()))
    avr = sum(lst) / len(lst)
    cal = sum((x - avr) ** 2 for x in lst)
    print(math.sqrt(cal / N))