while True:
    n = int(raw_input())
    if n==0: break
    l = map(float, raw_input().split())
    avg=sum(l)/len(l)
    naka=0
    for i in l:
        naka+=(i-avg)**2
    hyo2 = naka/n
    print (hyo2)**0.5
