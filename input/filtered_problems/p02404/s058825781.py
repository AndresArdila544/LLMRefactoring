XS = list(map(int, open(0).read().split()))
for i in range(0, len(XS), 2):
    H = XS[i]
    W = XS[i+1]
    if H == 0 and W == 0:
        break
    print("#"*W)
    for _ in range(H-2):
        print("#{}#".format("." * (W-2)))
    print("#"*W)
    print("")
