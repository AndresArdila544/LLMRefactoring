H, W = map(int, input().split())
while (W > 0 and H > 0):
    for i in range(H):
        for j in range(W):
            if ((i % 2 == 0) and (j % 2 != 0)) or ((i + 1) % 2 != 0 and (j % 2 == 0)):
                print("#", end="")
            else:
                print(".", end="")
        print()
    W, H = map(int, input().split())

"""