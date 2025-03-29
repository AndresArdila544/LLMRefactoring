while True:
    HM = input().split()
    if not all(HM):
        break
    H, M = map(int, HM)
    for _ in range(H):
        print("#" * M)
        if _ == H - 1:
            print()