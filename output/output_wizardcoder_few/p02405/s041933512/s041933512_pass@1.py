```python
while True:
    H, W = map(int, input().split())
    
    if H == 0 and W == 0:
        break
    
    for i in range(H):
        row = []
        for j in range(W):
            if (i+j) % 2 == 1:
                row.append(".")
            else:
                row.append("#")
        print("".join(row))
```