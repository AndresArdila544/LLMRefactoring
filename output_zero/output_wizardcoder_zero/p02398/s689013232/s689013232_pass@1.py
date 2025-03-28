```python
print(sum([1 for i in range(a, b+1) if c % i == 0]) 
```

This code uses a list comprehension and a generator expression to count the number of divisors of `c` within the range [`a`, `b`]. The `sum()` function takes a list of integers as its argument, which is created by the list comprehension, and returns the sum of all the values in the list.