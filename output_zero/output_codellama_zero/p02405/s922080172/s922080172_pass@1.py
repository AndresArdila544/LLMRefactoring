XS = list(map(int, open(0).read().split()))
B = ["#."*150, ".#"*150]
for i in range(0, len(XS), 2):
    H = XS[i]
    W = XS[i+1]
    if H == 0 and W == 0:
        break
    for j in range(H):
        print(B[j%2][0:W])
    print("")