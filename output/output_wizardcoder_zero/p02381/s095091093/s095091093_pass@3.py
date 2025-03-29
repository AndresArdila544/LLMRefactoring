n = int(input())
while n != 0:
    s = list(map(int, input().split()))
    print((sum([m - sum(s) / n) ** 2 for m in s]) / n) ** 0.5