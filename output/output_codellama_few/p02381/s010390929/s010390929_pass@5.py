n = int(input())
while n:
    b = list(map(int, input().split()))
    ave = sum(b) / n
    p = math.sqrt(sum((ave - i)**2 for i in b) / n)
    print("{:.8f}".format(p))
    A.clear()
    n = int(input())