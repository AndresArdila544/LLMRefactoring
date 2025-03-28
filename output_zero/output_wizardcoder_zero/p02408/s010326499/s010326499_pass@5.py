```python
C = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]]
for _ in range(int(input())):
    i, j = input().split()
    if i == 'S': C[0][int(j) - 1] = 0
    elif i == 'H': C[1][int(j) - 1] = 0
    elif i == 'C': C[2][int(j) - 1] = 0
    else: C[3][int(j) - 1] = 0
for r, row in enumerate(C):
    for c, col in enumerate(row):
        if col != 0 and (r == 0 or r == 1): print('{} {}'.format(['S', 'H'][r], c + 1), end=' ')
        elif col != 0: print('D {}'.format(c + 1), end=' ')
    print()
```

Explanation: 
- We initialize an empty list `C` with three sublists. Each sublist represents a row in the final output matrix.
- The first loop appends four lists `[1, 2, 3, 4, 5]`, `[6, 7, 8, 9, 10]`, and `[11, 12, 13]` to `C` respectively. 
- The second loop reads the input for each row in a string format of `'S i'` or `'H j'`, where `i` is the column index (starting from 1) and `j` is the row index (starting from 1). If it is not 'S', 'H', or 'C', then we assume it to be 'D'. 
- The `if-else` statements update the value of each element in the corresponding sublist. 
- The third loop iterates through each row and column in `C`, checking if the value is non-zero, and prints the corresponding letter followed by the column index (starting from 1). If it's not a header row, we print 'D', otherwise print 'S' or 'H'. We use the ternary operator `['S', 'H'][r]` to get the appropriate string for each row.