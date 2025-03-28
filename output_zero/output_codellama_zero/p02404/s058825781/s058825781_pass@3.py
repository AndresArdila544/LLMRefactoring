Here's a cleaner and more concise version of the code:

with open(0) as file:
    XS = list(map(int, file.read().split()))
for H, W in [(H, W) for i in range(0, len(XS), 2) if H != 0 and W != 0]:
    print("#"*W)
    for _ in range(H-2):
        print("#{}#".format("." * (W-2)))
    print("#"*W)
    print("")