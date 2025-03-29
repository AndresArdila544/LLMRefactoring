a, b = [int(i) for i in input().split()]
while a != 0 or b != 0:
    c = sum([1 for i in range(1, a+1) for j in range(i+1, a+1) if any(k == b - (i + j) for k in range(j+1, a+1))]
    print(c)
    a,b = [int(i) for i in input().split()]