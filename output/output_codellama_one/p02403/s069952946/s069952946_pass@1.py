Here is a refactored version of your program:

while True:
    H, W = map(int, input().split())
    if (H, W) == (0, 0):
        break
    print("#" * (W + 1))