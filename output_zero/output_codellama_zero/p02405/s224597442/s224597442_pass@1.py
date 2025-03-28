while True:
    H, W = map(int, input().split())
    if not (H > 0 and W > 0): break
    print("#." * (W // 2), end="")
    for i in range(H//2 - 1, -1, -1):
        print(".#" * (W // 2), end="")
        if H % 2 == 1 and i == 0:
            print("#." * (W // 2))
        print("")