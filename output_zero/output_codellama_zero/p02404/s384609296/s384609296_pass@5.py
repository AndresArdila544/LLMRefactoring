while True:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            break
        else:
            print('#' * W)
            for i in range(H - 2):
                print(f"{'#'.join(['']*(W-2))}#")
            print('#' * W)