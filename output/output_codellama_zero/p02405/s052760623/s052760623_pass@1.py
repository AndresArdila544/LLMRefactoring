import sys

while True:
    H, W = map(int, input().split())
    if not (W > 0 and H > 0):
        break
    for i in range(H):
        for j in range(W):
            print("#" if (i + j) % 2 == 0 else ".", end="")
        print()
    print()