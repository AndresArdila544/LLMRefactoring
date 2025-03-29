while True:
    try:
        H, W = (int(x) for x in input().split(" "))
    except ValueError:
        break
    if not H and not W:
        break
    print("#" * W + "\n")
    for _ in range(H - 2):
        print((("#" + "." * (W - 2) + "#")) + "\n")
    print("#" * W)