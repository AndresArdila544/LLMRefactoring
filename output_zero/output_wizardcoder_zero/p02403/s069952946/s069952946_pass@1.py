```python
while True:
    H, W = map(int, input().split())
    if (H,W) == (0, 0):
        break
    for j in range(1, H+1):
        print("#" * W)
```

The original code is equivalent to the refactored version, as it accomplishes the same task with fewer lines and improved readability. The `map` function converts a list of string input into a tuple of integers for `H` and `W`, and then the loop prints `#` character `W` times for each value of `j` from 1 to `H+1`. Since we do not need the outer loop, it can be removed as well.