Here is the refactored version of your code:
```
XS = list(map(int, open(0).read().split()))
B = ["#."*150, ".#"*150]
for H, W in zip(XS[::2], XS[1::2]):
    if H == 0 and W == 0:
        break
    for _ in range(H):
        print(B[_ % 2][:W])
    print("")
```