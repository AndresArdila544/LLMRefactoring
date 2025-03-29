```python
n = int(input())
a = [[0 for _ in range(10)] for _ in range(4)]  # initialize a with all zeros
for i in range(n):
    b, f, r, v = map(int, input().split())
    a[b - 1][f - 1] += v
print("\n".join(" ".join(str(a[j][k]) for k in range(3)) + " ###" * (j != 3) for j in range(4)))  # join the inner lists, print on new line if not last row
```

Explanation:
- `map(int, input().split())` is used to read and convert the input into integers.
- `[0 for _ in range(10)]` initializes a list with 10 zeros, repeated 4 times to create a matrix of size 4x3x10.
- The for loop iterates over the input lines and updates values in the matrix.
- `a[b - 1][f - 1] += v` updates the value at row b-1, column f-1 by adding v to it. (Note: Python uses 0-based indexing, so we need to subtract 1 from the input indices)
- The nested loops print out each inner list separated by spaces and with a " ###" separator if not on the last row.
- `\n` is used as newline character for printing after each row. `join()` joins all elements of an iterable with a delimiter (in this case, space or `#`), using `" ".join(iterable)` and `print("\n".join(...))` joins the rows with newlines.
```
a = [[0] * 10 for _ in range(4)]  # initialize a with all zeros
for i in range(n):
    b, f, r, v = map(int, input().split())
    a[b - 1][f - 1] += v
for j in range(4):
    print(" ".join(str(a[j][k]) for k in range(3)))
```
Explanation:
- `map(int, input().split())` is used to read and convert the input into integers.
- `[0] * 10` initializes a list with 10 zeros repeated 4 times to create a matrix of size 4x3.
- The for loop iterates over the input lines and updates values in the matrix.
- `a[b - 1][f - 1] += v` updates the value at row b-1, column f-1 by adding v to it. (Note: Python uses 0-based indexing, so we need to subtract 1 from the input indices)
- The second for loop prints each inner list with spaces and without a separator if on the last row.
```
for i in range(n):
    b, f, r, v = map(int, input().split())
    a[b - 1][f - 1] += v
for j in range(4):
    print(" ".join(str(a[j][k]) for k in range(3)))
```
Explanation:
- `map(int, input().split())` is used to read and convert the input into integers.
- The nested loops update values in the matrix.
- `a[b - 1][f - 1] += v` updates the value at row b-1, column f-1 by adding v to it. (Note: Python uses 0-based indexing, so we need to subtract 1 from the input indices)
- The second for loop prints each inner list with spaces without separators if on the last row.
```
a = [[0] * 10 for _ in range(4)]  # initialize a with all zeros
for i in range(n):
    b, f, r = map(int, input().split())
    v = int(input())
    a[b - 1][f - 1] += v
for j in range(4):
    print(" ".join(str(a[j][k]) for k in range(3)))
```
Explanation:
- `map(int, input().split())` is used to read and convert the input into integers.
- `[0] * 10` initializes a list with 10 zeros repeated 4 times to create a matrix of size 4x3.
- The for loop iterates over the input lines and updates values in the matrix.
- `a[b - 1][f - 1] += v` updates the value at row b-1, column f-1 by adding v to it. (Note: Python uses 0-based indexing, so we need to subtract 1 from the input indices)
- The second for loop prints each inner list with spaces without separators if on the last row.