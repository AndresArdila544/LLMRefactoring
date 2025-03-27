while True:
    H,W = map(int, input().split(" "))
    if W == H == 0: break
    print("#" * W + "\n")
    print(( "#" + "." * (W - 2) + "#" ) + "\n" * (H - 2))
    print("#" * W)