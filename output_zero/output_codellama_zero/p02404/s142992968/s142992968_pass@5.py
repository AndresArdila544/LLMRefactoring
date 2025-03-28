while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0: break
    print('#' * W + '\n' + ('#.' * (W - 2) + '#\n') * (H - 2) if W > 2 else '')