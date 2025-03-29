```python
r, c = map(int, input().split())
a = []
for i in range(r):
    a.append([sum(map(int, input().split()))] + list(map(int, input().split()))
print(*[x[:c-1] for x in zip(*a)])
print(sum(x[-1] for x in a))
```

Explanation:
The original code creates an array `a` of size r x c, where each row contains integers separated by space. The first `r` lines are the rows of the matrix and the last line is the total sum of all columns.

We can reduce the complexity of the code by using list comprehension to create a 2D array and then use `zip()` function with a transpose to get the matrix, and then calculate the row sums. We can also add the row sums in the same loop.

The first line is reduced from `a = []` to `a = [[]]`. The rest of the code remains unchanged.

```python
r, c = map(int, input().split())  # get dimensions of matrix
for i in range(r):
    a.append([sum(map(int, input().split())] + list(map(int, input().split()))  # append row and sum to array
a = list(zip(*a[::-1]))   # transpose matrix
print(' '.join(str(x) for x in [x[:c-1] for x in a])  # print rows except last column
print(sum(x[-1] for x in a))  # print total sum of columns. 
```