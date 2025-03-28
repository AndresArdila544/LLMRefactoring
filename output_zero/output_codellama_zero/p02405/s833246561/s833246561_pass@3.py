```
while True:
    H, W = input().split()
    H, W = int(H), int(W)
    if H == 0 and W == 0:
        break
    a = "".join("#" for _ in range(W // 2)) + "." * (W - W // 2)
    b = "." * (W // 2) + "".join("#" for _ in range(W - W // 2))
    for i in range(H):
        if i % 2 == 0:
            print(a)
        else :
            print(b)
    print()
```