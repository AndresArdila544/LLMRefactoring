n = int(input())
while n > 0:
    a = [float(i) for i in input().split()]
    average = sum(a) / len(a)
    print((sum([(i - average) ** 2 for i in a]) / len(a)) ** 0.5)
    n -= 1