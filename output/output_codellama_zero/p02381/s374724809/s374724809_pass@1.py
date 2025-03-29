while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    std = sum([(ai - mean)**2 for ai in a]) / n
    print((std ** 0.5))