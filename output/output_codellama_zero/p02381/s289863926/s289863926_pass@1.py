import statistics
while True:
    n = int(input())
    if n==0: break
    l = list(map(float, input().split()))
    avg=statistics.mean(l)
    hyo2 = ((sum((i-avg)**2 for i in l))/n)**0.5
    print (hyo2)