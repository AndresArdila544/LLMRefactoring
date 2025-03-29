n = int(input())
while True:
    H = list(map(int, input().split()))
    if H[0] + H[1] == 0:
        break
    else:
        for i in range(H[0]): # H
            print("#", end="")
            if i == 0 or i == (H[0] - 1):
                for j in range(1, H[1]-1):
                    print("#", end="")
            else:
                for j in range(1, H[1]-1):
                    print(".", end="")
                print("#\n")