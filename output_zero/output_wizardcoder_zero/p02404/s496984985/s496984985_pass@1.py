```python
for _ in range(int(input()) + 1):
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    print("#" * H)
    for i in range(1, W - 1):
        print("#." * (H - 2) + "#")
print("#" * H)
``` 

Explanation: 
- The original code has a while loop that runs indefinitely until it receives input values for `W` and `H`. 
- It then prints `#` followed by (H-2) `.`'s, followed by another `#`, to create the pattern of `#.#` for each row.
- Once it receives `(0, 0)` as input values, the loop terminates and exits. 
- The refactored code uses a `for` loop with a conditional statement that iterates over the range from `1` to `W - 2`, instead of using a while loop.
- The `print("#" * H)` at the end prints the top and bottom border of the pattern. 
- The `if W == 0 and H == 0` condition is incorporated into the `for` loop's break statement, so that it exits when `(0, 0)` are received as input values.
- Instead of using a separate `print("#"+"."*(H-2)+"#")` for each row, the code uses string multiplication to create the pattern in a single line. 
- The refactored code should be more concise and easier to read than the original one.