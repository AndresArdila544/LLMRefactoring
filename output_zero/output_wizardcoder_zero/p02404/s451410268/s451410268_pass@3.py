while True:
    num = [int(i) for i in input().split()]
    H, W = num[0], num[1]
    if H == 0 and W == 0:
        break
    print("#" * W + "\n")
    ((print("#." * (W - 2) + "#\n") for _ in range(H-2))
    print("#" * W)