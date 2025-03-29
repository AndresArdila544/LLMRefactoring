Here is the refactored version of the code:
```
while True:
    h, w = map(int, input().split())
    if not h:
        break
    for _ in range(h):
        print("#" * w)
    print()
```
This version has fewer lines and improved readability. The `for` loop is used to iterate over the rows of the grid, and the `print()` function is used to print each row. The `map()` function is used to convert the input strings to integers, and the `*` operator is used to repeat the `#` character for each column in a row. The `if` statement is used to check if the height is 0, and the `break` statement is used to exit the loop when it is.