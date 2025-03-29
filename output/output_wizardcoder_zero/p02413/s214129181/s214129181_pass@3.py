Here is the refactored version of the code that preserves its functionality and improves its readability:

```python
a, b = map(int, input().split())
bs = [list(map(int, input().split())) for _ in range(a)]  # Use `_` as a throwaway variable to avoid creating unnecessary loop counter
for i in range(b):
    bs.append(sum([row[i] for row in bs]))
print(*[" ".join(map(str, row)) for row in bs])
```

Explanation: 
- The original code reads two numbers `a` and `b` from input and initializes a list `bs`.
- It then creates another list by iterating through each row of the matrix (given as inputs) and summing up the values for that row using a list comprehension.
- Finally, it appends this sum to the matrix.
- The last step is to iterate through the matrix and print each row with space-separated elements in each line using a list comprehension.