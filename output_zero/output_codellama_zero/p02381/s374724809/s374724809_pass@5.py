while True:
    n=int(input())
    if n==0:
        break
    a=[int(x) for x in input().split()]
    mean=sum(a)/n
    std=sum((x-mean)**2 for x in a)/n
    print(std**0.5)