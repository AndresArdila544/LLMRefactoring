import math

while True:
    n = int(input())
    if n == 0:
        break
    data = list(map(int, input().split()))
    m = float(sum(data) / n)
    for i in data:
        aa += float((i - m) ** 2) / n
    a = math.sqrt(aa)
    print(a)