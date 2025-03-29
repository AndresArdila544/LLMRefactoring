n = int(input())
while n != 0:
    a = list(map(float, input().split()))
    average = sum(a) / len(a)
    print((sum([(i - average) ** 2 for i in a]) / (len(a)-1)) ** 0.5)
    n = int(input())