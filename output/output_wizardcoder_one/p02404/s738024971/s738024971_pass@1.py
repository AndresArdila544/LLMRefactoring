H, W = map(int, input().split())
for i in range(max(1, H+1):
    for j in range(W+1):
        print("#" if (i == 0 or i == H-1) or (j == 0 or j == W-1) else ".", end="")
    print()
print("")