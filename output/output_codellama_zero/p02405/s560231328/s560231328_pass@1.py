```
import sys
ct = 0
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    
    so = ""
    se = ""
    for j in range(W):
        if j & 1:
            se += "#"
            so += "."
        else:
            se += "."
            so += "#"
    
    for i in range(H):
        if i & 1:
            print(so)
        else:
            print(se)
        sys.stdout.write("\n")
```