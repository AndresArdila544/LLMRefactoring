```python
n, m, l = map(int, input().split())
A = [[0 for _ in range(m)] for _ in range(n)]
B = [[0 for _ in range(l)] for _ in range(m)]
C = [[0 for _ in range(l)] for _ in range(n)]

for row in range(n):
    arow, brow = map(int, input().split()), list(map(int, input().split()))
    A[row] = arow
    B[row] = brow

for i in range(n):
    for j in range(l):
        C[i][j] = sum(A[i][k] * B[k][j] for k in range(m))
    if j < l - 1:
        print(C[i][j], end=" ")
    else:
        print(C[i][j])
``` 

This version of the code is more concise and easier to read. It uses list comprehensions instead of for loops, and it separates the input from the calculation into two separate steps. The output format remains consistent with the original code.

The first three lines of the original code can be combined into a single line by using the `list` function to create the matrices:
```python
n, m, l = map(int, input().split())
A, B, C = [[0 for _ in range(m)] for _ in range(n)], [[0 for _ in range(l)] for _ in range(m)], [[0 for _ in range(l)] for _ in range(n)]
```