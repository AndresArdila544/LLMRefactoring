```python
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    else:
        print("#."*(W//2) + "\n"*((H-1)//2)
        print(".#"*(W//2)+".")*(H%2==1))
```

This code replaces the original while loop with a single line that first reads input and then prints the output based on the given conditions.