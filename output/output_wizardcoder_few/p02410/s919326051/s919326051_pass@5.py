```python
n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = [int(input()) for _ in range(m)]
for i in range(n):
  value = sum(a * b for a, b in zip(A[i], B))
  print(value)
```

Explanation: 
- In the first line, we get `n` and `m` values from input and convert them to integers.
- In the second line, we use list comprehension to create a nested list `A` that contains `n` rows of `m` numbers as elements, where each row is separated by space.
- In the third line, we use another list comprehension to create a list `B` with `m` integers that can be used for multiplication in the next loop.
- The loop iterates over each row of matrix `A` and multiplies it with corresponding value in list `B`.
- We then append the product to a new list `res` which will store all the products. 
- Finally, we print each element of `res` separated by space using `print(*res, sep=' ')` statement.