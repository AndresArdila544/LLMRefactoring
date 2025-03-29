Refactored version:
```python
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    
    for i in range(H):
        row = ""
        for j in range(W):
            if (i + j) % 2 == 1:
                row += ". "
            else:
                row += "# "
        print(row[:-1])
```

Explanation:
The original code iterates through the rows and columns of a matrix, printing a `#` or `.` character based on whether `(i+j) % 2 == 1`. The `if (i + j) % 2 == 1:` condition is true when either i or j is odd, since they are added together and the sum is odd. To reduce lines of code and improve readability, we can concatenate the row using a string instead of printing it inside each loop iteration. Additionally, we can use `print(row[:-1])` to remove the trailing space at the end of each row. This version does not require the creation of any new variables or lists, so is more concise and easier to understand than the original code.