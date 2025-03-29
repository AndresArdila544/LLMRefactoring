```python
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        row = "." * (W // 2) + "#" * ((W + 1) % 2)
        print(row[:W])
```

Explanation:

- The while loop continues until the input values of H and W are both 0, which is when we want to stop.
- For each row, we create a string with "." * (W // 2) + "#" * ((W + 1) % 2) characters. This string will have half as many dots as there are columns in the grid and 1 more if W is odd, because we want to alternate between dots and hashes. 
- We use slicing to print only the first W characters of the string, which gives us the desired pattern. The [:W] slice operator means "print the first W elements".
- Note that we do not need any if-else statements since both options print either a dot or a hash.
```python
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    row = "." * (W // 2) + "#" * ((W + 1) % 2)
    print(row[:W])
```

This code is more concise, easier to read, and reduces the complexity of nested loops.