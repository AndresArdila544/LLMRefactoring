while True:
    H, W = map(int, input().split())
    
    if not (H and W):
        break
    
    for i in range(1, H - 1):
        print("#" * (W + 2)
        
    if H > 1:
        print("#", end="")
        
    for j in range(W):
        if j != 0 and j != W - 1:
            print(".", end="")
            
    if H > 1:
        print("#", end="")
        
    print("\n")