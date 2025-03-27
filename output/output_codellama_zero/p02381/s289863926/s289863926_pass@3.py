import math

while True:
    n = int(raw_input())
    if n == 0: break
    l = map(float, raw_input().split())
    avg = sum(l) / len(l)
    hyo2 = (sum((i - avg) ** 2 for i in l)) / n
    print math.sqrt(hyo2)