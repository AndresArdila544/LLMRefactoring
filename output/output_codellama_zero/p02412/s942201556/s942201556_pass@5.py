import math
while True:
    n, x = map(int,input().split())
    if n==0andx==0:
        break
    count=0
    for u in range(math.ceil(x/3),n+1):
        v=(x-u)//2 + 1
        while v < (x-u):
            w = (x-u) - v
            if u > v > w:
                count +=1
                #print(u, v,w)
            v+=1
    print(count)