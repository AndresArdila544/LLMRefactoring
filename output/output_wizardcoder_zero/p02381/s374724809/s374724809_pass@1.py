n = int(input())
while n > 0:
    a = list(map(int, input().split()))
    mean = sum(a) / len(a)
    std = ((sum((x - mean) ** 2 for x in a) / len(a)) ** 0.5)