```python
while True:
    N = list(map(int,input().split()))
    if not all(N): # finish condition
        break
    for i in range(1, N[0] + 1): # H-1 to include the last row as well
        print("#" * (i == 0 or i == N[0]) + "#" * (N[1] - 2) + "#" if i != N[0] else "")
print() 
```

Explanation: 
The original code creates a nested loop that prints `#` and `.` based on the input values. The outer loop runs from `1 to H`, while the inner loop runs from `1 to W-2`. If `i == 0 or i == N[0]` then we want to print `#` otherwise, we want to print ".". We can use string concatenation and a conditional statement to achieve this in a single line. The `+ ""` is used to append an empty string for the last row that should only have `#` and not `.`. Finally, there's a new line character at the end of each row so we need a separate print statement after the inner loop completes.

The refactored version uses list comprehension and conditional expressions to achieve the same functionality in fewer lines. We check if `i == 0 or i == N[0]` using a ternary operator to determine what character(s) to print, then print `"#" * (N[1] - 2)` for the middle part of the row and `""` if it's not the last row. The outer loop uses a range function with `+1` to include the last row in the iteration.

The `not all(N)` check is used as a break condition, since we don't need to iterate any further after we have reached 0 or 0 values for H and W. 

I hope this helps! Let me know if you have any questions.