while True:
    
    H, W = map(int, input().split())
    
    if H == W == 0:
        break
    
    for i in range(H):
        for j in range(W):
            print("#" if i in [0, (H-1)] or j in [0, (W-1)] else ".", end = "")
        
        print("")
        
    print("")