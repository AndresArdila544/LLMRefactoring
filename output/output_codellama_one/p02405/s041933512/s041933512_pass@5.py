while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    
    for i in range(H):
        for j in range(W):
            print((i + j) % 2 == 1 and "." or "#", end='')
        print()
    print()