H, W = map(int, input().split())
for i in range(1, H+1):
    print("".join("#" if (i + W) % 2 else ".", end="") + ("\n" if i < H else "")