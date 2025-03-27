while True:
    num = [int(i) for i in input().split(" ")]
    H = num[0]
    W =num[1]
    if W == H == 0:
        break
    print("#" * W + "\n")
    print( ( ("#" + "." * (W - 2) + "#" ) + "\n") * (H -2) )
    print("#" * W)