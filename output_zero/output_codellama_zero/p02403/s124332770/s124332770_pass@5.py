while True:
    H,W=list(map(int,input().split()))
    if H==0and W ==0:break
    print("#"*W)
    for i in range(H):print("#"*W)