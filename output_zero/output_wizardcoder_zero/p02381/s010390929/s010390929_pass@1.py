A=[]
while True:
    n = int(input())
    if n == 0:
        break
    
    else:
        b = list(map(int, input().split()))
        avg = sum(b) / n
        for i in range(n):
            A.append((avg - b[i]) ** 2)
        p = math.sqrt(sum(A) / n)
        print("{:.8f}".format(p))
        A.clear()