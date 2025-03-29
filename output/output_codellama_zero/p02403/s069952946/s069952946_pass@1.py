def print_grid(H, W):
    for j in range(1, H+1):
        for i in range(1, W+1):
            print("#", end="")
        print()

print_grid(int(input()), int(input()))