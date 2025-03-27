while 1:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    else:
        for h in range(H):
            print('#' * W)
        print()