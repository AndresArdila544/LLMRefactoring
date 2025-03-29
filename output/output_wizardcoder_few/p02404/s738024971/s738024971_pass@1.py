```python
while True:
    H, W = map(int, input().split())
    
    if H == W == 0:
        break
    
    for i in range(1, H + 1):
        print("#" * (W - 2) + ".\n" if i == 1 or i == H else "#" + "." * (W - 2) + "#", end = "")
        
print("")
```