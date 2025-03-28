```python
print(sum(1 for i in range(a, b+1) if c % i == 0))
```

This version uses a generator expression to count the number of factors of `c` within the range [`a`, `b+1`) and then applies the built-in `sum()` function to sum up all the values in the generator. This is more concise, faster, and easier to read than using a loop with an if statement inside it.