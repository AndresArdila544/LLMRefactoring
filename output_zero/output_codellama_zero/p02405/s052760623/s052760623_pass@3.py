```
H, W = map(int, input().split())
while H > 0 and W > 0:
    for i in range(H):
        for j in range(W):
            if (i % 2 == 0) and (j % 2 == 0):
                print("#", end="")
            elif (i + 1) % 2 == 0 and (j + 1) % 2 == 0:
                print("#", end="")
            else:
                print(".", end="")
        print()
    H, W = map(int, input().split())
```