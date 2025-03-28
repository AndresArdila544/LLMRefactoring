while True:
    n=int(input())
    if n==0:
        break
    a=[int(i) for i in input().split()]
    mean=sum(a)/n
    std=sum((x-mean)**2 for x in a)
    std/=n
    print(std**0.5)