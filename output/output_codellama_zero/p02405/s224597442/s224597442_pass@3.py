import sys
while True:
    H, W = map(int, input().split())
    if not (H*W):
        break
    else:
        if W%2 == 0:
            for i in range(H//2, -1, -1):
                print("#."*(W//2))
                print(".#"*(W//2))
        else:
            for i in range(H // 2, -1, -1):
                print("#."*(W//2)+"#")
                print(".#"*(W//2)+".")
        print("")