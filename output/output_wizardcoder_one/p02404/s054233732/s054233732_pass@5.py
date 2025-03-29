```python
while True:
    N = list(map(int, input().split()))
    if sum(N) == 0:
        break # finish
    for i in range(N[0]):
        print("#"*(2*N[1]) if i == 0 or i == (N[0]-1) else "#."*(N[1]-2), end="\n")
``` 

This version has less code and is more concise. The `if` statement has been replaced with a ternary operator, which improves readability by reducing the number of lines required to print the top and bottom bars of the pyramid. Additionally, the range function now only iterates up to N[0] instead of 2*N[1], ensuring that the first and last rows are correctly printed with a `#` in each cell.

The final line of the program is also simplified from `print("\n")` to using `end="\n"` as an argument to the print function. This prevents the need for an extra print statement, which reduces the amount of code by 1. 

Note: this version assumes that input is given in the format of two integers N[0] and N[1]. If you require the program to check for `N` being a tuple or list, you can add this functionality to the while loop condition. Additionally, if you want to remove the quotation marks from around the `#` characters, simply replace `"#"` with `'#'`.