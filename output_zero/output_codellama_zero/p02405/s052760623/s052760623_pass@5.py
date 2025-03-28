Here is a refactored version of the code:

H, W = map(int, input().split())
while H > 0 and W > 0:
    for i in range(H):
        for j in range(W):
            if (i % 2 == 0) ^ (j % 2 == 0):
                print("#" if j % 2 else ".", end="")
        print()
    print()
    H, W = map(int, input().split())