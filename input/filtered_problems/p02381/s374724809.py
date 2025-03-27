while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    mean=sum(a)/n
    std=0
    for i in range(n):
        std+=(a[i]-mean)**2
    std/=n
    print(std**0.5)
