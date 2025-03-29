```python
W, H = map(int, input().split())
for _ in range(H):
    print("#"*(2+H-3) + "#") if W > 1 else ""
```
This version uses a single line of code and the `map()` function to achieve the same functionality as the original program. The `_` is a throwaway variable used in loops that don't need to be assigned, but will still loop through the correct number of times. It also eliminates the unnecessary conditionals and splits into two separate lines for clarity.

Note: This code assumes that `W` and `H` are positive integers. If there is a possibility for negative values or non-integers being entered, you may need to add error handling to validate the input.