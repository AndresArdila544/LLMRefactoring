while True:
    H, W = map(int, input().split())
    if not (H and W): break
    for _ in range(H): print('#' * W)
    print()