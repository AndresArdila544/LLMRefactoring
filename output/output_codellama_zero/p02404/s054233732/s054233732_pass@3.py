Here is the refactored version of the code:
```
N = list(map(int,input().split()))
if N[0] + N[1] == 0:
    judge = False
else:
    for i in range(0, N[0]):# H
        if i == 0 or i == (N[0] - 1):
            print("#" * (N[1] - 2) + "#")
        else:
            print(".", end="")
            print("#", end="")
    print("\n")
```