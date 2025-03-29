import math
n = int(input())
while True:
    if n == 0:
        break
    b = list(map(int, input().split()))
    ave = sum(b) / n
    A = [(ave - i) ** 2 for i in b]
    p = math.sqrt(sum(A) / n)
    print("{:.8f}".format(p))
    A.clear()