Here is a refactored version of the original program:
while True:
    H, W = map(int, input().split())
    if not (H == 0 and W == 0):
        if W % 2 == 0:
            for i in range(H // 2, -1, -1):
                print("#." * (W // 2) + "\n" * (i == H // 2))
                print(".#" * (W // 2) + "\n" * (i == H // 2))
        else:
            for i in range(H // 2, -1, -1):
                print("#." * ((W + 1) // 2) + "#")
                print(".#" * ((W + 1) // 2) + ".")
        print("")