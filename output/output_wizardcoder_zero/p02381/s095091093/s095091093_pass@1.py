n = int(input())
while n != 0:
    s = list(map(int, input().split()))
    sum_s = sum(s)
    mean = sum_s / len(s)
    print((sum([(m - mean)**2 for m in s]) / len(s)) ** .5)