```python
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    else:
        for i in range(H // 2):
            print("#." * (W // 2) + "#" if H % 2 != 0 or i < H - 1 else "#." * ((W // 2) + W % 2))
            print(".#" * (W // 2) + ".")
        
```