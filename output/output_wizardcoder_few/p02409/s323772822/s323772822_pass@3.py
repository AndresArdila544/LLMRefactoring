```python
n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    a[b - 1][f - 1][r - 1] += v
for j in range(4):
    for k in range(3):
        print(' '.join([str(a[j][k][l]) for l in range(10)]))
    if j != 3:
        print("####################")
``` 

Explanation:
- We can directly assign the value of `n` to the variable `n`.
- The nested loops and indexing are removed, making it more concise.
- Instead of printing a new line after each row using `(j != 3)` condition, we added a separator (`#`) in between each row using join method.
```python
####################`