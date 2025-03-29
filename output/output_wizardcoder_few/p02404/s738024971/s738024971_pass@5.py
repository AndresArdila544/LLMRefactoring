```python
while True:
    H, W = map(int, input().split())
    
    if H == W == 0:
        break
    
    for i in range(H):
        print("#" + "#"*(W-2) + ("#" if i==0 or i==H-1 else ".") + "\n"
              + ("#" * ((i!=0 and i!=H-1)) * (W-2) + "."*(W-2) + ("#" if i==0 or i==H-1) + "\n" if i<H-2 else "")
              + "#"*(W-2)
              , end="")
    print("")