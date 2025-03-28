```python
while True:
    H, W = input().split()
    if int(H) == 0 and int(W) == 0:
        break
    a, b = "", ""
    for i in range(int(W)):
        if i % 2 == 0:
            a += "#"
            b += "."
        else:
            a += "."
            b += "#"
    for i in range(int(H):
        print("{}{}".format("#" * int((i % 2 == 0), "." * int(i % 2 != 0)) * W)
```

Note: I have used the ternary operator to reduce the if-else statements.