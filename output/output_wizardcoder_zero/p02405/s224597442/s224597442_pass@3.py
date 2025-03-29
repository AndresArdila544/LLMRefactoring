```python
def print_half_pyramid(H, W):
    if H == 0 and W == 0:
        return
    
    if W % 2 == 0:
        i = H//2
        while i > 0:     
            print("#."*(W//2) + "#"*(H - (i*2)) + "\n" + ".#"*(W//2) + "#")
            i -= 1
    else:
        i = H // 2
        while i > 0:     
            print("#."*(W//2)+".#"*(H - (i*2)) + "\n" + ".#"*(W//2)+"." if i == 1 else "#."*(W//2) + "#\n" + ".#"*(W//2)+".")
            i -= 1
        
for _ in range(int(input()) - 1):
    H, W = map(int, input().split())
    print_half_pyramid(H, W)
```