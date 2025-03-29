Here is the refactored version of the code:
while True:
    H, W = input().split()
    if (H == "0" and W == "0"):
        break
    a = "#" * int(W) + "." * (int(W) - 1)
    b = "." * int(W) + "#" * (int(W) - 1)
    for i in range(0, H):
        if i % 2 == 0:
            print(a)
        else:
            print(b)