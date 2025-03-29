import math
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(float, input().split()))
    average = sum(a) / len(a)
    print((sum([(i - average) ** 2 for i in a]) / len(a)) ** 0.5)