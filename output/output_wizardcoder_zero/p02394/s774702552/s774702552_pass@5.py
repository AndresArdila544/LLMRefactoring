```
W, H, x, y, r = map(int, input().split())
if W - r >= x > 0 and H - r >= y > 0:
    print("Yes")
else:
    print("No")
```