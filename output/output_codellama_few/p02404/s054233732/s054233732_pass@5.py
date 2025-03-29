import sys

n = list(map(int, input().split()))
if n[0] + n[1] == 0:
    sys.exit()
else:
    for i in range(0, n[0]):
        print("#", end="")
        if i == 0 or i == (n[0] - 1):
            for j in range(1, n[1]-1):
                print("#", end="")
            print("#")
        else:
            for j in range(1, n[1]-1):
                print(".", end="")
            print("#")
print("\n")