while True:
    H,W= list(map(int, input().split()))
    if H == 0 and W == 0:
        break
    x = "#" * W
    for i in range(H):
        print(x)
    print()
