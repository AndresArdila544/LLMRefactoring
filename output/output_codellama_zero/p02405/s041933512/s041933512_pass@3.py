while True:
    
    H,W = map(int,input().split())
    
    if H==0 and W==0:
        break
    
    for i in range(H):
        print("".join("#" if (i+j)%2 else "." for j in range(W)))
    print()